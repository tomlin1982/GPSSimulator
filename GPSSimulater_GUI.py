# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPSSimulater_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from QLed import QLed

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(800, 600))
        Frame.setMaximumSize(QtCore.QSize(800, 600))
        Frame.setSizeIncrement(QtCore.QSize(800, 600))
        Frame.setBaseSize(QtCore.QSize(800, 600))        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        Frame.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 781, 231))
        self.groupBox.setObjectName("groupBox")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 30, 761, 81))
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setStyleSheet("border: 2px solid silver; color: rgb(25, 31, 24) ; background: rgb(135, 173, 52);")
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 130, 761, 81))
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setStyleSheet("border: 2px solid silver; color: rgb(25, 31, 24) ; background: rgb(135, 173, 52);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(610, 510, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 370, 141, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(190, 370, 141, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(400, 370, 141, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(540, 370, 141, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(2)
        self.label_2.setMidLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(10, 300, 50, 50))
        #self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self._led=QLed(self.frame, onColour=QLed.Red, shape=QLed.Circle)
        self._led.value=False
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(self) 
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(65, 300, 689, 41))
        self.checkBox.setStyleSheet("QCheckBox::indicator { width: 50px; height: 50px;}")
        self.checkBox.setObjectName("checkBox")


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "GPS 模擬器"))
        self.groupBox.setTitle(_translate("Frame", "現在時刻"))
        self.pushButton.setText(_translate("Frame", "離開"))
        self.checkBox.setText(_translate("Frame", "啟動連續傳送模式"))        
        self.label.setText(_translate("Frame", "傳輸埠："))
        self.label_3.setText(_translate("Frame", "鮑  率："))
        self.label_2.setText(_translate("Frame", "GPS 模擬器"))

         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())