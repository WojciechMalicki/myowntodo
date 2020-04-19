# -*- coding: utf-8 -*-

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

		# Push buttons
		self.loginBtn = QPushButton("Za&loguj")
		self.endBtn = QPushButton("&Koniec")

		# Push buttons' layout
		layout = QHBoxLayout()
		layout.addWidget(self.loginBtn)
		layout.addWidget(self.endBtn)

		# window's main layout
		layoutV = QVBoxLayout(self)
		layoutV.addWidget(self.view)
		layoutV.addLayout(layout)

		# widget's properties
		self.setWindowTitle("My Own ToDo")
		self.resize(500, 300)



