from PySide2.QtWidgets import QMainWindow, QApplication, QButtonGroup, QFileSystemModel, QFileDialog
from PySide2.QtCore import QDir
from studioui import Ui_MainWindow


from custom_logging import *
from composition import *
import sys
import os
import pickle
import time


NOTES = ["A", "B", "C", "D", "E", "F", "G"]
ACCIDENTALS = ["♮", "♯", "♭"]
SCALES = ["major", "minor", "harmonic", "melodic"]


class Studio(QMainWindow):
	def __init__(self):
		super(Studio, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.configuration = {} # always represents active ui
		self.init_user_input_vars()

		self.init_ui()

	def init_ui(self):

		self.ui.nav_group = QButtonGroup()
		self.ui.nav_group.addButton(self.ui.nav_configure)
		self.ui.nav_group.addButton(self.ui.nav_write)

		self.ui.ranges_group = QButtonGroup()
		self.ui.ranges_group.addButton(self.ui.sharp_ranges)
		self.ui.ranges_group.addButton(self.ui.flat_ranges)
		self.ui.sharp_ranges.setCheckable(True)
		self.ui.flat_ranges.setCheckable(True)
		self.ui.sharp_ranges.setChecked(True)

		# Signal Connections
		# connected function is an update function
		# update functions are always called in response to user input updates
		# to modify class attributes and call other methods to update other display areas when needed
		# some updates use other functions to handle the attribute change


		self.ui.nav_group.buttonClicked.connect(self.navigate)

		self.ui.save.clicked.connect(self.save_configuration)


		# Configure
		self.ui.measures.textEdited.connect(self.update_measures)



		self.ui.timesig_num.textEdited.connect(self.update_timesig)
		self.ui.timesig_den.textEdited.connect(self.update_timesig)

		self.ui.keysig_note.currentTextChanged.connect(self.update_keysig_note)
		self.ui.keysig_acc.currentTextChanged.connect(self.update_keysig_acc)
		self.ui.keysig_scale.currentTextChanged.connect(self.update_keysig_scale)

		self.ui.ranges_group.buttonClicked.connect(self.update_ranges_mode)
		self.ui.lh_range1_slider.valueChanged.connect(self.update_lh_range1)
		self.ui.lh_range2_slider.valueChanged.connect(self.update_lh_range2)
		self.ui.rh_range1_slider.valueChanged.connect(self.update_rh_range1)
		self.ui.rh_range2_slider.valueChanged.connect(self.update_rh_range2)


		# Write
		self.ui.song_name.textEdited.connect(self.update_song_name)
		self.ui.song_folder.clicked.connect(self.select_song_folder)

		self.ui.pdf.stateChanged.connect(self.update_pdf)
		self.ui.midi.stateChanged.connect(self.update_midi)

		self.ui.compose.clicked.connect(self.compose)


	def init_user_input_vars(self):
		# So called user input vars are Studio level variables reflecting the current state of ui input widgets
		self.song_name = "<unnamed>"
		self.song_folder = os.getcwd()+"/output"
		# cycling inputs starting back one because update will do a cycle
		self.keysig_note_index = 1
		self.keysig_acc_index = 3
		self.keysig_scale_index = len(SCALES)-1 # allows adding more scale patterns later

		self.ranges_mode = "♯"
		self.ui.lh_range1_slider.setSliderPosition(0)
		self.ui.lh_range2_slider.setSliderPosition(39)
		self.ui.rh_range1_slider.setSliderPosition(39)
		self.ui.rh_range2_slider.setSliderPosition(87)
		self.configuration["rh_range2"] = self.ui.rh_range2_slider.value()
		self.configuration["lh_range2"] = self.ui.lh_range2_slider.value()

		self.update_all_ranges()

	# prepares self.configuration values to be passed to Composition constructor
	# returns rules dict
	# Does not hold filename or path, only music info
	def prepare_rules(self):
		rules = {}
		rules['measures'] = self.configuration['measures']
		rules['timesig'] = self.configuration['timesig']
		rules['key'] = self.assemble_key()
		rules['key_scale'] = self.configuration['keysig_scale']
		rules['lh_ranges'] = [self.lh_range1_lynotation, self.lh_range2_lynotation]
		rules['rh_ranges'] = [self.rh_range1_lynotation, self.rh_range2_lynotation]
		rules['pdf'] = self.configuration['pdf']
		rules['midi'] = self.configuration['midi']

	# runs every update method
	def update_ui(self):
		self.update_measures()
		self.update_timesig()
		self.update_keysig_note()
		self.update_keysig_acc()
		self.update_keysig_scale()
		self.update_song_name()
		self.update_all_ranges()
		self.update_extended_filepath()
		self.update_pdf()
		self.update_midi()

	def navigate(self, button):
		if button == self.ui.nav_configure:
			self.ui.configure.raise_()
		elif button == self.ui.nav_write:
			self.ui.write.raise_()

	# Compose button should only be called with a valid folder selected
	def compose(self):
		Composition(self.song_name, self.song_folder, self.prepare_rules())

	def update_song_name(self):
		self.configuration['song_name'] = self.ui.song_name.text()

	def update_measures(self):
		self.configuration['measures'] = int(self.ui.measures.text())

	def update_timesig(self):
		self.configuration['timesig']= (int(self.ui.timesig_num.text()), int(self.ui.timesig_den.text()))
		
#	def __init__(self, name, measures, timesig, key, key_scale, left_limits, right_limits, extended_filepath, pdf, midi):
	def update_keysig_note(self):   # change to cycler
		self.configuration["keysig_note"] = self.ui.keysig_note.currentText()

	def update_keysig_scale(self):
		self.configuration["keysig_scale"] = self.ui.keysig_scale.currentText()

	def update_keysig_acc(self):
		self.configuration["keysig_acc"] = self.ui.keysig_acc.currentText()

		# change range mode as needed
		if self.configuration["keysig_acc"] == "♯":
			self.ranges_mode = "♯"
			self.ui.sharp_ranges.setChecked(True)
			self.ui.sharp_ranges.setEnabled(False)
			self.ui.flat_ranges.setEnabled(False)
			self.update_all_ranges()
		elif self.keysig_acc == "♭":
			self.ranges_mode = "♭"
			self.ui.flat_ranges.setChecked(True)
			self.ui.sharp_ranges.setEnabled(False)
			self.ui.flat_ranges.setEnabled(False)
			self.update_all_ranges()
		else:
			self.ui.sharp_ranges.setEnabled(True)
			self.ui.flat_ranges.setEnabled(True)

	def update_ranges_mode(self, button):
		if button == self.ui.sharp_ranges:
			self.ranges_mode = "♯"
			self.update_all_ranges()
		else:
			self.ranges_mode = "♭"
			self.update_all_ranges()

	def update_lh_range1(self):
		self.configuration["lh_range1"] = self.ui.lh_range1_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["lh_range1"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["lh_range1"]]

		self.lh_range1_lynotation = lynotation
		self.lh_range1_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.lh_range1_label.setText(self.lh_range1_numbered)
		self.ui.lh_range1_header_label.setText(self.lh_range1_numbered)
		self.update_lh_span()

	def update_lh_range2(self):
		self.configuration["lh_range2"] = self.ui.lh_range2_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["lh_range2"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["lh_range2"]]

		self.lh_range2_lynotation = lynotation
		self.lh_range2_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.lh_range2_label.setText(self.lh_range2_numbered)
		self.ui.lh_range2_header_label.setText(self.lh_range2_numbered)
		self.update_lh_span()

	def update_lh_span(self):
		self.lh_span = self.configuration["lh_range2"] - self.configuration["lh_range1"]
		self.ui.lh_span.setText(str(abs(self.lh_span)))

	def update_rh_range1(self):
		self.configuration["rh_range1"] = self.ui.rh_range1_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["rh_range1"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["rh_range1"]]

		self.rh_range1_lynotation = lynotation
		self.rh_range1_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.rh_range1_label.setText(self.rh_range1_numbered)
		self.ui.rh_range1_header_label.setText(self.rh_range1_numbered)
		self.update_rh_span()

	def update_rh_range2(self):
		self.configuration["rh_range2"] = self.ui.rh_range2_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.configuration["rh_range2"]]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.configuration["rh_range2"]]

		self.rh_range2_lynotation = lynotation
		self.rh_range2_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.rh_range2_label.setText(self.rh_range2_numbered)
		self.ui.rh_range2_header_label.setText(self.rh_range2_numbered)

		self.update_rh_span()

	def update_all_ranges(self):
		self.update_lh_range1()
		self.update_lh_range2()
		self.update_rh_range1()
		self.update_rh_range2()

	def update_rh_span(self):
		self.rh_span = self.configuration["rh_range2"] - self.configuration["rh_range1"]
		self.ui.rh_span.setText(str(abs(self.rh_span)))

	# def update_extended_filepath(self):
	# 	self.extended_filepath = self.ui.extended_filepath.text()
	# 	if self.extended_filepath:
	# 		self.extended_filepath += "/"

	def update_pdf(self):
		self.configuration["pdf"] = self.ui.pdf.isChecked()

	def update_midi(self):
		self.configuration["midi"] = self.ui.pdf.isChecked()


	# converts lyform notation to numbered notation for display purposes for range sliders
	def lynotation_to_numbered(self, lynotation):

		clef = 3
		numbered = [lynotation[0]]

		for c in lynotation:
			if c == ",":
				clef -= 1
			elif c == "'":
				clef += 1
		if clef != 0:
			numbered.append(str(clef))
			
		if "is" in lynotation:
			numbered.append("♯")
		elif "es" in lynotation:
			numbered.append("♭")

		return "".join(numbered)

	def assemble_key(self):
		if self.keysig_acc == "♯":
			return f"{self.keysig_note.lower()}is"
		elif self.keysig_acc == "♭":
			return f"{self.keysig_note.lower()}es"
		else:
			return self.keysig_note.lower()

	def save_configuration(self):

		if configuration_filename := self._save_configuration_dialog():
			self._write_config(configuration_filename)

	def _write_config(self, configuration_filename):
		log_debug(f"pickle time")
		pickle.dump(self.configuration, open(configuration_filename, 'wb'))

	# return fp
	def _save_configuration_dialog(self):
		self.fp = ""
		self.ui.save_dialog = QFileDialog(self)
		self.ui.save_dialog.setOption(QFileDialog.ReadOnly, True) # not working
		self.ui.save_dialog.setAcceptMode(QFileDialog.AcceptSave)
		self.ui.save_dialog.setDirectory(os.getcwd()+'/configurations')
		self.ui.save_dialog.setFilter(QDir.Dirs) #idk what it does
		if self.ui.save_dialog.exec_():

			files = self.ui.save_dialog.selectedFiles()
			selected = self.ui.save_dialog.selectedUrls()
			directory = self.ui.save_dialog.directory()

			_directory = directory.path()
			_file = files[0].split("/")[-1]

			print(_file)
			print(_directory)

			fp = f"{_directory}/{_file}.cf"

			return fp

	def select_song_folder(self):
		directory = ""
		self.ui.select_folder_dialog = QFileDialog(self)
		self.ui.select_folder_dialog.setAcceptMode(QFileDialog.AcceptSave)
		self.ui.select_folder_dialog.setFileMode(QFileDialog.Directory)
		self.ui.select_folder_dialog.setDirectory(QDir(os.getcwd()+'/output'))
		if 	self.ui.select_folder_dialog.exec_():

			directory = self.ui.select_folder_dialog.selectedFiles()[0]
			direct = QDir(os.getcwd()).relativeFilePath(directory)
			self.song_folder = direct
			self.update_song_filename()

	def update_song_filename(self):
		self.ui.song_filename_label.setText(self.song_filename())

	def song_filename(self):
		return f"{self.song_folder}/{self.song_name}.ly"

	def load_configuration(self):
		if configuration_filename := self._load_dialog():
			self.configuration = pickle.load(configuration_filename)
			self.update_ui()


app = QApplication(sys.argv)
app_window = Studio()

app_window.show()
sys.exit(app.exec_())