# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class Ui_Widget(object):
    """
    main window
    """
    def setupUi (self, Widget):
        """
        Window setup
        """

        Widget.setObjectName("Widget")
        # Table view of data
        self.view = QTableView()

        # Command Line
        self.commandLine = QLineEdit()

        # window's main layout
        layoutV = QVBoxLayout(self)
        layoutV.addWidget(self.view)
        layoutV.addWidget(self.commandLine)

        # widget's properties
        self.resize(500, 300)


