import sys
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *
from qtdesigner import *
import serial, serial.tools.list_ports
from threading import Thread, Event

accelX=0.0
accelY=0.0
accelZ=0.0
gyroX=0.0
gyroY=0.0
gyroZ=0.0
angleX=0.0
angleY=0.0
angleZ=0.0
sicaklik=0.0
sicaklik1=0.0
basinc=0.0
nem=0.0

veriPaketi = []

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.unitUI = Ui_MainWindow()
        self.unitUI.setupUi(self)
        
        self.serial = Communication()

        self.combo_boxes_add_item()
        self.init_table()
        self.unitUI.pushButtonConnect.clicked.connect(self.fonk_connect)
        self.unitUI.pushButtonDisconnect.clicked.connect(self.fonk_disconnect)
        
        self.serial.data_received.connect(self.update_table)

    def init_table(self):
        header_list = ["accelX", "accelY", "accelZ", "gyroX", "gyroY", "gyroZ", "angleX", "angleY", "angleZ", "sicaklik", "sicaklik1", "basinc", "nem"]        
        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet("background-color: #A5A977; color: #131313")
        self.tableWidget.verticalHeader().hide()       
        self.values = 0
        self.tableWidget.setRowCount(self.values + 1)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowHeight(0,10)
      
        for index, header in enumerate(header_list):
            header_item = QTableWidgetItem(header)
            header_item.setForeground(QColor("#131313"))
            self.tableWidget.setHorizontalHeaderItem(index, header_item)
            header_item = self.tableWidget.horizontalHeader()
            header_item.setStyleSheet("background-color: #A5A977")

        for index, header in enumerate(header_list):
            header_item = QTableWidgetItem(header)
            header_item.setBackground(QColor("#A5A977"))
            self.tableWidget.setHorizontalHeaderItem(index, header_item)

        self.unitUI.verticalLayoutTable.addWidget(self.tableWidget)

    def update_table(self, data):
        global veriPaketi

        def floatToStr(number):
            return str(number)
        
        values = data.split()
        if len(values) == 13:
            self.tableWidget.selectRow(self.values)
            table_list = list(map(floatToStr, values))
            index = 0
            while index <= 12:
                self.tableWidget.setItem(self.values, index, QTableWidgetItem(table_list[index]))
                self.tableWidget.setRowHeight(index, 10)
                index += 1
            self.values += 1
            self.tableWidget.setRowCount(self.values + 1)
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def fonk_connect(self):
        portName = self.unitUI.comboBoxPort.currentText()
        baudRate = int(self.unitUI.comboBoxBaudrate.currentText())

        self.serial.serialPort.port = portName
        self.serial.serialPort.baudrate = baudRate
        self.serial.connect()

        if self.serial.serialPort.is_open: #self.alive.isSet() and self.serialPort.is_open

            self.unitUI.pushButtonConnect.setEnabled(False)
            self.unitUI.pushButtonDisconnect.setEnabled(True)
            self.unitUI.comboBoxPort.setEnabled(False)
            self.unitUI.comboBoxBaudrate.setEnabled(False)
    
    def fonk_disconnect(self):
        self.serial.disconnect()

        if not self.serial.serialPort.is_open:

            self.unitUI.pushButtonConnect.setEnabled(True)
            self.unitUI.pushButtonDisconnect.setEnabled(False)
            self.unitUI.comboBoxPort.setEnabled(True)
            self.unitUI.comboBoxBaudrate.setEnabled(True)
        
    def combo_boxes_add_item(self):
        self.unitUI.comboBoxPort.clear()
        self.unitUI.comboBoxBaudrate.clear()

        serialPorts = serial.tools.list_ports.comports()
        serialPortNames = [port.device for port in serialPorts]
        self.unitUI.comboBoxPort.addItems(serialPortNames)

        baudRates = [9600, 19200, 38400, 57600, 115200]
        self.unitUI.comboBoxBaudrate.addItems(map(str, baudRates))


class Communication(QObject):                                                   
    data_received = pyqtSignal(str) 

    def __init__(self):
        super().__init__()
        self.serialPort  = serial.Serial()

        self.thread = None
        self.alive = Event()

    def connect(self):
        try:    
            self.serialPort.open()

        except:
            print("baglanti acılamadı")

        if (self.serialPort.is_open): 
            self.start_thread()  

    def disconnect(self):
        self.stop_thread()
        self.serialPort.close()
        
    def read_data(self):
        global veriPaketi, accelX, accelY, accelZ, gyroX, gyroY, gyroZ, angleX, angleY, angleZ, sicaklik, sicaklik1, basinc, nem

        while(self.alive.isSet() and self.serialPort.is_open):
            st = time.time()
            data = self.serialPort.readline().decode("utf-8").strip()
            values = data.split()
            print(type(values))
            print(values[3])
            print(len(values))
            if(len(values) == 13):
                #mahir kart
                accelX = float(values[0])
                accelY = float(values[1])
                accelZ = float(values[2])
                gyroX = float(values[3])
                gyroY = float(values[4])
                gyroZ = float(values[5])
                angleX = float(values[6])
                angleY = float(values[7])
                angleZ = float(values[8])
                sicaklik = float(values[9])
                sicaklik1 = float(values[10])
                basinc = float(values[11])
                nem = float(values[12]) / 100.0  
                veriPaketi = [accelX,accelY,accelZ,gyroX,gyroY,gyroZ,angleX,angleY,angleZ,sicaklik,sicaklik1,basinc,nem]
                self.data_received.emit(data)
                
    def start_thread(self):
        self.thread = Thread(target=self.read_data) 
        self.thread.setDaemon(True)  
        self.alive.set()         
        self.thread.start()  

    def stop_thread(self):
        if(self.thread is not None):
            self.alive.clear()
            self.thread.join()
            self.thread = None
        
            
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
