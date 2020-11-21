from PySide2.QtWidgets import QMainWindow, QApplication, QButtonGroup
from studio_ui import Ui_MainWindow

from custom_logging import *
from composition import *
import sys

import time


NOTES = ["A", "B", "C", "D", "E", "F", "G"]
ACCIDENTALS = ["♮", "♯", "♭"]
SCALES = ["major", "minor", "harmonic", "melodic"]


class Studio(QMainWindow):
	def __init__(self):
		super(Studio, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.init_user_input_vars()

		self.init_ui()

		self.frames = [self.ui.studio, self.ui.meet_the_composer]
		self.active_frame = self.ui.studio


	def init_ui(self):

		self.ui.keyboard_cat.hide()

		self.ui.ranges_group = QButtonGroup()
		self.ui.ranges_group.addButton(self.ui.sharp_ranges)
		self.ui.ranges_group.addButton(self.ui.flat_ranges)
		self.ui.sharp_ranges.setCheckable(True)
		self.ui.flat_ranges.setCheckable(True)
		self.ui.sharp_ranges.setChecked(True)

		# Signal Connections
		# connected function is an _update function
		# _update functions are always called in response to user input updates
		# to modify class attributes and refresh other parts of the display if needed
		# some _updates use other functions to handle the attribute change
		self.ui.corner_logo.clicked.connect(self.swap_frames)
		self.ui.corner_logo_2.clicked.connect(self.swap_frames)

		self.ui.measures.textEdited.connect(self._update_measures)

		self.ui.new_name.textEdited.connect(self._update_new_name)

		self.ui.timesig_num.textEdited.connect(self._update_timesig)
		self.ui.timesig_den.textEdited.connect(self._update_timesig)

		self.ui.keysig_note.clicked.connect(self._update_keysig_note)
		self.ui.keysig_acc.clicked.connect(self._update_keysig_acc)
		self.ui.keysig_scale.clicked.connect(self._update_keysig_scale)

		self.ui.ranges_group.buttonPressed.connect(self._update_ranges_mode)
		self.ui.lh_range1_slider.valueChanged.connect(self._update_lh_range1)
		self.ui.lh_range2_slider.valueChanged.connect(self._update_lh_range2)
		self.ui.rh_range1_slider.valueChanged.connect(self._update_rh_range1)
		self.ui.rh_range2_slider.valueChanged.connect(self._update_rh_range2)

		self.ui.extended_filepath.textEdited.connect(self._update_extended_filepath)
		self.ui.pdf.stateChanged.connect(self._update_pdf)
		self.ui.midi.stateChanged.connect(self._update_midi)

		self.ui.compose.clicked.connect(self.compose)


	def init_user_input_vars(self):
		# So called user input vars are Studio level variables reflecting the current state of the user input from the ui

		# cycling inputs starting back one because _update will do a cycle
		self.keysig_note_index = 1
		self.keysig_acc_index = 3
		self.keysig_scale_index = len(SCALES)-1 # allows adding more scale patterns later

		self.ranges_mode = "♯"
		self.ui.lh_range1_slider.setSliderPosition(0)
		self.ui.lh_range2_slider.setSliderPosition(39)
		self.ui.rh_range1_slider.setSliderPosition(39)
		self.ui.rh_range2_slider.setSliderPosition(87)
		self.rh_range2 = self.ui.rh_range2_slider.value()
		self.lh_range2 = self.ui.lh_range2_slider.value()

		self._update_measures()
		self._update_timesig()
		self._update_keysig_note()
		self._update_keysig_acc()
		self._update_keysig_scale()
		self._update_new_name()
		self.refresh_range_vars() # calls all 4 range updates
		self._update_extended_filepath()
		self._update_pdf()
		self._update_midi()


	def compose(self):

		# call composition constructor
		Composition(self.new_name, self.measures, self.timesig, self.keysig_to_key(), self.keysig_scale,
			[self.lh_range1_lynotation, self.lh_range2_lynotation], [self.rh_range1_lynotation, self.rh_range2_lynotation], self.extended_filepath, self.pdf, self.midi)

	def _update_new_name(self):
		self.new_name = self.ui.new_name.text()
		self.ui.name_label_1.setText(self.new_name)

	def _update_measures(self):
		self.measures = int(self.ui.measures.text())

	def _update_timesig(self):
		self.timesig = (int(self.ui.timesig_num.text()), int(self.ui.timesig_den.text()))
		
#	def __init__(self, name, measures, timesig, key, key_scale, left_limits, right_limits, extended_filepath, pdf, midi):
	def _update_keysig_note(self):   # change to cycler
		self.cycle_keysig_note()
		self.keysig_note = NOTES[self.keysig_note_index]
		self.ui.keysig_note.setText(self.keysig_note)

	def cycle_keysig_note(self):
		if self.keysig_note_index < 7:
			self.keysig_note_index += 1
		else:
			self.keysig_note_index = 0

	def _update_keysig_scale(self):
		self.cycle_keysig_scale()
		self.keysig_scale = SCALES[self.keysig_scale_index]
		self.ui.keysig_scale.setText(self.keysig_scale)

	def cycle_keysig_scale(self):
		if self.keysig_scale_index < len(SCALES)-1:
			self.keysig_scale_index += 1
		else:
			self.keysig_scale_index = 0

# ["♮", "♯", "♭"]
	def _update_keysig_acc(self):
		self.cycle_keysig_acc()
		self.keysig_acc = ACCIDENTALS[self.keysig_acc_index]
		self.ui.keysig_acc.setText(self.keysig_acc)

		# change range mode as needed
		if self.keysig_acc == "♯":
			self.ranges_mode = "♯"
			self.ui.sharp_ranges.setChecked(True)
			self.ui.sharp_ranges.setEnabled(False)
			self.ui.flat_ranges.setEnabled(False)
			self.refresh_range_vars()
		elif self.keysig_acc == "♭":
			self.ranges_mode = "♭"
			self.ui.flat_ranges.setChecked(True)
			self.ui.sharp_ranges.setEnabled(False)
			self.ui.flat_ranges.setEnabled(False)
			self.refresh_range_vars()
		else:
			self.ui.sharp_ranges.setEnabled(True)
			self.ui.flat_ranges.setEnabled(True)

	def cycle_keysig_acc(self):
		if self.keysig_acc_index < 2:
			self.keysig_acc_index += 1
		else:
			self.keysig_acc_index = 0

	def _update_ranges_mode(self, button):
		if button == self.ui.sharp_ranges:
			self.ranges_mode = "♯"
			self.refresh_range_vars()
		else:
			self.ranges_mode = "♭"
			self.refresh_range_vars()

	def _update_lh_range1(self):
		self.lh_range1 = self.ui.lh_range1_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.lh_range1]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.lh_range1]

		self.lh_range1_lynotation = lynotation
		self.lh_range1_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.lh_range1_label.setText(self.lh_range1_numbered)
		self.ui.lh_range1_header_label.setText(self.lh_range1_numbered)
		self._update_lh_span()

	def _update_lh_range2(self):
		self.lh_range2 = self.ui.lh_range2_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.lh_range2]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.lh_range2]

		self.lh_range2_lynotation = lynotation
		self.lh_range2_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.lh_range2_label.setText(self.lh_range2_numbered)
		self.ui.lh_range2_header_label.setText(self.lh_range2_numbered)
		self._update_lh_span()

	def _update_lh_span(self):
		self.lh_span = self.lh_range2 - self.lh_range1
		self.ui.lh_span.setText(str(self.lh_span))

	def _update_rh_range1(self):
		self.rh_range1 = self.ui.rh_range1_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.rh_range1]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.rh_range1]

		self.rh_range1_lynotation = lynotation
		self.rh_range1_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.rh_range1_label.setText(self.rh_range1_numbered)
		self.ui.rh_range1_header_label.setText(self.rh_range1_numbered)
		self._update_rh_span()

	def _update_rh_range2(self):
		self.rh_range2 = self.ui.rh_range2_slider.value()
		lynotation = ""

		if self.ranges_mode == "♯":
			lynotation = pitchesre.SHARP_LIST[self.rh_range2]
		elif self.ranges_mode == "♭":
			lynotation = pitchesre.FLAT_LIST[self.rh_range2]

		self.rh_range2_lynotation = lynotation
		self.rh_range2_numbered = self.lynotation_to_numbered(lynotation)

		#update labels
		self.ui.rh_range2_label.setText(self.rh_range2_numbered)
		self.ui.rh_range2_header_label.setText(self.rh_range2_numbered)

		self._update_rh_span()


	def refresh_range_vars(self):
		self._update_lh_range1()
		self._update_lh_range2()
		self._update_rh_range1()
		self._update_rh_range2()

	def _update_rh_span(self):
		self.rh_span = self.rh_range2 - self.rh_range1
		self.ui.rh_span.setText(str(self.rh_span))

	def _update_extended_filepath(self):
		self.extended_filepath = self.ui.extended_filepath.text()
		if self.extended_filepath:
			self.extended_filepath += "/"

	def _update_pdf(self):
		self.pdf = self.ui.pdf.isChecked()

	def _update_midi(self):
		self.midi = self.ui.pdf.isChecked()

	def swap_frames(self):
		if self.active_frame == self.ui.studio:
			self.active_frame = self.ui.meet_the_composer
		else:
			self.active_frame = self.ui.studio

		self.active_frame.raise_()

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

	def keysig_to_key(self):
		if self.keysig_acc == "♯":
			return f"{self.keysig_note.lower()}is"
		elif self.keysig_acc == "♭":
			return f"{self.keysig_note.lower()}es"
		else:
			return self.keysig_note.lower()

	def flash_cat(self):
		self.ui.keyboard_cat.show()
		time.sleep(.6)
		self.ui.keyboard_cat.hide()
		time.sleep(.1)
		self.ui.keyboard_cat.show()
		time.sleep(.4)
		self.ui.keyboard_cat.hide()
		time.sleep(.1)
		self.ui.keyboard_cat.show()
		time.sleep(.1)
		self.ui.keyboard_cat.hide()
		time.sleep(.1)
		self.ui.keyboard_cat.show()
		time.sleep(.1)
		self.ui.keyboard_cat.hide()
		time.sleep(.1)
		self.ui.keyboard_cat.show()
		time.sleep(.1)
		self.ui.keyboard_cat.hide()


app = QApplication(sys.argv)
app_window = Studio()

app_window.show()
sys.exit(app.exec_())