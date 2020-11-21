# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studioui.ui'
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
        self.studio = QFrame(self.centralwidget)
        self.studio.setObjectName(u"studio")
        self.studio.setGeometry(QRect(0, 0, 1600, 900))
        self.studio.setFrameShape(QFrame.StyledPanel)
        self.studio.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.studio)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 390, 191, 54))
        self.key_sig_box = QHBoxLayout(self.horizontalLayoutWidget)
        self.key_sig_box.setSpacing(0)
        self.key_sig_box.setObjectName(u"key_sig_box")
        self.key_sig_box.setContentsMargins(0, 0, 0, 0)
        self.keysig_label = QLabel(self.horizontalLayoutWidget)
        self.keysig_label.setObjectName(u"keysig_label")
        font = QFont()
        font.setPointSize(9)
        self.keysig_label.setFont(font)
        self.keysig_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.keysig_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.keysig_label.setMargin(6)

        self.key_sig_box.addWidget(self.keysig_label)

        self.keysig_spacer1 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.key_sig_box.addItem(self.keysig_spacer1)

        self.keysig_note = QPushButton(self.horizontalLayoutWidget)
        self.keysig_note.setObjectName(u"keysig_note")
        self.keysig_note.setMinimumSize(QSize(46, 37))
        self.keysig_note.setMaximumSize(QSize(26, 40))
        font1 = QFont()
        font1.setPointSize(20)
        self.keysig_note.setFont(font1)
        self.keysig_note.setStyleSheet(u"QPushButton {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	border-radius: 4px;\n"
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
"\n"
"}\n"
"")

        self.key_sig_box.addWidget(self.keysig_note)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.keysig_acc = QPushButton(self.horizontalLayoutWidget)
        self.keysig_acc.setObjectName(u"keysig_acc")
        self.keysig_acc.setMinimumSize(QSize(26, 24))
        self.keysig_acc.setMaximumSize(QSize(26, 40))
        font2 = QFont()
        font2.setPointSize(14)
        self.keysig_acc.setFont(font2)
        self.keysig_acc.setStyleSheet(u"QPushButton {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	border-radius: 4px;\n"
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
"}\n"
"")

        self.verticalLayout.addWidget(self.keysig_acc)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.key_sig_box.addLayout(self.verticalLayout)

        self.verticalLayoutWidget_3 = QWidget(self.studio)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(60, 550, 511, 51))
        self.lh_range1_box = QVBoxLayout(self.verticalLayoutWidget_3)
        self.lh_range1_box.setObjectName(u"lh_range1_box")
        self.lh_range1_box.setContentsMargins(0, 0, 0, 0)
        self.lh_range1_note_display = QHBoxLayout()
        self.lh_range1_note_display.setObjectName(u"lh_range1_note_display")
        self.lh_range1_label = QLabel(self.verticalLayoutWidget_3)
        self.lh_range1_label.setObjectName(u"lh_range1_label")
        self.lh_range1_label.setFont(font)
        self.lh_range1_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.lh_range1_note_display.addWidget(self.lh_range1_label)

        self.lh_range1_spacerr = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lh_range1_note_display.addItem(self.lh_range1_spacerr)


        self.lh_range1_box.addLayout(self.lh_range1_note_display)

        self.lh_range1_slider = QSlider(self.verticalLayoutWidget_3)
        self.lh_range1_slider.setObjectName(u"lh_range1_slider")
        self.lh_range1_slider.setMinimumSize(QSize(0, 0))
        self.lh_range1_slider.setLayoutDirection(Qt.LeftToRight)
        self.lh_range1_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.lh_range1_slider.setMaximum(87)
        self.lh_range1_slider.setPageStep(1)
        self.lh_range1_slider.setValue(2)
        self.lh_range1_slider.setTracking(True)
        self.lh_range1_slider.setOrientation(Qt.Horizontal)
        self.lh_range1_slider.setInvertedAppearance(False)
        self.lh_range1_slider.setTickPosition(QSlider.NoTicks)
        self.lh_range1_slider.setTickInterval(0)

        self.lh_range1_box.addWidget(self.lh_range1_slider)

        self.horizontalLayoutWidget_3 = QWidget(self.studio)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(50, 290, 171, 91))
        self.time_sig_box = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.time_sig_box.setObjectName(u"time_sig_box")
        self.time_sig_box.setContentsMargins(0, 0, 0, 0)
        self.time_sig_label = QLabel(self.horizontalLayoutWidget_3)
        self.time_sig_label.setObjectName(u"time_sig_label")
        self.time_sig_label.setFont(font)
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
        font3 = QFont()
        font3.setPointSize(11)
        self.timesig_num.setFont(font3)
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
        self.timesig_line.setFont(font)
        self.timesig_line.setLineWidth(4)
        self.timesig_line.setFrameShape(QFrame.HLine)
        self.timesig_line.setFrameShadow(QFrame.Sunken)

        self.time_sig.addWidget(self.timesig_line)

        self.timesig_den = QLineEdit(self.horizontalLayoutWidget_3)
        self.timesig_den.setObjectName(u"timesig_den")
        self.timesig_den.setMinimumSize(QSize(0, 30))
        self.timesig_den.setFont(font3)
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
        self.lh_range_label.setGeometry(QRect(70, 520, 71, 26))
        self.lh_range_label.setFont(font)
        self.lh_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.verticalLayoutWidget_4 = QWidget(self.studio)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(60, 600, 511, 51))
        self.lh_range2_box = QVBoxLayout(self.verticalLayoutWidget_4)
        self.lh_range2_box.setObjectName(u"lh_range2_box")
        self.lh_range2_box.setContentsMargins(0, 0, 0, 0)
        self.lh_range2_display = QHBoxLayout()
        self.lh_range2_display.setObjectName(u"lh_range2_display")
        self.lh_range2_label = QLabel(self.verticalLayoutWidget_4)
        self.lh_range2_label.setObjectName(u"lh_range2_label")
        self.lh_range2_label.setFont(font)
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

        self.lh_range1_header_label = QLabel(self.studio)
        self.lh_range1_header_label.setObjectName(u"lh_range1_header_label")
        self.lh_range1_header_label.setGeometry(QRect(260, 520, 29, 26))
        self.lh_range1_header_label.setFont(font)
        self.lh_range1_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.lh_range2_header_label = QLabel(self.studio)
        self.lh_range2_header_label.setObjectName(u"lh_range2_header_label")
        self.lh_range2_header_label.setGeometry(QRect(320, 520, 29, 26))
        self.lh_range2_header_label.setFont(font)
        self.lh_range2_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dash = QLabel(self.studio)
        self.dash.setObjectName(u"dash")
        self.dash.setGeometry(QRect(300, 520, 16, 26))
        self.dash.setFont(font)
        self.dash.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.new_name = QLineEdit(self.studio)
        self.new_name.setObjectName(u"new_name")
        self.new_name.setGeometry(QRect(180, 160, 293, 44))
        self.new_name.setMinimumSize(QSize(240, 44))
        font4 = QFont()
        font4.setFamily(u"Rasa")
        font4.setPointSize(14)
        self.new_name.setFont(font4)
        self.new_name.setStyleSheet(u"QLineEdit {\n"
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
        self.new_name.setCursorPosition(0)
        self.extended_filepath = QLineEdit(self.studio)
        self.extended_filepath.setObjectName(u"extended_filepath")
        self.extended_filepath.setGeometry(QRect(1060, 160, 281, 40))
        self.extended_filepath.setMinimumSize(QSize(240, 40))
        font5 = QFont()
        font5.setFamily(u"Rasa")
        font5.setPointSize(12)
        self.extended_filepath.setFont(font5)
        self.extended_filepath.setStyleSheet(u"QLineEdit {\n"
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
        self.extended_filepath.setCursorPosition(0)
        self.additional_fp_label = QLabel(self.studio)
        self.additional_fp_label.setObjectName(u"additional_fp_label")
        self.additional_fp_label.setGeometry(QRect(1060, 120, 131, 30))
        self.additional_fp_label.setMaximumSize(QSize(16777215, 30))
        self.additional_fp_label.setFont(font)
        self.additional_fp_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.additional_fp_label.setAlignment(Qt.AlignCenter)
        self.additional_fp_label.setMargin(6)
        self.prompt = QLabel(self.studio)
        self.prompt.setObjectName(u"prompt")
        self.prompt.setGeometry(QRect(130, 60, 171, 61))
        self.prompt.setFont(font)
        self.prompt.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.prompt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.prompt.setWordWrap(True)
        self.prompt.setMargin(6)
        self.prompt_2 = QLabel(self.studio)
        self.prompt_2.setObjectName(u"prompt_2")
        self.prompt_2.setGeometry(QRect(130, 0, 261, 51))
        font6 = QFont()
        font6.setPointSize(28)
        self.prompt_2.setFont(font6)
        self.prompt_2.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.prompt_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.prompt_2.setWordWrap(True)
        self.prompt_2.setMargin(6)
        self.timesig_line_2 = QFrame(self.studio)
        self.timesig_line_2.setObjectName(u"timesig_line_2")
        self.timesig_line_2.setGeometry(QRect(130, 48, 291, 16))
        self.timesig_line_2.setMinimumSize(QSize(0, 10))
        self.timesig_line_2.setFont(font)
        self.timesig_line_2.setLineWidth(4)
        self.timesig_line_2.setFrameShape(QFrame.HLine)
        self.timesig_line_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_2 = QWidget(self.studio)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 240, 231, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.length_label = QLabel(self.horizontalLayoutWidget_2)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setMinimumSize(QSize(140, 0))
        self.length_label.setMaximumSize(QSize(120, 30))
        self.length_label.setFont(font)
        self.length_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.length_label.setWordWrap(True)
        self.length_label.setMargin(6)

        self.horizontalLayout_3.addWidget(self.length_label)

        self.measure_count = QLineEdit(self.horizontalLayoutWidget_2)
        self.measure_count.setObjectName(u"measure_count")
        self.measure_count.setMinimumSize(QSize(0, 30))
        self.measure_count.setMaximumSize(QSize(60, 16777215))
        self.measure_count.setFont(font3)
        self.measure_count.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(137, 137, 206);\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgb(24, 40, 40);\n"
"}")
        self.measure_count.setMaxLength(3)
        self.measure_count.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.measure_count)

        self.output_tree = QTreeView(self.studio)
        self.output_tree.setObjectName(u"output_tree")
        self.output_tree.setGeometry(QRect(910, 230, 431, 281))
        self.output_tree.setStyleSheet(u"QTreeView {\n"
"	color: rgb(137, 137, 206);\n"
"	background-color: rgb(25, 40, 40);\n"
"}")
        self.rh_range_label = QLabel(self.studio)
        self.rh_range_label.setObjectName(u"rh_range_label")
        self.rh_range_label.setGeometry(QRect(70, 670, 121, 26))
        self.rh_range_label.setFont(font)
        self.rh_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_range2_header_label = QLabel(self.studio)
        self.rh_range2_header_label.setObjectName(u"rh_range2_header_label")
        self.rh_range2_header_label.setGeometry(QRect(320, 670, 29, 26))
        self.rh_range2_header_label.setFont(font)
        self.rh_range2_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_range1_header_label = QLabel(self.studio)
        self.rh_range1_header_label.setObjectName(u"rh_range1_header_label")
        self.rh_range1_header_label.setGeometry(QRect(260, 670, 29, 26))
        self.rh_range1_header_label.setFont(font)
        self.rh_range1_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.verticalLayoutWidget_6 = QWidget(self.studio)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(60, 750, 511, 51))
        self.rh_range2_box = QVBoxLayout(self.verticalLayoutWidget_6)
        self.rh_range2_box.setObjectName(u"rh_range2_box")
        self.rh_range2_box.setContentsMargins(0, 0, 0, 0)
        self.rh_range2_display = QHBoxLayout()
        self.rh_range2_display.setObjectName(u"rh_range2_display")
        self.rh_range2_label = QLabel(self.verticalLayoutWidget_6)
        self.rh_range2_label.setObjectName(u"rh_range2_label")
        self.rh_range2_label.setFont(font)
        self.rh_range2_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.rh_range2_display.addWidget(self.rh_range2_label)

        self.rh_range2_spacerr = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rh_range2_display.addItem(self.rh_range2_spacerr)


        self.rh_range2_box.addLayout(self.rh_range2_display)

        self.rh_range2_slider = QSlider(self.verticalLayoutWidget_6)
        self.rh_range2_slider.setObjectName(u"rh_range2_slider")
        self.rh_range2_slider.setMinimumSize(QSize(0, 0))
        self.rh_range2_slider.setLayoutDirection(Qt.LeftToRight)
        self.rh_range2_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.rh_range2_slider.setMaximum(87)
        self.rh_range2_slider.setPageStep(1)
        self.rh_range2_slider.setValue(2)
        self.rh_range2_slider.setTracking(True)
        self.rh_range2_slider.setOrientation(Qt.Horizontal)
        self.rh_range2_slider.setInvertedAppearance(False)
        self.rh_range2_slider.setTickPosition(QSlider.NoTicks)
        self.rh_range2_slider.setTickInterval(0)

        self.rh_range2_box.addWidget(self.rh_range2_slider)

        self.verticalLayoutWidget_7 = QWidget(self.studio)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(60, 700, 511, 51))
        self.rh_range1_box = QVBoxLayout(self.verticalLayoutWidget_7)
        self.rh_range1_box.setObjectName(u"rh_range1_box")
        self.rh_range1_box.setContentsMargins(0, 0, 0, 0)
        self.rh_range1_note_display = QHBoxLayout()
        self.rh_range1_note_display.setObjectName(u"rh_range1_note_display")
        self.rh_range1_label = QLabel(self.verticalLayoutWidget_7)
        self.rh_range1_label.setObjectName(u"rh_range1_label")
        self.rh_range1_label.setFont(font)
        self.rh_range1_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.rh_range1_note_display.addWidget(self.rh_range1_label)

        self.rh_range1_spacerr = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rh_range1_note_display.addItem(self.rh_range1_spacerr)


        self.rh_range1_box.addLayout(self.rh_range1_note_display)

        self.rh_range1_slider = QSlider(self.verticalLayoutWidget_7)
        self.rh_range1_slider.setObjectName(u"rh_range1_slider")
        self.rh_range1_slider.setMinimumSize(QSize(0, 0))
        self.rh_range1_slider.setLayoutDirection(Qt.LeftToRight)
        self.rh_range1_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.rh_range1_slider.setMaximum(87)
        self.rh_range1_slider.setPageStep(1)
        self.rh_range1_slider.setValue(2)
        self.rh_range1_slider.setTracking(True)
        self.rh_range1_slider.setOrientation(Qt.Horizontal)
        self.rh_range1_slider.setInvertedAppearance(False)
        self.rh_range1_slider.setTickPosition(QSlider.NoTicks)
        self.rh_range1_slider.setTickInterval(0)

        self.rh_range1_box.addWidget(self.rh_range1_slider)

        self.dash_2 = QLabel(self.studio)
        self.dash_2.setObjectName(u"dash_2")
        self.dash_2.setGeometry(QRect(300, 670, 16, 26))
        self.dash_2.setFont(font)
        self.dash_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.output_label = QLabel(self.studio)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(900, 200, 71, 30))
        self.output_label.setMinimumSize(QSize(60, 0))
        self.output_label.setMaximumSize(QSize(120, 30))
        self.output_label.setFont(font)
        self.output_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.output_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.output_label.setWordWrap(True)
        self.output_label.setMargin(6)
        self.save_as = QLabel(self.studio)
        self.save_as.setObjectName(u"save_as")
        self.save_as.setGeometry(QRect(910, 520, 241, 30))
        self.save_as.setMaximumSize(QSize(16777215, 30))
        self.save_as.setFont(font)
        self.save_as.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.save_as.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.save_as.setMargin(6)
        self.name_label_1 = QLabel(self.studio)
        self.name_label_1.setObjectName(u"name_label_1")
        self.name_label_1.setGeometry(QRect(860, 150, 171, 30))
        self.name_label_1.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setPointSize(12)
        self.name_label_1.setFont(font7)
        self.name_label_1.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.name_label_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_label_1.setMargin(6)
        self.writing = QLabel(self.studio)
        self.writing.setObjectName(u"writing")
        self.writing.setGeometry(QRect(780, 150, 81, 30))
        self.writing.setMaximumSize(QSize(16777215, 30))
        self.writing.setFont(font7)
        self.writing.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.writing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.writing.setMargin(6)
        self.horizontalLayoutWidget_4 = QWidget(self.studio)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(150, 460, 73, 51))
        self.ranges_mode = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.ranges_mode.setSpacing(2)
        self.ranges_mode.setObjectName(u"ranges_mode")
        self.ranges_mode.setContentsMargins(0, 0, 0, 0)
        self.sharp_ranges = QPushButton(self.horizontalLayoutWidget_4)
        self.sharp_ranges.setObjectName(u"sharp_ranges")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sharp_ranges.sizePolicy().hasHeightForWidth())
        self.sharp_ranges.setSizePolicy(sizePolicy)
        self.sharp_ranges.setMaximumSize(QSize(16777215, 25))
        self.sharp_ranges.setFont(font2)
        self.sharp_ranges.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(25, 40, 40);\n"
