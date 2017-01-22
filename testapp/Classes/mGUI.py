#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
"""

import sys
from PyQt4 import QtGui, QtCore


class QuitWindow(QtGui.QWidget):

    def __init__(self):
        super(QuitWindow, self).__init__()
        
        self.initUI()

    def initUI(self):
        
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        self.raise_()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
                            "Are you sure to quit?",
                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                            QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()         

