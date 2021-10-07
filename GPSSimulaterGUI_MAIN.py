# -*- coding: utf-8 -*-
import os
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal, QSettings, QVariant, QTimer, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtGui, QtWidgets 
import serial
import serial.tools.list_ports
from clock_png import img
import base64
from GPSSimulater_GUI import Ui_Frame
import binascii
import textwrap
from MyDialog import Ui_Dialog
from nmeasim.simulator import Simulator
from datetime import datetime, timezone
from os import environ
import time


my_home_path = os.getcwd()
myini_file = "GPSADJ.ini"
myinifile_path = my_home_path+"\\"+myini_file
print(myinifile_path)
if os.path.isfile(myinifile_path):
      size = os.path.getsize(myinifile_path)
      if size == 0:
          with open(myinifile_path, "w") as file:
              file.write("[System]\n")
              file.write("ComportName=COM1\n")
              file.write("BaudRate=4800\n")
              file.write("ShareCOMwithTIDS=0\n")
              file.write("CalibrateSecs=1")

      else:
          pass
else:
  with open(myinifile_path, "w") as file:
    file.write("[System]\n")
    file.write("ComportName=COM1\n")
    file.write("BaudRate=4800\n")
    file.write("ShareCOMwithTIDS=0\n")
    file.write("CalibrateSecs=1")