"	background-color: rgb(67, 67, 100);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(80, 80, 126);\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(18, 30, 30);\n"
"}")

        self.ranges_mode.addWidget(self.sharp_ranges)

        self.flat_ranges = QPushButton(self.horizontalLayoutWidget_4)
        self.flat_ranges.setObjectName(u"flat_ranges")
        sizePolicy.setHeightForWidth(self.flat_ranges.sizePolicy().hasHeightForWidth())
        self.flat_ranges.setSizePolicy(sizePolicy)
        self.flat_ranges.setMaximumSize(QSize(16777215, 25))
        self.flat_ranges.setFont(font2)
        self.flat_ranges.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(25, 40, 40);\n"
"	background-color: rgb(67, 67, 100);\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(80, 80, 126);\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(18, 30, 30);\n"
"}")

        self.ranges_mode.addWidget(self.flat_ranges)

        self.ranges_label = QLabel(self.studio)
        self.ranges_label.setObjectName(u"ranges_label")
        self.ranges_label.setGeometry(QRect(70, 470, 51, 26))
        self.ranges_label.setFont(font)
        self.ranges_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.lh_span = QLabel(self.studio)
        self.lh_span.setObjectName(u"lh_span")
        self.lh_span.setGeometry(QRect(470, 520, 81, 26))
        self.lh_span.setFont(font)
        self.lh_span.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_span = QLabel(self.studio)
        self.rh_span.setObjectName(u"rh_span")
        self.rh_span.setGeometry(QRect(470, 670, 81, 26))
        self.rh_span.setFont(font)
        self.rh_span.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.length_label_3 = QLabel(self.studio)
        self.length_label_3.setObjectName(u"length_label_3")
        self.length_label_3.setGeometry(QRect(400, 520, 60, 30))
        self.length_label_3.setMinimumSize(QSize(60, 0))
        self.length_label_3.setMaximumSize(QSize(120, 30))
        self.length_label_3.setFont(font)
        self.length_label_3.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label_3.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.length_label_3.setWordWrap(True)
        self.length_label_3.setMargin(6)
        self.length_label_4 = QLabel(self.studio)
        self.length_label_4.setObjectName(u"length_label_4")
        self.length_label_4.setGeometry(QRect(400, 670, 60, 30))
        self.length_label_4.setMinimumSize(QSize(60, 0))
        self.length_label_4.setMaximumSize(QSize(120, 30))
        self.length_label_4.setFont(font)
        self.length_label_4.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label_4.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.length_label_4.setWordWrap(True)
        self.length_label_4.setMargin(6)
        self.corner_logo = QPushButton(self.studio)
        self.corner_logo.setObjectName(u"corner_logo")
        self.corner_logo.setGeometry(QRect(0, 0, 100, 100))
        icon = QIcon()
        icon.addFile(u"data/images/avante-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.corner_logo.setIcon(icon)
        self.corner_logo.setIconSize(QSize(100, 100))
        self.keysig_scale = QPushButton(self.studio)
        self.keysig_scale.setObjectName(u"keysig_scale")
        self.keysig_scale.setGeometry(QRect(230, 420, 120, 21))
        self.keysig_scale.setMinimumSize(QSize(120, 20))
        self.keysig_scale.setMaximumSize(QSize(26, 30))
        self.keysig_scale.setFont(font2)
        self.keysig_scale.setStyleSheet(u"QPushButton {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	border-radius: 4px;\n"
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
"}\n"
"")
        self.keyboard_cat = QFrame(self.studio)
        self.keyboard_cat.setObjectName(u"keyboard_cat")
        self.keyboard_cat.setGeometry(QRect(0, 0, 1600, 900))
        self.keyboard_cat.setFrameShape(QFrame.StyledPanel)
        self.keyboard_cat.setFrameShadow(QFrame.Raised)
        self.keyboard_cat_label_2 = QLabel(self.keyboard_cat)
        self.keyboard_cat_label_2.setObjectName(u"keyboard_cat_label_2")
        self.keyboard_cat_label_2.setEnabled(True)
        self.keyboard_cat_label_2.setGeometry(QRect(0, 0, 1600, 900))
        self.keyboard_cat_label_2.setPixmap(QPixmap(u"data/images/keyboard-cat.png"))
        self.keyboard_cat_label_2.setScaledContents(True)
        self.compose = QPushButton(self.studio)
        self.compose.setObjectName(u"compose")
        self.compose.setGeometry(QRect(910, 680, 400, 40))
        self.compose.setMinimumSize(QSize(0, 40))
        self.compose.setMaximumSize(QSize(400, 16777215))
        self.compose.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")
        self.cats = QCheckBox(self.studio)
        self.cats.setObjectName(u"cats")
        self.cats.setGeometry(QRect(910, 640, 121, 31))
        self.cats.setStyleSheet(u"QCheckBox {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")
        self.pdf = QCheckBox(self.studio)
        self.pdf.setObjectName(u"pdf")
        self.pdf.setGeometry(QRect(910, 560, 111, 31))
        self.pdf.setStyleSheet(u"QCheckBox {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")
        self.pdf.setCheckable(True)
        self.pdf.setChecked(True)
        self.midi = QCheckBox(self.studio)
        self.midi.setObjectName(u"midi")
        self.midi.setGeometry(QRect(910, 600, 111, 31))
        self.midi.setStyleSheet(u"QCheckBox {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")
        self.midi.setChecked(True)
        self.keyboard_cat.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.lh_range_label.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.lh_range1_header_label.raise_()
        self.dash.raise_()
        self.lh_range2_header_label.raise_()
        self.new_name.raise_()
        self.extended_filepath.raise_()
        self.additional_fp_label.raise_()
        self.prompt.raise_()
        self.prompt_2.raise_()
        self.timesig_line_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.output_tree.raise_()
        self.rh_range_label.raise_()
        self.rh_range2_header_label.raise_()
        self.rh_range1_header_label.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.dash_2.raise_()
        self.output_label.raise_()
        self.save_as.raise_()
        self.name_label_1.raise_()
        self.writing.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.ranges_label.raise_()
        self.lh_span.raise_()
        self.rh_span.raise_()
        self.length_label_3.raise_()
        self.length_label_4.raise_()
        self.corner_logo.raise_()
        self.keysig_scale.raise_()
        self.compose.raise_()
        self.cats.raise_()
        self.pdf.raise_()
        self.midi.raise_()
        self.meet_the_composer = QFrame(self.centralwidget)
        self.meet_the_composer.setObjectName(u"meet_the_composer")
        self.meet_the_composer.setGeometry(QRect(0, 0, 1600, 900))
        self.meet_the_composer.setFrameShape(QFrame.StyledPanel)
        self.meet_the_composer.setFrameShadow(QFrame.Raised)
        self.whitefur_photo = QLabel(self.meet_the_composer)
        self.whitefur_photo.setObjectName(u"whitefur_photo")
        self.whitefur_photo.setGeometry(QRect(10, 100, 1000, 800))
        self.whitefur_photo.setPixmap(QPixmap(u"data/images/composer.png"))
        self.label_3 = QLabel(self.meet_the_composer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1080, 100, 401, 401))
        self.label_3.setFont(font7)
        self.label_3.setStyleSheet(u"QFrame {\n"
"	color: rgb(137, 137, 206);\n"
"}")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.corner_logo_2 = QPushButton(self.meet_the_composer)
        self.corner_logo_2.setObjectName(u"corner_logo_2")
        self.corner_logo_2.setGeometry(QRect(0, 0, 100, 100))
        self.corner_logo_2.setIcon(icon)
        self.corner_logo_2.setIconSize(QSize(100, 100))
        self.prompt_4 = QLabel(self.meet_the_composer)
        self.prompt_4.setObjectName(u"prompt_4")
        self.prompt_4.setGeometry(QRect(130, 60, 261, 31))
        self.prompt_4.setFont(font)
        self.prompt_4.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.prompt_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.prompt_4.setWordWrap(True)
        self.prompt_4.setMargin(6)
        self.timesig_line_3 = QFrame(self.meet_the_composer)
        self.timesig_line_3.setObjectName(u"timesig_line_3")
        self.timesig_line_3.setGeometry(QRect(130, 48, 291, 16))
        self.timesig_line_3.setMinimumSize(QSize(0, 10))
        self.timesig_line_3.setFont(font)
        self.timesig_line_3.setLineWidth(4)
        self.timesig_line_3.setFrameShape(QFrame.HLine)
        self.timesig_line_3.setFrameShadow(QFrame.Sunken)
        self.prompt_3 = QLabel(self.meet_the_composer)
        self.prompt_3.setObjectName(u"prompt_3")
        self.prompt_3.setGeometry(QRect(130, 0, 381, 51))
        self.prompt_3.setFont(font6)
        self.prompt_3.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.prompt_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.prompt_3.setWordWrap(True)
        self.prompt_3.setMargin(6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.meet_the_composer.raise_()
        self.studio.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.keysig_label.setText(QCoreApplication.translate("MainWindow", u"Key Signature:", None))
        self.keysig_note.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.keysig_acc.setText(QCoreApplication.translate("MainWindow", u"\u266e", None))
        self.lh_range1_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.time_sig_label.setText(QCoreApplication.translate("MainWindow", u"Time Signature:", None))
        self.timesig_num.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.timesig_num.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_num.setPlaceholderText("")
        self.timesig_den.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.timesig_den.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_den.setPlaceholderText("")
        self.lh_range_label.setText(QCoreApplication.translate("MainWindow", u"Left:", None))
        self.lh_range2_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range1_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range2_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.new_name.setText("")
        self.new_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name a new piece", None))
        self.extended_filepath.setText("")
        self.extended_filepath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/output/", None))
        self.additional_fp_label.setText(QCoreApplication.translate("MainWindow", u"Extended Filepath", None))
        self.prompt.setText(QCoreApplication.translate("MainWindow", u"Professor Whitefur can do many things, just tell him what you need", None))
        self.prompt_2.setText(QCoreApplication.translate("MainWindow", u"The Studio", None))
        self.length_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Length in measures:</p><p><br/></p></body></html>", None))
        self.measure_count.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.measure_count.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.measure_count.setPlaceholderText("")
        self.rh_range_label.setText(QCoreApplication.translate("MainWindow", u"Right:", None))
        self.rh_range2_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.rh_range1_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.rh_range2_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.rh_range1_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/output/</p></body></html>", None))
        self.save_as.setText(QCoreApplication.translate("MainWindow", u"filepath/filename", None))
        self.name_label_1.setText(QCoreApplication.translate("MainWindow", u"new name", None))
        self.writing.setText(QCoreApplication.translate("MainWindow", u"Writing", None))
        self.sharp_ranges.setText(QCoreApplication.translate("MainWindow", u"\u266f", None))
        self.flat_ranges.setText(QCoreApplication.translate("MainWindow", u"\u266d", None))
        self.ranges_label.setText(QCoreApplication.translate("MainWindow", u"Ranges", None))
        self.lh_span.setText(QCoreApplication.translate("MainWindow", u"steps", None))
        self.rh_span.setText(QCoreApplication.translate("MainWindow", u"steps", None))
        self.length_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Span:</p></body></html>", None))
        self.length_label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Span:</p></body></html>", None))
        self.corner_logo.setText("")
        self.keysig_scale.setText(QCoreApplication.translate("MainWindow", u"major", None))
        self.keyboard_cat_label_2.setText("")
        self.compose.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.cats.setText(QCoreApplication.translate("MainWindow", u"cats", None))
        self.pdf.setText(QCoreApplication.translate("MainWindow", u".pdf", None))
        self.midi.setText(QCoreApplication.translate("MainWindow", u".midi", None))
        self.whitefur_photo.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Composer and professor Arthur &quot;Skip&quot; Whitefur has been composing masterpieces since his owner died in his sleep three days ago, and has quickly ascended the pinnacle of the art with now universally-acclaimed works such as <span style=\" font-style:italic;\">Crispy Does It </span>and <span style=\" font-style:italic;\">When I Shed</span>.<br/></p><p>Dr. Whitefur does not read his email, but you can usually find him working at the forge of his craft or in the bedroom sustaining himself on more of his owner's remains. And now let's finish with a few words from Dr Skip himself:<br/></p><p align=\"center\"><span style=\" font-style:italic;\">&quot;I hate other cats. They think they can eat my food, so I hiss and swat at them every time. I'll cut any of them who comes near my food&quot;</span></p><p align=\"center\">- Professor Arthur &quot;Skip&quot; Whitefur</p></body></html>", None))
        self.corner_logo_2.setText("")
        self.prompt_4.setText(QCoreApplication.translate("MainWindow", u"It's a cat", None))
        self.prompt_3.setText(QCoreApplication.translate("MainWindow", u"Meet the Composer", None))
    # retranslateUi

