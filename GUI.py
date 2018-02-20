# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from threading import Thread
from datetime import datetime
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 460)
        self.start_BTN = QtWidgets.QPushButton(Dialog)
        self.start_BTN.setGeometry(QtCore.QRect(540, 380, 91, 71))
        self.start_BTN.setDefault(True)
        self.start_BTN.setFlat(False)
        self.start_BTN.setObjectName("start_BTN")
        self.mode_comboBox = QtWidgets.QComboBox(Dialog)
        self.mode_comboBox.setGeometry(QtCore.QRect(440, 10, 191, 61))
        self.mode_comboBox.setToolTip("")
        self.mode_comboBox.setAccessibleName("")
        self.mode_comboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mode_comboBox.setAutoFillBackground(False)
        self.mode_comboBox.setCurrentText("")
        self.mode_comboBox.setFrame(True)
        self.mode_comboBox.setObjectName("mode_comboBox")
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.mode_comboBox.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 229, 130))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time1_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time1_lbl.setFont(font)
        self.time1_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.time1_lbl.setObjectName("time1_lbl")
        self.horizontalLayout.addWidget(self.time1_lbl)
        self.temp1_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp1_lbl.setFont(font)
        self.temp1_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.temp1_lbl.setObjectName("temp1_lbl")
        self.horizontalLayout.addWidget(self.temp1_lbl)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.time2_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time2_lbl.setFont(font)
        self.time2_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.time2_lbl.setObjectName("time2_lbl")
        self.horizontalLayout_3.addWidget(self.time2_lbl)
        self.temp2_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp2_lbl.setFont(font)
        self.temp2_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.temp2_lbl.setObjectName("temp2_lbl")
        self.horizontalLayout_3.addWidget(self.temp2_lbl)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.time3_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.time3_lbl.setFont(font)
        self.time3_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.time3_lbl.setObjectName("time3_lbl")
        self.horizontalLayout_4.addWidget(self.time3_lbl)
        self.temp3_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.temp3_lbl.setFont(font)
        self.temp3_lbl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.temp3_lbl.setObjectName("temp3_lbl")
        self.horizontalLayout_4.addWidget(self.temp3_lbl)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 0, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(450, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 280, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.source_temp = QtWidgets.QLabel(Dialog)
        self.source_temp.setGeometry(QtCore.QRect(20, 380, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.source_temp.setFont(font)
        self.source_temp.setObjectName("source_temp")
        self.time1_spinBox = QtWidgets.QSpinBox(Dialog)
        self.time1_spinBox.setGeometry(QtCore.QRect(510, 110, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time1_spinBox.setFont(font)
        self.time1_spinBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.time1_spinBox.setObjectName("time1_spinBox")
        self.stop_BTN = QtWidgets.QPushButton(Dialog)
        self.stop_BTN.setGeometry(QtCore.QRect(310, 380, 91, 71))
        self.stop_BTN.setDefault(True)
        self.stop_BTN.setFlat(False)
        self.stop_BTN.setObjectName("stop_BTN")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(150, 180, 311, 131))
        self.lcdNumber.setSizeIncrement(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(87, 240, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 240, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(87, 240, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setToolTip("")
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(450, 180, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.time2_spinBox = QtWidgets.QSpinBox(Dialog)
        self.time2_spinBox.setGeometry(QtCore.QRect(510, 210, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.time2_spinBox.setFont(font)
        self.time2_spinBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.time2_spinBox.setObjectName("time2_spinBox")
        self.temp_spinBox = QtWidgets.QSpinBox(Dialog)
        self.temp_spinBox.setGeometry(QtCore.QRect(510, 310, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.temp_spinBox.setFont(font)
        self.temp_spinBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.temp_spinBox.setObjectName("temp_spinBox")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(430, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(0, 240, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.ready_lbl_4 = QtWidgets.QLabel(Dialog)
        self.ready_lbl_4.setGeometry(QtCore.QRect(20, 200, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ready_lbl_4.setFont(font)
        self.ready_lbl_4.setObjectName("ready_lbl_4")
        self.temp_spinBox.setMinimum(4)

        self.mode_comboBox.addItem("انتخاب کنید")
        self.mode_comboBox.addItem("بیماری 1")
        self.mode_comboBox.addItem("بیماری 2")
        self.mode_comboBox.addItem("بیماری 3")
        self.mode_comboBox.addItem("بیماری 4")
        self.mode_comboBox.addItem("بیماری 5")
        self.mode_comboBox.addItem("انتخاب دستی")

        self.mode1_List = ['3', '50', '5', '5', '45', '8', '7', '10', '9']
        self.mode2_List = ['5', '10', '4', '6', '49', '12', '8', '50', '15']
        self.mode3_List = ['0', '30', '9', '8', '40', '12', '6', '50', '13']
        self.mode4_List = ['1', '3', '7', '0', '55', '15', '1', '10', '5']
        self.mode5_List = ['1', '2', '5', '0', '45', '8', '1', '0', '9']
        self.mode6_List = ['0', '0', '4']

        self.mode_List=[]
        self.mode_List.append(self.mode1_List)
        self.mode_List.append(self.mode2_List)
        self.mode_List.append(self.mode3_List)
        self.mode_List.append(self.mode4_List)
        self.mode_List.append(self.mode5_List)
        self.mode_List.append(self.mode6_List)

        self.mode_comboBox.currentIndexChanged.connect(self.mode_comboBox_item_changed)
        self.time1_spinBox.valueChanged.connect(self.time1_spinBox_value_changed)
        self.time2_spinBox.valueChanged.connect(self.time2_spinBox_value_changed)
        self.temp_spinBox.valueChanged.connect(self.temp_spinBox_value_changed)
        self.start_BTN.clicked.connect(self.start_BTN_func)
        self.stop_BTN.clicked.connect(self.stop_BTN_func)

        self.label_2.hide()
        self.label_3.hide()
        self.label_8.hide()
        self.time1_spinBox.hide()
        self.time2_spinBox.hide()
        self.temp_spinBox.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.time_part1 = 0
        self.time_part2 = 0
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.timer3 = QTimer()
        self.step_counter = 1
        self.flag=1

    def timer_update(self, radioButton_Status, mode_index):
        #print(radioButton_Status)
        if(self.step_counter==1 and self.flag==1):
            print("if 1")
            self.time_part1 = int(self.mode_List[mode_index-1][0])
            self.time_part2 = int(self.mode_List[mode_index-1][1])
            print(self.time_part1,self.time_part2)
            #self.time_part1 = 0
            #self.time_part2 = 15
            self.flag=0
        if (self.step_counter == 2 and self.flag == 1):
            print("if 2")
            self.time_part1 = int(self.mode_List[mode_index-1][3])
            self.time_part2 = int(self.mode_List[mode_index-1][4])
            print(self.time_part1, self.time_part2)
            #self.time_part1 = 0
            #self.time_part2 = 20
            self.flag = 0
        if (self.step_counter == 3 and self.flag == 1):
            print("if 3")
            self.time_part1 = int(self.mode_List[mode_index-1][6])
            self.time_part2 = int(self.mode_List[mode_index-1][7])
            print(self.time_part1, self.time_part2)
            #self.time_part1 = 0
            #self.time_part2 = 30
            self.flag = 0


        self.time_part1_str = ""
        self.time_part2_str = ""
        self.myStr = ""

        if (self.time_part1 < 10):
            self.time_part1_str = "0"+str(self.time_part1)
        if (self.time_part1 == 0):
            self.time_part1_str = "0"+str(self.time_part1)
        if (self.time_part2 < 10):
            self.time_part2_str = "0" + str(self.time_part2)
        if (self.time_part1 >= 10):
            self.time_part1_str = str(self.time_part1)
        if (self.time_part2 == 0):
            self.time_part2_str = "0"+str(self.time_part2)
        if (self.time_part2 >= 10):
            self.time_part2_str = str(self.time_part2)

        self.myStr=self.time_part1_str + ":" + self.time_part2_str

        print(self.myStr)
        app.processEvents()  # just this one line allows display of 'i'
        self.lcdNumber.display(self.myStr)

        if (self.time_part2>=0):
            self.time_part2 -= 1

        if (self.time_part2 == -1):
            if (self.time_part1 == 0):
                if(radioButton_Status==True):
                    print("Next Step")
                    self.step_counter+=1
                    self.flag=1
                if (radioButton_Status == False):
                    print("timer Stop 1")
                    self.timer1.stop()
            if (self.time_part1 > 0):
                self.time_part1 -= 1
                self.time_part2 = 59

        if (self.step_counter == 4):
            print("timer Stop 2")
            self.time_part1 = 0
            self.time_part2 = 0
            self.timer1.stop()

    def start_BTN_func(self):
        min = 0
        sec = 0
        self.myStr = ""
        if (self.mode_comboBox.currentIndex() == 0):
            print("Select Mode")
        else:
            self.mode_comboBox.setDisabled(1)
            self.timer1.timeout.connect(lambda: self.timer_update(self.radioButton.isChecked(),self.mode_comboBox.currentIndex()))
            self.timer1.start(1000)

            ####################################

    def stop_BTN_func(self):
        print("stop")

    def time1_spinBox_value_changed(self):
        self.mode6_List[0] = str(self.time1_spinBox.value())
        self.time1_lbl.setText("زمان : " + self.mode6_List[0] + ":" + self.mode6_List[1])

    def time2_spinBox_value_changed(self):
        self.mode6_List[1] = str(self.time2_spinBox.value())
        self.time1_lbl.setText("زمان : " + self.mode6_List[0] + ":" + self.mode6_List[1])

    def temp_spinBox_value_changed(self):
        valueStr = str(self.temp_spinBox.value())
        self.temp1_lbl.setText("دما : " + valueStr)

    def mode_comboBox_item_changed(self):
        self.label_6.show()
        self.temp2_lbl.show()
        self.time2_lbl.show()

        self.label_7.show()
        self.temp3_lbl.show()
        self.time3_lbl.show()

        self.label_2.hide()
        self.label_3.hide()
        self.label_8.hide()
        self.time1_spinBox.hide()
        self.time2_spinBox.hide()
        self.temp_spinBox.hide()
        if(self.mode_comboBox.currentIndex()==1):
            self.time1_lbl.setText("زمان : " + str(self.mode_List[0][0]) + ":" + str(self.mode_List[0][1]))
            self.temp1_lbl.setText("دما : " + str(self.mode_List[0][2]))

            self.time2_lbl.setText("زمان : " + str(self.mode_List[0][3]) + ":" + str(self.mode_List[0][4]))
            self.temp2_lbl.setText("دما : " + str(self.mode_List[0][5]))

            self.time3_lbl.setText("زمان : " + str(self.mode_List[0][6]) + ":" + str(self.mode_List[0][7]))
            self.temp3_lbl.setText("دما : " + str(self.mode_List[0][8]))

        if (self.mode_comboBox.currentIndex() == 2):
            self.time1_lbl.setText("زمان : " + str(self.mode_List[1][0]) + ":" + str(self.mode_List[1][1]))
            self.temp1_lbl.setText("دما : " + str(self.mode_List[1][2]))

            self.time2_lbl.setText("زمان : " + str(self.mode_List[1][3]) + ":" + str(self.mode_List[1][4]))
            self.temp2_lbl.setText("دما : " + str(self.mode_List[1][5]))

            self.time3_lbl.setText("زمان : " + str(self.mode_List[1][6]) + ":" + str(self.mode_List[1][7]))
            self.temp3_lbl.setText("دما : " + str(self.mode_List[1][8]))
        if (self.mode_comboBox.currentIndex() == 3):
            self.time1_lbl.setText("زمان : " + str(self.mode_List[2][0]) + ":" + str(self.mode_List[2][1]))
            self.temp1_lbl.setText("دما : " + str(self.mode_List[2][2]))

            self.time2_lbl.setText("زمان : " + str(self.mode_List[2][3]) + ":" + str(self.mode_List[2][4]))
            self.temp2_lbl.setText("دما : " + str(self.mode_List[2][5]))

            self.time3_lbl.setText("زمان : " + str(self.mode_List[2][6]) + ":" + str(self.mode_List[2][7]))
            self.temp3_lbl.setText("دما : " + str(self.mode_List[2][8]))
        if (self.mode_comboBox.currentIndex() == 4):
            self.time1_lbl.setText("زمان : " + str(self.mode_List[3][0]) + ":" + str(self.mode_List[3][1]))
            self.temp1_lbl.setText("دما : " + str(self.mode_List[3][2]))

            self.time2_lbl.setText("زمان : " + str(self.mode_List[3][3]) + ":" + str(self.mode_List[3][4]))
            self.temp2_lbl.setText("دما : " + str(self.mode_List[3][5]))

            self.time3_lbl.setText("زمان : " + str(self.mode_List[3][6]) + ":" + str(self.mode_List[3][7]))
            self.temp3_lbl.setText("دما : " + str(self.mode_List[3][8]))
        if (self.mode_comboBox.currentIndex() == 5):
            self.time1_lbl.setText("زمان : " + str(self.mode_List[4][0]) + ":" + str(self.mode_List[4][1]))
            self.temp1_lbl.setText("دما : " + str(self.mode_List[4][2]))

            self.time2_lbl.setText("زمان : " + str(self.mode_List[4][3]) + ":" + str(self.mode_List[4][4]))
            self.temp2_lbl.setText("دما : " + str(self.mode_List[4][5]))

            self.time3_lbl.setText("زمان : " + str(self.mode_List[4][6]) + ":" + str(self.mode_List[4][7]))
            self.temp3_lbl.setText("دما : " + str(self.mode_List[4][8]))

        if (self.mode_comboBox.currentIndex() == 6):
            self.time1_spinBox.setValue(0)
            self.time2_spinBox.setValue(0)
            self.temp_spinBox.setValue(0)
            # neshon dadane object ha baraye halate dasti
            self.label_2.show()
            self.label_3.show()
            self.label_8.show()
            self.time1_spinBox.show()
            self.time2_spinBox.show()
            self.temp_spinBox.show()

            self.label_6.hide()
            self.temp2_lbl.hide()
            self.time2_lbl.hide()

            self.label_7.hide()
            self.temp3_lbl.hide()
            self.time3_lbl.hide()

            self.time1_lbl.setText("زمان : 0")
            self.temp1_lbl.setText("دما : 4")
            self.time2_lbl.setText("زمان : 0")
            self.temp2_lbl.setText("دما : 0")
            self.time3_lbl.setText("زمان : 0")
            self.temp3_lbl.setText("دما : 0")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start_BTN.setText(_translate("Dialog", "شروع"))
        self.time1_lbl.setText(_translate("Dialog", "زمان:"))
        self.temp1_lbl.setText(_translate("Dialog", "دما:"))
        self.label_5.setText(_translate("Dialog", "بازه اول"))
        self.time2_lbl.setText(_translate("Dialog", "زمان:"))
        self.temp2_lbl.setText(_translate("Dialog", "دما:"))
        self.label_6.setText(_translate("Dialog", "بازه دوم"))
        self.time3_lbl.setText(_translate("Dialog", "زمان:"))
        self.temp3_lbl.setText(_translate("Dialog", "دما:"))
        self.label_7.setText(_translate("Dialog", "بازه سوم"))
        self.label.setText(_translate("Dialog", "نمایشگر"))
        self.label_2.setText(_translate("Dialog", "مقدار زمان : (دقیقه) "))
        self.label_3.setText(_translate("Dialog", "مقدار دما :"))
        self.source_temp.setText(_translate("Dialog", "دمای مخزن :"))
        self.stop_BTN.setText(_translate("Dialog", "پایان"))
        self.label_8.setText(_translate("Dialog", "مقدار زمان : (ثانیه) "))
        self.radioButton.setText(_translate("Dialog", "اتوماتیک"))
        self.status.setText(_translate("Dialog", "آماده با کار"))
        self.ready_lbl_4.setText(_translate("Dialog", "وضعیت سیستم :"))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

