# Form implementation generated from reading ui file '..\gui\MixSerialPort.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MixSerialPort(object):
    def setupUi(self, MixSerialPort):
        MixSerialPort.setObjectName("MixSerialPort")
        MixSerialPort.resize(813, 605)
        self.centralwidget = QtWidgets.QWidget(parent=MixSerialPort)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1_com = QtWidgets.QWidget()
        self.tab1_com.setObjectName("tab1_com")
        self.tabWidget.addTab(self.tab1_com, "")
        self.tab2_touch = QtWidgets.QWidget()
        self.tab2_touch.setObjectName("tab2_touch")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab2_touch)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab2_touch, "")
        self.tab3_res = QtWidgets.QWidget()
        self.tab3_res.setObjectName("tab3_res")
        self.tabWidget.addTab(self.tab3_res, "")
        MixSerialPort.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MixSerialPort)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 22))
        self.menubar.setObjectName("menubar")
        MixSerialPort.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MixSerialPort)
        self.statusbar.setObjectName("statusbar")
        MixSerialPort.setStatusBar(self.statusbar)

        self.retranslateUi(MixSerialPort)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MixSerialPort)

    def retranslateUi(self, MixSerialPort):
        _translate = QtCore.QCoreApplication.translate
        MixSerialPort.setWindowTitle(_translate("MixSerialPort", "MixSerialPort"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1_com), _translate("MixSerialPort", "Serial COM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2_touch), _translate("MixSerialPort", "Touch Track"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3_res), _translate("MixSerialPort", "Reserved"))