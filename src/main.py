#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import time
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from win import mixSerialWin

class mixSerialMain(QMainWindow, mixSerialWin.Ui_MixSerialPort):

    def __init__(self, parent=None):
        super(mixSerialMain, self).__init__(parent)
        self._register_callbacks()
        self.setupUi(self)
        self.comboBox_baud.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_dataBits.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_stopBits.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_parityBit.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)

    def _register_callbacks(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = mixSerialMain(None)
    mainWin.setWindowTitle(u"Mix Serial Port v0.1")
    mainWin.show()

    sys.exit(app.exec())

