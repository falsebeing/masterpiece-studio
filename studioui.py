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
        MainWindow.resize(1589, 900)
        MainWindow.setStyleSheet(u"background-color:rgb(16, 24, 24);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.configure = QFrame(self.centralwidget)
        self.configure.setObjectName(u"configure")
        self.configure.setGeometry(QRect(0, 80, 1600, 820))
        self.configure.setFrameShape(QFrame.StyledPanel)
        self.configure.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.configure)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(60, 550, 511, 51))
        self.lh_range1_box = QVBoxLayout(self.verticalLayoutWidget_3)
        self.lh_range1_box.setObjectName(u"lh_range1_box")
        self.lh_range1_box.setContentsMargins(0, 0, 0, 0)
        self.lh_range1_note_display = QHBoxLayout()
        self.lh_range1_note_display.setObjectName(u"lh_range1_note_display")
        self.lh_range1_label = QLabel(self.verticalLayoutWidget_3)
        self.lh_range1_label.setObjectName(u"lh_range1_label")
        font = QFont()
        font.setPointSize(9)
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

        self.lh_range_label = QLabel(self.configure)
        self.lh_range_label.setObjectName(u"lh_range_label")
        self.lh_range_label.setGeometry(QRect(70, 520, 71, 26))
        self.lh_range_label.setFont(font)
        self.lh_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.verticalLayoutWidget_4 = QWidget(self.configure)
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

        self.lh_range1_header_label = QLabel(self.configure)
        self.lh_range1_header_label.setObjectName(u"lh_range1_header_label")
        self.lh_range1_header_label.setGeometry(QRect(260, 520, 29, 26))
        self.lh_range1_header_label.setFont(font)
        self.lh_range1_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.lh_range2_header_label = QLabel(self.configure)
        self.lh_range2_header_label.setObjectName(u"lh_range2_header_label")
        self.lh_range2_header_label.setGeometry(QRect(320, 520, 29, 26))
        self.lh_range2_header_label.setFont(font)
        self.lh_range2_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dash = QLabel(self.configure)
        self.dash.setObjectName(u"dash")
        self.dash.setGeometry(QRect(300, 520, 16, 26))
        self.dash.setFont(font)
        self.dash.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_range_label = QLabel(self.configure)
        self.rh_range_label.setObjectName(u"rh_range_label")
        self.rh_range_label.setGeometry(QRect(70, 670, 121, 26))
        self.rh_range_label.setFont(font)
        self.rh_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_range2_header_label = QLabel(self.configure)
        self.rh_range2_header_label.setObjectName(u"rh_range2_header_label")
        self.rh_range2_header_label.setGeometry(QRect(320, 670, 29, 26))
        self.rh_range2_header_label.setFont(font)
        self.rh_range2_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_range1_header_label = QLabel(self.configure)
        self.rh_range1_header_label.setObjectName(u"rh_range1_header_label")
        self.rh_range1_header_label.setGeometry(QRect(260, 670, 29, 26))
        self.rh_range1_header_label.setFont(font)
        self.rh_range1_header_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.verticalLayoutWidget_6 = QWidget(self.configure)
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

        self.verticalLayoutWidget_7 = QWidget(self.configure)
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

        self.dash_2 = QLabel(self.configure)
        self.dash_2.setObjectName(u"dash_2")
        self.dash_2.setGeometry(QRect(300, 670, 16, 26))
        self.dash_2.setFont(font)
        self.dash_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.horizontalLayoutWidget_4 = QWidget(self.configure)
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
        font1 = QFont()
        font1.setPointSize(14)
        self.sharp_ranges.setFont(font1)
        self.sharp_ranges.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"}\n"
"\n"
"\n"
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
        self.sharp_ranges.setCheckable(True)

        self.ranges_mode.addWidget(self.sharp_ranges)

        self.flat_ranges = QPushButton(self.horizontalLayoutWidget_4)
        self.flat_ranges.setObjectName(u"flat_ranges")
        sizePolicy.setHeightForWidth(self.flat_ranges.sizePolicy().hasHeightForWidth())
        self.flat_ranges.setSizePolicy(sizePolicy)
        self.flat_ranges.setMaximumSize(QSize(16777215, 25))
        self.flat_ranges.setFont(font1)
        self.flat_ranges.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"}\n"
