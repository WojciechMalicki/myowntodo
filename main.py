#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon
from gui import Ui_Widget
from tabmodel import TabModel
import motdconnect
import motdparser


class Task(QWidget, Ui_Widget):
    """
    application interface
    """
    def __init__(self, parent=None):
        super(Task, self).__init__(parent)
        self.setupUi(self)
        self.commandLine.returnPressed.connect(self.onEnterPressed)
        self.configuration()


    def configuration(self):
        self.setGeometry(30, 30, 300, 400)
        self.setWindowTitle("Colitodoli")
        self.setWindowIcon(QIcon('colitodoli.png'))
        self.show()

    def onEnterPressed(self):
        print(self.commandLine.text())
        motdparser.command_parse(self.commandLine.text())
        self.commandLine.clear()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    motdconnect.connect()
    model = TabModel()
    winapp = Task()
    sys.exit(app.exec_())