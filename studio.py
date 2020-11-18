from PySide2.QtWidgets import QMainWindow, QApplication
from studio_ui import Ui_MainWindow

from composition import *
import subprocess
import sys



KEYS = ["C", "G", "D", "A", "E", "B"]

TIME_SIGNATURES = {
	'4/4': (4, 4),
	'3/4': (3, 4),
	'2/4': (2, 4),
	'2/2': (2, 2),
	'6/8': (6, 8),
	'7/8': (7, 8),
	'5/16': (5,16)
}

OUTPUT_FILEPATH = "output\\"

class Studio(QMainWindow):
	def __init__(self):
		super(Studio, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.init_ui()


	def init_ui(self):

		pass


# create_ly(content, 'testttt')

# subprocess.call(["lilypond", "long.ly"])


app = QApplication(sys.argv)
app_window = Studio()

app_window.show()
sys.exit(app.exec_())