"\n"
"\n"
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
        self.flat_ranges.setCheckable(True)

        self.ranges_mode.addWidget(self.flat_ranges)

        self.ranges_label = QLabel(self.configure)
        self.ranges_label.setObjectName(u"ranges_label")
        self.ranges_label.setGeometry(QRect(70, 470, 51, 26))
        self.ranges_label.setFont(font)
        self.ranges_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.lh_span = QLabel(self.configure)
        self.lh_span.setObjectName(u"lh_span")
        self.lh_span.setGeometry(QRect(470, 520, 81, 26))
        self.lh_span.setFont(font)
        self.lh_span.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.rh_span = QLabel(self.configure)
        self.rh_span.setObjectName(u"rh_span")
        self.rh_span.setGeometry(QRect(470, 670, 81, 26))
        self.rh_span.setFont(font)
        self.rh_span.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.length_label_3 = QLabel(self.configure)
        self.length_label_3.setObjectName(u"length_label_3")
        self.length_label_3.setGeometry(QRect(400, 520, 60, 30))
        self.length_label_3.setMinimumSize(QSize(60, 0))
        self.length_label_3.setMaximumSize(QSize(120, 30))
        self.length_label_3.setFont(font)
        self.length_label_3.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label_3.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.length_label_3.setWordWrap(True)
        self.length_label_3.setMargin(6)
        self.length_label_4 = QLabel(self.configure)
        self.length_label_4.setObjectName(u"length_label_4")
        self.length_label_4.setGeometry(QRect(400, 670, 60, 30))
        self.length_label_4.setMinimumSize(QSize(60, 0))
        self.length_label_4.setMaximumSize(QSize(120, 30))
        self.length_label_4.setFont(font)
        self.length_label_4.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label_4.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.length_label_4.setWordWrap(True)
        self.length_label_4.setMargin(6)
        self.keyboard_cat = QFrame(self.configure)
        self.keyboard_cat.setObjectName(u"keyboard_cat")
        self.keyboard_cat.setGeometry(QRect(1600, 0, 1600, 900))
        self.keyboard_cat.setFrameShape(QFrame.StyledPanel)
        self.keyboard_cat.setFrameShadow(QFrame.Raised)
        self.keyboard_cat_label_2 = QLabel(self.keyboard_cat)
        self.keyboard_cat_label_2.setObjectName(u"keyboard_cat_label_2")
        self.keyboard_cat_label_2.setEnabled(True)
        self.keyboard_cat_label_2.setGeometry(QRect(0, 0, 1600, 900))
        self.keyboard_cat_label_2.setPixmap(QPixmap(u"data/images/keyboard-cat.png"))
        self.keyboard_cat_label_2.setScaledContents(True)
        self.quarter_note_weight = QWidget(self.configure)
        self.quarter_note_weight.setObjectName(u"quarter_note_weight")
        self.quarter_note_weight.setGeometry(QRect(570, 180, 251, 61))
        self.lh_range2_header_label_2 = QLabel(self.quarter_note_weight)
        self.lh_range2_header_label_2.setObjectName(u"lh_range2_header_label_2")
        self.lh_range2_header_label_2.setGeometry(QRect(0, 0, 40, 51))
        self.lh_range2_header_label_2.setFont(font)
        self.lh_range2_header_label_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.lh_range2_header_label_2.setWordWrap(True)
        self.lh_range2_header_label_3 = QLabel(self.quarter_note_weight)
        self.lh_range2_header_label_3.setObjectName(u"lh_range2_header_label_3")
        self.lh_range2_header_label_3.setGeometry(QRect(60, 10, 61, 26))
        self.lh_range2_header_label_3.setFont(font)
        self.lh_range2_header_label_3.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.horizontalSlider = QSlider(self.quarter_note_weight)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(40, 40, 211, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.half_weight_widget = QWidget(self.configure)
        self.half_weight_widget.setObjectName(u"half_weight_widget")
        self.half_weight_widget.setGeometry(QRect(570, 120, 251, 61))
        self.half_weight_label = QLabel(self.half_weight_widget)
        self.half_weight_label.setObjectName(u"half_weight_label")
        self.half_weight_label.setGeometry(QRect(0, 0, 40, 51))
        self.half_weight_label.setFont(font)
        self.half_weight_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.half_weight_label.setWordWrap(True)
        self.half_weight_value = QLabel(self.half_weight_widget)
        self.half_weight_value.setObjectName(u"half_weight_value")
        self.half_weight_value.setGeometry(QRect(60, 10, 61, 22))
        self.half_weight_value.setFont(font)
        self.half_weight_value.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.half_weight_slider = QSlider(self.half_weight_widget)
        self.half_weight_slider.setObjectName(u"half_weight_slider")
        self.half_weight_slider.setGeometry(QRect(40, 40, 211, 16))
        self.half_weight_slider.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.configure)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(270, 20, 101, 61))
        self.save_load = QVBoxLayout(self.verticalLayoutWidget)
        self.save_load.setSpacing(2)
        self.save_load.setObjectName(u"save_load")
        self.save_load.setContentsMargins(0, 0, 0, 0)
        self.save = QPushButton(self.verticalLayoutWidget)
        self.save.setObjectName(u"save")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy1)
        self.save.setMinimumSize(QSize(0, 0))
        self.save.setMaximumSize(QSize(400, 16777215))
        self.save.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"\n"
