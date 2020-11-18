# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studio.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet(u"background-color:rgb(16, 24, 24);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.meet_the_composer = QFrame(self.centralwidget)
        self.meet_the_composer.setObjectName(u"meet_the_composer")
        self.meet_the_composer.setGeometry(QRect(0, 0, 1600, 900))
        self.meet_the_composer.setFrameShape(QFrame.StyledPanel)
        self.meet_the_composer.setFrameShadow(QFrame.Raised)
        self.whitefur_photo = QLabel(self.meet_the_composer)
        self.whitefur_photo.setObjectName(u"whitefur_photo")
        self.whitefur_photo.setGeometry(QRect(20, 30, 1000, 800))
        self.whitefur_photo.setPixmap(QPixmap(u"data/composer.png"))
        self.label_3 = QLabel(self.meet_the_composer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1080, 140, 401, 401))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QFrame {\n"
"	color: rgb(137, 137, 206);\n"
"}")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.studio = QFrame(self.centralwidget)
        self.studio.setObjectName(u"studio")
        self.studio.setGeometry(QRect(0, 0, 1600, 900))
        self.studio.setFrameShape(QFrame.StyledPanel)
        self.studio.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.studio)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 210, 240, 40))
        self.lineEdit.setMinimumSize(QSize(240, 40))
        font1 = QFont()
        font1.setFamily(u"Rasa")
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")
        self.lineEdit.setCursorPosition(0)
        self.output_folder_entry = QLineEdit(self.studio)
        self.output_folder_entry.setObjectName(u"output_folder_entry")
        self.output_folder_entry.setGeometry(QRect(550, 210, 240, 40))
        self.output_folder_entry.setMinimumSize(QSize(240, 40))
        self.output_folder_entry.setFont(font1)
        self.output_folder_entry.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}")
        self.output_folder_entry.setCursorPosition(0)
        self.corner_logo = QLabel(self.studio)
        self.corner_logo.setObjectName(u"corner_logo")
        self.corner_logo.setGeometry(QRect(0, 0, 100, 100))
        self.corner_logo.setPixmap(QPixmap(u"data/images/avante-note.png"))
        self.label_2 = QLabel(self.studio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 0, 461, 71))
        font2 = QFont()
        font2.setFamily(u"Rasa")
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(60, 86, 138);")
        self.horizontalLayoutWidget = QWidget(self.studio)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(170, 460, 191, 51))
        self.key_sig_box = QHBoxLayout(self.horizontalLayoutWidget)
        self.key_sig_box.setSpacing(0)
        self.key_sig_box.setObjectName(u"key_sig_box")
        self.key_sig_box.setContentsMargins(0, 0, 0, 0)
        self.keysig_label = QLabel(self.horizontalLayoutWidget)
        self.keysig_label.setObjectName(u"keysig_label")
        font3 = QFont()
        font3.setPointSize(9)
        self.keysig_label.setFont(font3)
        self.keysig_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.keysig_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.keysig_label.setMargin(6)

        self.key_sig_box.addWidget(self.keysig_label)

        self.keysig_spacer1 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.key_sig_box.addItem(self.keysig_spacer1)

        self.keysig_note = QComboBox(self.horizontalLayoutWidget)
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.setObjectName(u"keysig_note")
        self.keysig_note.setMinimumSize(QSize(46, 0))
        self.keysig_note.setMaximumSize(QSize(42, 16777215))
        font4 = QFont()
        font4.setPointSize(20)
        self.keysig_note.setFont(font4)
        self.keysig_note.setStyleSheet(u"QComboBox {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	background-color: rgb(16, 24, 24);\n"
"	color: rgb(137, 137, 206);\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"")

        self.key_sig_box.addWidget(self.keysig_note)

        self.keysig_acc = QPushButton(self.horizontalLayoutWidget)
        self.keysig_acc.setObjectName(u"keysig_acc")
        self.keysig_acc.setMinimumSize(QSize(0, 40))
        self.keysig_acc.setMaximumSize(QSize(26, 16777215))
        font5 = QFont()
        font5.setPointSize(16)
        self.keysig_acc.setFont(font5)
        self.keysig_acc.setStyleSheet(u"QPushButton {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	background-color: rgb(16, 24, 24);\n"
"	color: rgb(137, 137, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"")

        self.key_sig_box.addWidget(self.keysig_acc)

        self.verticalLayoutWidget_3 = QWidget(self.studio)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(180, 600, 511, 51))
        self.lh_range1_box = QVBoxLayout(self.verticalLayoutWidget_3)
        self.lh_range1_box.setObjectName(u"lh_range1_box")
        self.lh_range1_box.setContentsMargins(0, 0, 0, 0)
        self.lh_range1_note_display = QHBoxLayout()
        self.lh_range1_note_display.setObjectName(u"lh_range1_note_display")
        self.lh_range1_label = QLabel(self.verticalLayoutWidget_3)
        self.lh_range1_label.setObjectName(u"lh_range1_label")
        self.lh_range1_label.setFont(font3)
        self.lh_range1_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.lh_range1_note_display.addWidget(self.lh_range1_label)

        self.lh_range1_spacerr = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lh_range1_note_display.addItem(self.lh_range1_spacerr)


        self.lh_range1_box.addLayout(self.lh_range1_note_display)

        self.note_slider = QSlider(self.verticalLayoutWidget_3)
        self.note_slider.setObjectName(u"note_slider")
        self.note_slider.setMinimumSize(QSize(0, 0))
        self.note_slider.setLayoutDirection(Qt.LeftToRight)
        self.note_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.note_slider.setMaximum(87)
        self.note_slider.setPageStep(1)
        self.note_slider.setValue(2)
        self.note_slider.setTracking(True)
        self.note_slider.setOrientation(Qt.Horizontal)
        self.note_slider.setInvertedAppearance(False)
        self.note_slider.setTickPosition(QSlider.NoTicks)
        self.note_slider.setTickInterval(0)

        self.lh_range1_box.addWidget(self.note_slider)

        self.horizontalLayoutWidget_3 = QWidget(self.studio)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(170, 340, 171, 91))
        self.time_sig_box = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.time_sig_box.setObjectName(u"time_sig_box")
        self.time_sig_box.setContentsMargins(0, 0, 0, 0)
        self.time_sig_label = QLabel(self.horizontalLayoutWidget_3)
        self.time_sig_label.setObjectName(u"time_sig_label")
        self.time_sig_label.setFont(font3)
        self.time_sig_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.time_sig_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.time_sig_label.setMargin(6)

        self.time_sig_box.addWidget(self.time_sig_label)

        self.horizontalSpacer = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_sig_box.addItem(self.horizontalSpacer)

        self.time_sig = QVBoxLayout()
        self.time_sig.setObjectName(u"time_sig")
        self.timesig_num = QLineEdit(self.horizontalLayoutWidget_3)
        self.timesig_num.setObjectName(u"timesig_num")
        self.timesig_num.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setPointSize(11)
        self.timesig_num.setFont(font6)
        self.timesig_num.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(137, 137, 206);\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgb(24, 40, 40);\n"