class MyMainForm(QMainWindow, Ui_Frame):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.im = QtGui.QPixmap()
        self.im.loadFromData(base64.b64decode(img))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(self.im)
        self.setWindowIcon(self.icon)

        self.mytime = QDateTime.currentDateTime()        

        
        self.qsettings = QSettings(myinifile_path, QSettings.IniFormat)       
        self.qsettings.beginGroup("System")
        print(self.qsettings.allKeys())
        self.MyComportName = self.qsettings.value('ComportName')
        self.MyBaudRate = self.qsettings.value('BaudRate')
        self.MyCalibrateSecs = self.qsettings.value('CalibrateSecs')
        print(self.MyComportName)
        print(self.MyBaudRate)
        print(self.MyCalibrateSecs)

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.sentTimeinCOM)

        self.serialport = serial.Serial()
        self.comlists = []
        for port in serial.tools.list_ports.comports():
            self.comlists.append(str(port)[0:5])

        if len(self.comlists) == 0:
            self.comboBox.addItem(self.MyComportName)
        else:
            self.comboBox.addItems(self.comlists)
        # print(self.comboBox.maxCount())


        self.listports = ["110", "300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000", '256000']
      
        self.comboBox_2.addItems(self.listports)
        my_index = self.listports.index(self.MyBaudRate)
        self.comboBox_2.setCurrentIndex(my_index)
        # self.checkBox.setChecked(True) 
        self.checkBox.stateChanged.connect(self.clickBox)
        self.timer.start(1000)              
        self.showTime()
        self.sim = Simulator()
        self.sim.gps.output = ('GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA')
        self.sim.gps.num_sats = 14  # GPS 衛星數
        self.sim.gps.lat = 0.25058606  # GPS 緯度
        self.sim.gps.lon = 1.215601853  # GPS 經度
        self.sim.gps.altitude = -13  # GPS 高度
        self.sim.gps.geoid_sep = -45.3
        self.sim.gps.mag_var = -1.1
        self.sim.gps.kph = 60.0
        self.sim.gps.heading = 90.0
        self.sim.gps.mag_heading = 90.1

        # print(dir(self.checkBox.event))
        # if self.checkBox.isChecked:            
        #     print(self.checkBox.isChecked())  
        #     self.timer.start(1000)              
        #     self.showTime()         


        # elif not self.checkBox.isChecked:
        #     self.timer.timeout.disconnect(self.showTime)
        #     self.timer.stop()


        self.pushButton.clicked.connect(self.Exit)
        self.pushButton.setStyleSheet(
            "QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))} QPushButton {background-color: #3cbaa2; border: 1px solid black; border-radius: 5px; } QPushButton:disabled {background-color: rgb(170, 170, 127)}"
        )

       

        



    def clickBox(self, state):
    
        if state == Qt.Checked:
            
            self.mycomport_text = str(self.comboBox.currentText())
            print(self.mycomport_text)
            self.comboBox.setEnabled(False)
            self.mybuadrate_text = str(self.comboBox_2.currentText())
            print(self.mybuadrate_text)
            self.comboBox_2.setEnabled(False)            
            self.serialport.baudrate = self.mybuadrate_text
            self.serialport.port = self.mycomport_text


            ##self.serialport.open()
            try:
                self.serialport.open()
            except serial.SerialException as e:
                self.showDialog()
                sys.stderr.write('Could not open serial port {}: {}\n'.format(self.serialport.name, e))
 

                sys.exit(1)
            # print('Checked')
            if self.MyCalibrateSecs == '1':
                self.timer2.start(1000)
                self.sentTimeinCOM()
            else:
                mycount = int(self.MyCalibrateSecs)
                self.timer2.setInterval(1 * mycount * 1000)
                self.timer2.start()
                self.sentTimeinCOM()
            
 
        else:
            # print('Unchecked')
            self.sim.kill()
            self.timer2.stop()
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            if self.serialport.is_open == True:
                self.serialport.close()





    def display(self,str):
        print(str)
     
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        # self.listWidget.addItem(str)

        # print(str)
    
    def showTime(self):

        # print(len(self.TimeDisplay))
        # print(self.TimeDisplay[6:8])
        self.mytime = QDateTime.currentDateTime()
        self.DataDisplay = self.mytime.toString('yyyy-MM-dd')
        self.TimeDisplay = self.mytime.toString('hh:mm:ss')

        if (int(self.TimeDisplay[6:8]) % 2) == 0:
            self.TimeDisplay = self.TimeDisplay[:2] + ' ' + self.TimeDisplay[3:]

        if (int(self.TimeDisplay[6:8]) % 2) == 0:
            self.TimeDisplay = self.TimeDisplay[:5] + ' ' + self.TimeDisplay[6:]
        
        self.lcdNumber_2.display(self.TimeDisplay)
        self.lcdNumber.display(self.DataDisplay)
    
    def sentTimeinCOM(self):
        self.mytime = QDateTime.currentDateTime()
        self.mytime2 = self.mytime.toUTC()
        print(self.mytime2)
        self.DataDisplay = self.mytime2.toString('yyyy-MM-dd')
        self.TimeDisplay = self.mytime2.toString('hh:mm:ss')
        if (int(self.TimeDisplay[6:8]) % 0.5) == 0:
            self._led.toggleValue()
        
        # for i in range(0,len(self.TimeDisplay)):
            # print(i, self.TimeDisplay[i])

        
        my_ss = int(self.TimeDisplay[6:8])
        print(my_ss)
        my_mm = int(self.TimeDisplay[3:5])
        print(my_mm)
        my_hh = int(self.TimeDisplay[0:2])
        print(my_hh)


        # print(self.DataDisplay)
        # print(len(self.DataDisplay))

        my_yy = int(self.DataDisplay[0:4])
        print(my_yy)
        my_mo = int(self.DataDisplay[5:7])
        print(my_mo)
        my_dd = int(self.DataDisplay[8:10])
        print(my_dd)





        # sim.gps.date_time = datetime.now(TZ_LOCAL)  # PC current time, local time zone
        self.sim.gps.date_time = datetime(my_yy, my_mo, my_dd, my_hh, my_mm, my_ss, tzinfo=timezone.utc)
        self.sim.gps.hdop = 3.1
        self.sim.gps.vdop = 5.0
        self.sim.gps.pdop = (self.sim.gps.hdop ** 2 + self.sim.gps.vdop ** 2) ** 0.5
        # Precision decimal points for various measurements
        self.sim.gps.horizontal_dp = 4
        self.sim.gps.vertical_dp = 1
        self.sim.gps.speed_dp = 1
        self.sim.gps.time_dp = 1
        self.sim.gps.angle_dp = 1
        # Keep straight course for simulator - don't randomly change the heading
        self.sim.heading_variation = 0
        self.sim.serve(output=self.serialport, blocking=False)
        # temp01 = my_hh * 3600 + my_mm * 60 + my_ss
        # # print(temp01)
        #
        # temp02 = ("0x%06X" % temp01)[2:]
        # print(temp02)
        # res = textwrap.fill(temp02, width=2)
        # temp03 = res.split()
        # # print(temp03)
        # my_hex_time_text = temp03[2]+temp03[1]+temp03[0]
        # # my_hex_time_text = "000000"
        #
        # my_hex_text_title = '3C2E73742E3E00000005'
        # hex_time_text = '8F9D00'
        # hex_text_end = '00373030313031303030303030000000000000C84132352E300000000000000000000000000A000000070000003000DE443C2E656E2E3E'
        # total_data_temp = my_hex_text_title + my_hex_time_text + hex_text_end
        # # print(total_data_temp)
        # # print(total_data_temp.encode('utf-8'))
        # my_sent_data = binascii.unhexlify(total_data_temp.encode('utf-8'))
        # print(my_sent_data)
        # self.serialport.write(my_sent_data)

    def showDialog(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    

    def Exit(self, event):
        time_temp = "00:00:00"
        data_temp = "0000-00-00"        
        self.lcdNumber_2.display(time_temp)
        self.lcdNumber.display(data_temp)
        print(self.serialport.port)
        if self.serialport.port == None:
            self.qsettings.setValue('ComportName', self.MyComportName)
        else:
            self.qsettings.setValue('ComportName', self.serialport.port[0:4])
        # print(type(self.comboBox_2.currentText()))
        # print(type(self.serialport.baudrate))
        if self.serialport.baudrate == 9600 :
            print(self.comboBox_2.currentText())
            self.qsettings.setValue('BaudRate', self.comboBox_2.currentText())
        else:
            self.qsettings.setValue('BaudRate', self.serialport.baudrate)
        self.timer.stop()
        sys.exit(self)
      

    




class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    finished = pyqtSignal()
    trigger1 = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()
        self.stop_flag = False
    
    def stop(self):
        self.stop_flag = True

    def run(self):
        self.mytime = QDateTime.currentDateTime()
        self.DataDisplay = self.mytime.toString('yyyy-MM-dd')
        self.TimeDisplay = self.mytime.toString('hh:mm:ss') 
        my_ss = int(self.TimeDisplay[6:8])
        # print(myDisplayTime)
        
        self.trigger1.emit(self.TimeDisplay)
        self.finished.emit()


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "1.0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1.0"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1.0"
    environ["QT_SCALE_FACTOR"] = "1.0"




if __name__ == "__main__":
    suppress_qt_warnings()
    # app = QApplication(sys.argv)
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    myWin = MyMainForm()
    myWin.show()

    im = QtGui.QPixmap()
    im.loadFromData(base64.b64decode(img))

    menu = QtWidgets.QMenu( ) 

    icon = QtGui.QIcon()
    icon.addPixmap(im)
    tray = QtWidgets.QSystemTrayIcon()
    tray.setIcon(icon) 
    tray.setVisible(True)
    option1 = QtWidgets.QAction("顯示/隱藏") 
    # option2 = QtWidgets.QAction("GFG")
    # option1.triggered.connect(Form.show())
    option1.triggered.connect(lambda: myWin.hide()
            if myWin.isVisible() else myWin.show())
    menu.addAction(option1) 
    # menu.addAction(option2) 
    quit = QtWidgets.QAction("結束") 
    quit.triggered.connect(app.quit) 
    menu.addAction(quit)
    tray.setContextMenu(menu) 
    app.exec_() 




    # sys.exit(app.exec_())