"}\n"
"")

        self.save_load.addWidget(self.save)

        self.load = QPushButton(self.verticalLayoutWidget)
        self.load.setObjectName(u"load")
        sizePolicy1.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy1)
        self.load.setMinimumSize(QSize(0, 0))
        self.load.setMaximumSize(QSize(400, 16777215))
        self.load.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"\n"
"}\n"
"")

        self.save_load.addWidget(self.load)

        self.widget = QWidget(self.configure)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(210, 160, 28, 71))
        self.time_sig = QVBoxLayout(self.widget)
        self.time_sig.setSpacing(0)
        self.time_sig.setObjectName(u"time_sig")
        self.time_sig.setContentsMargins(0, 0, 0, 0)
        self.timesig_num = QLineEdit(self.widget)
        self.timesig_num.setObjectName(u"timesig_num")
        self.timesig_num.setMinimumSize(QSize(0, 26))
        self.timesig_num.setFont(font)
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

        self.timesig_line = QFrame(self.widget)
        self.timesig_line.setObjectName(u"timesig_line")
        self.timesig_line.setMinimumSize(QSize(0, 10))
        self.timesig_line.setFont(font)
        self.timesig_line.setFrameShadow(QFrame.Plain)
        self.timesig_line.setLineWidth(2)
        self.timesig_line.setFrameShape(QFrame.HLine)

        self.time_sig.addWidget(self.timesig_line)

        self.timesig_den = QLineEdit(self.widget)
        self.timesig_den.setObjectName(u"timesig_den")
        self.timesig_den.setMinimumSize(QSize(0, 26))
        self.timesig_den.setFont(font)
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

        self.time_sig_label = QLabel(self.configure)
        self.time_sig_label.setObjectName(u"time_sig_label")
        self.time_sig_label.setGeometry(QRect(50, 180, 140, 27))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.time_sig_label.sizePolicy().hasHeightForWidth())
        self.time_sig_label.setSizePolicy(sizePolicy2)
        self.time_sig_label.setMinimumSize(QSize(140, 0))
        self.time_sig_label.setMaximumSize(QSize(140, 16777215))
        self.time_sig_label.setFont(font)
        self.time_sig_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.time_sig_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.time_sig_label.setMargin(6)
        self.length_label = QLabel(self.configure)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setGeometry(QRect(50, 130, 140, 30))
        sizePolicy2.setHeightForWidth(self.length_label.sizePolicy().hasHeightForWidth())
        self.length_label.setSizePolicy(sizePolicy2)
        self.length_label.setMinimumSize(QSize(140, 0))
        self.length_label.setMaximumSize(QSize(140, 30))
        self.length_label.setFont(font)
        self.length_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.length_label.setWordWrap(True)
        self.length_label.setMargin(6)
        self.measures = QLineEdit(self.configure)
        self.measures.setObjectName(u"measures")
        self.measures.setGeometry(QRect(204, 128, 40, 30))
        self.measures.setMinimumSize(QSize(0, 30))
        self.measures.setMaximumSize(QSize(50, 16777215))
        self.measures.setFont(font)
        self.measures.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(137, 137, 206);\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgb(24, 40, 40);\n"
