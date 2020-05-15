from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QGridLayout, QWidget
from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout

app = QApplication([])
window = QWidget()

lay1 = QHBoxLayout()
lay1.addWidget(QPushButton('OK'))
lay1.addWidget(QPushButton('Cancel'))
lay2 = QHBoxLayout()
lay2.addWidget(QPushButton('Print'))
lay2.addWidget(QPushButton('Panel'))
lay3 = QVBoxLayout()
lay3.addLayout(lay1)
lay3.addLayout(lay2)

window.setLayout(lay3)
window.show()
window.move(400, 400)
app.exec_()