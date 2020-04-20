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

class LoginDialog(QDialog):
    """ Login window """

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        # labels, editpole and buttons ###
        loginLbl = QLabel('Login')
        passwordLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.password = QLineEdit()
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        layout = QGridLayout(self)
        layout.addWidget(loginLbl, 0, 0)
        layout.addWidget(self.login, 0, 1)
        layout.addWidget(passwordLbl, 1, 0)
        layout.addWidget(self.password, 1, 1)
        layout.addWidget(self.buttons, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Logowanie')

    def loginPassword(self):
        return (self.login.text().strip(),
                self.password.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginPassword(parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        login, password = dialog.loginPassword()
        return (login, password, ok == QDialog.Accepted)

