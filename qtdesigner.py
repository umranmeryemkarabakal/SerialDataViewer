# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\umk54\Desktop\project\teamimutogay\qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(236, 231, 210);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBoxPort = QtWidgets.QComboBox(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPort.sizePolicy().hasHeightForWidth())
        self.comboBoxPort.setSizePolicy(sizePolicy)
        self.comboBoxPort.setStyleSheet("background-color: rgb(105, 160, 81);\n"
"color: rgb(19, 19, 19);\n"
"border-radius: 5px;\n"
"QComboBox {\n"
"    text-align: center;\n"
"}")
        self.comboBoxPort.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.horizontalLayout_2.addWidget(self.comboBoxPort)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.comboBoxBaudrate = QtWidgets.QComboBox(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxBaudrate.sizePolicy().hasHeightForWidth())
        self.comboBoxBaudrate.setSizePolicy(sizePolicy)
        self.comboBoxBaudrate.setStyleSheet("background-color: rgb(105, 160, 81);\n"
"color: rgb(19, 19, 19);\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"QComboBox {\n"
"    text-align: center;\n"
"}")
        self.comboBoxBaudrate.setObjectName("comboBoxBaudrate")
        self.horizontalLayout_2.addWidget(self.comboBoxBaudrate)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButtonConnect = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConnect.sizePolicy().hasHeightForWidth())
        self.pushButtonConnect.setSizePolicy(sizePolicy)
        self.pushButtonConnect.setStyleSheet("background-color: rgb(105, 160, 81);\n"
"color: rgb(19, 19, 19);\n"
"border-radius: 5px;")
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.horizontalLayout_2.addWidget(self.pushButtonConnect)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButtonDisconnect = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDisconnect.sizePolicy().hasHeightForWidth())
        self.pushButtonDisconnect.setSizePolicy(sizePolicy)
        self.pushButtonDisconnect.setStyleSheet("background-color: rgb(105, 160, 81);\n"
"color: rgb(19, 19, 19);\n"
"border-radius: 5px;")
        self.pushButtonDisconnect.setObjectName("pushButtonDisconnect")
        self.horizontalLayout_2.addWidget(self.pushButtonDisconnect)
        self.horizontalLayout_2.setStretch(0, 20)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 20)
        self.horizontalLayout_2.setStretch(3, 10)
        self.horizontalLayout_2.setStretch(4, 20)
        self.horizontalLayout_2.setStretch(5, 5)
        self.horizontalLayout_2.setStretch(6, 20)
        self.verticalLayout.addWidget(self.horizontalFrame)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setStyleSheet("background-color: rgb(165, 169, 119);\n"
"border-radius: 5px;")
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutTable = QtWidgets.QVBoxLayout()
        self.verticalLayoutTable.setObjectName("verticalLayoutTable")
        self.verticalLayout_2.addLayout(self.verticalLayoutTable)
        self.verticalLayout.addWidget(self.verticalFrame_2)
        self.verticalLayout.setStretch(0, 15)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 80)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 5)
        self.gridLayout.setColumnMinimumWidth(1, 90)
        self.gridLayout.setColumnMinimumWidth(2, 5)
        self.gridLayout.setRowMinimumHeight(0, 5)
        self.gridLayout.setRowMinimumHeight(1, 90)
        self.gridLayout.setRowMinimumHeight(2, 5)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 90)
        self.gridLayout.setColumnStretch(2, 5)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 90)
        self.gridLayout.setRowStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonConnect.setText(_translate("MainWindow", "Connect"))
        self.pushButtonDisconnect.setText(_translate("MainWindow", "Disconnect"))