"}")
        self.timesig_num.setAlignment(Qt.AlignCenter)

        self.time_sig.addWidget(self.timesig_num)

        self.timesig_line = QFrame(self.horizontalLayoutWidget_3)
        self.timesig_line.setObjectName(u"timesig_line")
        self.timesig_line.setMinimumSize(QSize(0, 10))
        self.timesig_line.setFont(font3)
        self.timesig_line.setLineWidth(4)
        self.timesig_line.setFrameShape(QFrame.HLine)
        self.timesig_line.setFrameShadow(QFrame.Sunken)

        self.time_sig.addWidget(self.timesig_line)

        self.timesig_den = QLineEdit(self.horizontalLayoutWidget_3)
        self.timesig_den.setObjectName(u"timesig_den")
        self.timesig_den.setMinimumSize(QSize(0, 30))
        self.timesig_den.setFont(font6)
        self.timesig_den.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(137, 137, 206);\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgb(24, 40, 40);\n"
"}")
        self.timesig_den.setAlignment(Qt.AlignCenter)

        self.time_sig.addWidget(self.timesig_den)


        self.time_sig_box.addLayout(self.time_sig)

        self.lh_range_label = QLabel(self.studio)
        self.lh_range_label.setObjectName(u"lh_range_label")
        self.lh_range_label.setGeometry(QRect(180, 560, 111, 26))
        self.lh_range_label.setFont(font3)
        self.lh_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.verticalLayoutWidget_4 = QWidget(self.studio)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(180, 650, 511, 51))
        self.lh_range2_box = QVBoxLayout(self.verticalLayoutWidget_4)
        self.lh_range2_box.setObjectName(u"lh_range2_box")
        self.lh_range2_box.setContentsMargins(0, 0, 0, 0)
        self.lh_range2_display = QHBoxLayout()
        self.lh_range2_display.setObjectName(u"lh_range2_display")
        self.lh_range2_label = QLabel(self.verticalLayoutWidget_4)
        self.lh_range2_label.setObjectName(u"lh_range2_label")
        self.lh_range2_label.setFont(font3)
        self.lh_range2_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.lh_range2_display.addWidget(self.lh_range2_label)

        self.lh_range2_spacerr = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lh_range2_display.addItem(self.lh_range2_spacerr)


        self.lh_range2_box.addLayout(self.lh_range2_display)

        self.lh_range2_slider = QSlider(self.verticalLayoutWidget_4)
        self.lh_range2_slider.setObjectName(u"lh_range2_slider")
        self.lh_range2_slider.setMinimumSize(QSize(0, 0))
        self.lh_range2_slider.setLayoutDirection(Qt.LeftToRight)
        self.lh_range2_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.lh_range2_slider.setMaximum(87)
        self.lh_range2_slider.setPageStep(1)
        self.lh_range2_slider.setValue(2)
        self.lh_range2_slider.setTracking(True)
        self.lh_range2_slider.setOrientation(Qt.Horizontal)
        self.lh_range2_slider.setInvertedAppearance(False)
        self.lh_range2_slider.setTickPosition(QSlider.NoTicks)
        self.lh_range2_slider.setTickInterval(0)

        self.lh_range2_box.addWidget(self.lh_range2_slider)

        self.verticalLayoutWidget_5 = QWidget(self.studio)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(800, 90, 511, 51))
        self.note_select_box_3 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.note_select_box_3.setObjectName(u"note_select_box_3")
        self.note_select_box_3.setContentsMargins(0, 0, 0, 0)
        self.note_display_3 = QHBoxLayout()
        self.note_display_3.setObjectName(u"note_display_3")
        self.note_l_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.note_display_3.addItem(self.note_l_spacer_3)

        self.note_label_3 = QLabel(self.verticalLayoutWidget_5)
        self.note_label_3.setObjectName(u"note_label_3")
        self.note_label_3.setFont(font3)
        self.note_label_3.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.note_display_3.addWidget(self.note_label_3)

        self.note_r_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.note_display_3.addItem(self.note_r_spacer_3)


        self.note_select_box_3.addLayout(self.note_display_3)

        self.note_slider_3 = QSlider(self.verticalLayoutWidget_5)
        self.note_slider_3.setObjectName(u"note_slider_3")
        self.note_slider_3.setMinimumSize(QSize(0, 0))
        self.note_slider_3.setLayoutDirection(Qt.LeftToRight)
        self.note_slider_3.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.note_slider_3.setMaximum(87)
        self.note_slider_3.setPageStep(1)
        self.note_slider_3.setValue(2)
        self.note_slider_3.setTracking(True)
        self.note_slider_3.setOrientation(Qt.Horizontal)
        self.note_slider_3.setInvertedAppearance(False)
        self.note_slider_3.setTickPosition(QSlider.NoTicks)
        self.note_slider_3.setTickInterval(0)

        self.note_select_box_3.addWidget(self.note_slider_3)

        self.lh_range1_header_label = QLabel(self.studio)
        self.lh_range1_header_label.setObjectName(u"lh_range1_header_label")
        self.lh_range1_header_label.setGeometry(QRect(330, 560, 29, 26))
        self.lh_range1_header_label.setFont(font3)
        self.lh_range1_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.lh_range2_header_label = QLabel(self.studio)
        self.lh_range2_header_label.setObjectName(u"lh_range2_header_label")
        self.lh_range2_header_label.setGeometry(QRect(390, 560, 29, 26))
        self.lh_range2_header_label.setFont(font3)
        self.lh_range2_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dash = QLabel(self.studio)
        self.dash.setObjectName(u"dash")
        self.dash.setGeometry(QRect(370, 560, 16, 26))
        self.dash.setFont(font3)
        self.dash.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.time_sig_label_5 = QLabel(self.studio)
        self.time_sig_label_5.setObjectName(u"time_sig_label_5")
        self.time_sig_label_5.setGeometry(QRect(1040, 240, 107, 41))
        self.time_sig_label_5.setFont(font3)
        self.time_sig_label_5.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.time_sig_label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.time_sig_label_5.setMargin(6)
        self.label = QLabel(self.studio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1120, 250, 57, 15))
        self.horizontalLayoutWidget_5 = QWidget(self.studio)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(910, 570, 331, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.keysig_rundown_label = QLabel(self.horizontalLayoutWidget_5)
        self.keysig_rundown_label.setObjectName(u"keysig_rundown_label")
        self.keysig_rundown_label.setFont(font3)
        self.keysig_rundown_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.keysig_rundown_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.keysig_rundown_label.setMargin(6)

        self.horizontalLayout.addWidget(self.keysig_rundown_label)

        self.keysig_rundown_value = QLabel(self.horizontalLayoutWidget_5)
        self.keysig_rundown_value.setObjectName(u"keysig_rundown_value")
        self.keysig_rundown_value.setFont(font3)
        self.keysig_rundown_value.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.keysig_rundown_value.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.keysig_rundown_value.setMargin(6)

        self.horizontalLayout.addWidget(self.keysig_rundown_value)

        self.horizontalLayoutWidget_6 = QWidget(self.studio)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(910, 540, 331, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.timesig_rundown_label = QLabel(self.horizontalLayoutWidget_6)
        self.timesig_rundown_label.setObjectName(u"timesig_rundown_label")
        self.timesig_rundown_label.setFont(font3)
        self.timesig_rundown_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.timesig_rundown_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.timesig_rundown_label.setMargin(6)

        self.horizontalLayout_2.addWidget(self.timesig_rundown_label)

        self.timesig_rundown_value = QLabel(self.horizontalLayoutWidget_6)
        self.timesig_rundown_value.setObjectName(u"timesig_rundown_value")
        self.timesig_rundown_value.setFont(font3)
        self.timesig_rundown_value.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.timesig_rundown_value.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.timesig_rundown_value.setMargin(6)

        self.horizontalLayout_2.addWidget(self.timesig_rundown_value)

        self.lineEdit.raise_()
        self.output_folder_entry.raise_()
        self.corner_logo.raise_()
        self.label_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.lh_range_label.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.lh_range1_header_label.raise_()
        self.dash.raise_()
        self.lh_range2_header_label.raise_()
        self.time_sig_label_5.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.archive = QFrame(self.centralwidget)
        self.archive.setObjectName(u"archive")
        self.archive.setGeometry(QRect(1280, 380, 1600, 900))
        self.archive.setFrameShape(QFrame.StyledPanel)
        self.archive.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.whitefur_photo.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Composer and professor Arthur &quot;Skip&quot; Whitefur has been composing masterpieces since his owner died in his sleep three days ago, and has quickly ascended the pinnacle of the art with now universally-acclaimed works such as <span style=\" font-style:italic;\">Crispy Does It </span>and <span style=\" font-style:italic;\">When I Shed</span>.<br/></p><p>Dr. Whitefur does not read his email, but you can usually find him working at the forge of his craft or in the bedroom sustaining himself on more of his owner's remains. And now let's finish with a few words from Dr Skip himself:<br/></p><p align=\"center\"><span style=\" font-style:italic;\">&quot;I hate other cats. They think they can eat my food, so I hiss and swat at them every time. I'll cut any of them who comes near my food&quot;</span></p><p align=\"center\">- Professor Arthur &quot;Skip&quot; Whitefur</p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title masterpiece...", None))
        self.output_folder_entry.setText("")
        self.output_folder_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"custom_filepath", None))
        self.corner_logo.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Professor Whitefur's Masterpiece Studio", None))
        self.keysig_label.setText(QCoreApplication.translate("MainWindow", u"Key Signature:", None))
        self.keysig_note.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.keysig_note.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.keysig_note.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.keysig_note.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.keysig_note.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.keysig_note.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.keysig_note.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.keysig_acc.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.lh_range1_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.time_sig_label.setText(QCoreApplication.translate("MainWindow", u"Time Signature:", None))
        self.timesig_num.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.timesig_num.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_num.setPlaceholderText("")
        self.timesig_den.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.timesig_den.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_den.setPlaceholderText("")
        self.lh_range_label.setText(QCoreApplication.translate("MainWindow", u"Left Hand Range:", None))
        self.lh_range2_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.note_label_3.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range1_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range2_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.time_sig_label_5.setText(QCoreApplication.translate("MainWindow", u"Rundown:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.keysig_rundown_label.setText(QCoreApplication.translate("MainWindow", u"Key Signature:", None))
        self.keysig_rundown_value.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.timesig_rundown_label.setText(QCoreApplication.translate("MainWindow", u"Time Signature:", None))
        self.timesig_rundown_value.setText(QCoreApplication.translate("MainWindow", u"4/4", None))
    # retranslateUi