"}")
        self.measures.setMaxLength(3)
        self.measures.setAlignment(Qt.AlignCenter)
        self.time_sig_label_2 = QLabel(self.configure)
        self.time_sig_label_2.setObjectName(u"time_sig_label_2")
        self.time_sig_label_2.setGeometry(QRect(50, 250, 140, 27))
        sizePolicy2.setHeightForWidth(self.time_sig_label_2.sizePolicy().hasHeightForWidth())
        self.time_sig_label_2.setSizePolicy(sizePolicy2)
        self.time_sig_label_2.setMinimumSize(QSize(140, 0))
        self.time_sig_label_2.setMaximumSize(QSize(140, 16777215))
        self.time_sig_label_2.setFont(font)
        self.time_sig_label_2.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.time_sig_label_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.time_sig_label_2.setMargin(6)
        self.keysig_note = QComboBox(self.configure)
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.addItem("")
        self.keysig_note.setObjectName(u"keysig_note")
        self.keysig_note.setGeometry(QRect(200, 240, 50, 52))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.keysig_note.sizePolicy().hasHeightForWidth())
        self.keysig_note.setSizePolicy(sizePolicy3)
        self.keysig_note.setMaximumSize(QSize(50, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        self.keysig_note.setFont(font2)
        self.keysig_note.setStyleSheet(u"QComboBox {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	border-radius: 4px;\n"
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
"}\n"
"")
        self.keysig_acc = QComboBox(self.configure)
        self.keysig_acc.addItem("")
        self.keysig_acc.addItem("")
        self.keysig_acc.addItem("")
        self.keysig_acc.setObjectName(u"keysig_acc")
        self.keysig_acc.setGeometry(QRect(250, 240, 40, 25))
        self.keysig_acc.setMinimumSize(QSize(0, 25))
        self.keysig_acc.setMaximumSize(QSize(40, 16777215))
        self.keysig_acc.setFont(font1)
        self.keysig_acc.setStyleSheet(u"QComboBox {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	border-radius: 4px;\n"
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
"}\n"
"")
        self.keysig_scale = QComboBox(self.configure)
        self.keysig_scale.addItem("")
        self.keysig_scale.addItem("")
        self.keysig_scale.addItem("")
        self.keysig_scale.addItem("")
        self.keysig_scale.setObjectName(u"keysig_scale")
        self.keysig_scale.setGeometry(QRect(250, 264, 100, 20))
        self.keysig_scale.setMinimumSize(QSize(60, 0))
        font3 = QFont()
        font3.setPointSize(11)
        self.keysig_scale.setFont(font3)
        self.keysig_scale.setStyleSheet(u"QComboBox {\n"
"\n"
"	border: 1px solid rgb(16, 24, 24);\n"
"	border-radius: 4px;\n"
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
"}\n"
"")
        self.lineEdit = QLineEdit(self.configure)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 20, 211, 61))
        font4 = QFont()
        font4.setPointSize(12)
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(137, 137, 206);\n"
"	border: 0px;\n"
"}")
        self.keyboard_cat.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.lh_range_label.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.lh_range1_header_label.raise_()
        self.dash.raise_()
        self.lh_range2_header_label.raise_()
        self.rh_range_label.raise_()
        self.rh_range2_header_label.raise_()
        self.rh_range1_header_label.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.dash_2.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.ranges_label.raise_()
        self.lh_span.raise_()
        self.rh_span.raise_()
        self.length_label_3.raise_()
        self.length_label_4.raise_()
        self.quarter_note_weight.raise_()
        self.half_weight_widget.raise_()
        self.verticalLayoutWidget.raise_()
        self.widget.raise_()
        self.time_sig_label.raise_()
        self.length_label.raise_()
        self.measures.raise_()
        self.time_sig_label_2.raise_()
        self.keysig_note.raise_()
        self.keysig_acc.raise_()
        self.keysig_scale.raise_()
        self.lineEdit.raise_()
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setGeometry(QRect(0, 0, 1600, 80))
        self.top_bar.setStyleSheet(u"QFrame {\n"
"	border:2px\n"
"}")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.corner_logo = QPushButton(self.top_bar)
        self.corner_logo.setObjectName(u"corner_logo")
        self.corner_logo.setGeometry(QRect(0, 0, 80, 80))
        icon = QIcon()
        icon.addFile(u"data/images/avante-note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.corner_logo.setIcon(icon)
        self.corner_logo.setIconSize(QSize(100, 100))
        self.horizontalLayoutWidget_5 = QWidget(self.top_bar)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(140, 0, 481, 80))
        self.nav = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.nav.setSpacing(2)
        self.nav.setObjectName(u"nav")
        self.nav.setContentsMargins(0, 0, 0, 0)
        self.nav_configure = QPushButton(self.horizontalLayoutWidget_5)
        self.nav_configure.setObjectName(u"nav_configure")
        sizePolicy1.setHeightForWidth(self.nav_configure.sizePolicy().hasHeightForWidth())
        self.nav_configure.setSizePolicy(sizePolicy1)
        self.nav_configure.setMaximumSize(QSize(16777215, 16777215))
        self.nav_configure.setFont(font2)
        self.nav_configure.setStyleSheet(u"QPushButton {\n"
"	border: 2px ;\n"
"	border-radius: 4px;\n"
"	color: rgb(37, 37, 59);\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(137, 137, 206);\n"
"	background-color:  rgb(18, 30, 30);\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(123, 184, 184);\n"
"	border: rgb(85, 170, 255);\n"
"	border-radius: 4px;\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"")
        self.nav_configure.setCheckable(True)
        self.nav_configure.setChecked(True)

        self.nav.addWidget(self.nav_configure)

        self.nav_write = QPushButton(self.horizontalLayoutWidget_5)
        self.nav_write.setObjectName(u"nav_write")
        sizePolicy1.setHeightForWidth(self.nav_write.sizePolicy().hasHeightForWidth())
        self.nav_write.setSizePolicy(sizePolicy1)
        self.nav_write.setMaximumSize(QSize(16777215, 16777215))
        self.nav_write.setFont(font2)
        self.nav_write.setStyleSheet(u"QPushButton {\n"
"	border: 2px ;\n"
"	border-radius: 4px;\n"
"	color: rgb(37, 37, 59);\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(137, 137, 206);\n"
"	background-color:  rgb(18, 30, 30);\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(123, 184, 184);\n"
"	border: rgb(85, 170, 255);\n"
"	border-radius: 4px;\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"")
        self.nav_write.setCheckable(True)

        self.nav.addWidget(self.nav_write)

        self.write = QFrame(self.centralwidget)
        self.write.setObjectName(u"write")
        self.write.setGeometry(QRect(0, 80, 1600, 820))
        self.write.setFrameShape(QFrame.StyledPanel)
        self.write.setFrameShadow(QFrame.Raised)
        self.pdf = QCheckBox(self.write)
        self.pdf.setObjectName(u"pdf")
        self.pdf.setGeometry(QRect(450, 340, 100, 31))
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
        self.midi = QCheckBox(self.write)
        self.midi.setObjectName(u"midi")
        self.midi.setGeometry(QRect(450, 380, 100, 31))
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
        self.compose = QPushButton(self.write)
        self.compose.setObjectName(u"compose")
        self.compose.setGeometry(QRect(450, 480, 300, 40))
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
        self.song_filename_label = QLabel(self.write)
        self.song_filename_label.setObjectName(u"song_filename_label")
        self.song_filename_label.setGeometry(QRect(520, 280, 171, 30))
        self.song_filename_label.setMaximumSize(QSize(16777215, 30))
        self.song_filename_label.setFont(font4)
        self.song_filename_label.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.song_filename_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.song_filename_label.setMargin(6)
        self.cats = QCheckBox(self.write)
        self.cats.setObjectName(u"cats")
        self.cats.setGeometry(QRect(450, 420, 100, 31))
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
        self.song_name = QLineEdit(self.write)
        self.song_name.setObjectName(u"song_name")
        self.song_name.setGeometry(QRect(450, 150, 300, 44))
        self.song_name.setMinimumSize(QSize(240, 44))
        font5 = QFont()
        font5.setFamily(u"Rasa")
        font5.setPointSize(14)
        self.song_name.setFont(font5)
        self.song_name.setStyleSheet(u"QLineEdit {\n"
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
        self.song_name.setCursorPosition(0)
        self.song_folder = QPushButton(self.write)
        self.song_folder.setObjectName(u"song_folder")
        self.song_folder.setGeometry(QRect(450, 210, 300, 40))
        self.song_folder.setMinimumSize(QSize(0, 40))
        self.song_folder.setMaximumSize(QSize(400, 16777215))
        self.song_folder.setStyleSheet(u"QPushButton {\n"
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
        self.writing = QLabel(self.write)
        self.writing.setObjectName(u"writing")
        self.writing.setGeometry(QRect(450, 280, 74, 30))
        self.writing.setMaximumSize(QSize(16777215, 30))
        self.writing.setFont(font4)
        self.writing.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.writing.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.writing.setMargin(6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.top_bar.raise_()
        self.configure.raise_()
        self.write.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lh_range1_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range_label.setText(QCoreApplication.translate("MainWindow", u"Left:", None))
        self.lh_range2_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range1_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.lh_range2_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.rh_range_label.setText(QCoreApplication.translate("MainWindow", u"Right:", None))
        self.rh_range2_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.rh_range1_header_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.rh_range2_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.rh_range1_label.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.sharp_ranges.setText(QCoreApplication.translate("MainWindow", u"\u266f", None))
        self.flat_ranges.setText(QCoreApplication.translate("MainWindow", u"\u266d", None))
        self.ranges_label.setText(QCoreApplication.translate("MainWindow", u"Ranges", None))
        self.lh_span.setText(QCoreApplication.translate("MainWindow", u"steps", None))
        self.rh_span.setText(QCoreApplication.translate("MainWindow", u"steps", None))
        self.length_label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Span:</p></body></html>", None))
        self.length_label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Span:</p></body></html>", None))
        self.keyboard_cat_label_2.setText("")
        self.lh_range2_header_label_2.setText(QCoreApplication.translate("MainWindow", u"Quarter Icon", None))
        self.lh_range2_header_label_3.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.half_weight_label.setText(QCoreApplication.translate("MainWindow", u"Half Icon", None))
        self.half_weight_value.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.timesig_num.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.timesig_num.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_num.setPlaceholderText("")
        self.timesig_den.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.timesig_den.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_den.setPlaceholderText("")
        self.time_sig_label.setText(QCoreApplication.translate("MainWindow", u"Time Signature:", None))
        self.length_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Length in measures:</p><p><br/></p></body></html>", None))
        self.measures.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.measures.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.measures.setPlaceholderText("")
        self.time_sig_label_2.setText(QCoreApplication.translate("MainWindow", u"Key Signature:", None))
        self.keysig_note.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.keysig_note.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.keysig_note.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.keysig_note.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.keysig_note.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.keysig_note.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.keysig_note.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.keysig_acc.setItemText(0, QCoreApplication.translate("MainWindow", u"\u266e", None))
        self.keysig_acc.setItemText(1, QCoreApplication.translate("MainWindow", u"\u266f", None))
        self.keysig_acc.setItemText(2, QCoreApplication.translate("MainWindow", u"\u266d", None))

        self.keysig_scale.setItemText(0, QCoreApplication.translate("MainWindow", u"major", None))
        self.keysig_scale.setItemText(1, QCoreApplication.translate("MainWindow", u"minor", None))
        self.keysig_scale.setItemText(2, QCoreApplication.translate("MainWindow", u"harmonic", None))
        self.keysig_scale.setItemText(3, QCoreApplication.translate("MainWindow", u"melodic", None))

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unnamed Configuration", None))
        self.corner_logo.setText("")
        self.nav_configure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.nav_write.setText(QCoreApplication.translate("MainWindow", u"Write", None))
        self.pdf.setText(QCoreApplication.translate("MainWindow", u".pdf", None))
        self.midi.setText(QCoreApplication.translate("MainWindow", u".midi", None))
        self.compose.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.song_filename_label.setText("")
        self.cats.setText(QCoreApplication.translate("MainWindow", u"cats", None))
        self.song_name.setText("")
        self.song_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name song", None))
        self.song_folder.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.writing.setText(QCoreApplication.translate("MainWindow", u"Writing:", None))
    # retranslateUi

