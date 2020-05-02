#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui import Ui_Widget, LoginDialog
from tabmodel import TabModel
import motdconnect


class Task(QWidget, Ui_Widget):
    """
    application interface
    """
    def __init__(self, parent=None):
        super(Task, self).__init__(parent)
        self.setupUi(self)

        self.loginBtn.clicked.connect(self.login)
        self.endBtn.clicked.connect(self.end)

    def login(self):
        """
        user login to app
        """
        slogin, password, ok = LoginDialog.getLoginPassword(self)
        if not ok:
            return

        if not slogin or not password:
            QMessageBox.warning(self, 'Błąd',
                                'Pusty login lub hasło!', QMessageBox.Ok)
            return

        self.user = motdconnect.tolog(slogin, password)

        if self.user is None:
            QMessageBox.critical(self, 'Błąd', 'Błędne hasło', QMessageBox.Ok)
            return

        tasks = motdconnect.readData(self.user)
        model.update(tasks)
        model.layoutChanged.emit()
        self.refreshView()


    def refreshView(self):
        self.view.setModel(model) # model transfer to view


    def end(self):
        self.close()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    motdconnect.connect()
    model = TabModel()
    winapp = Task()
    winapp.show()
    winapp.move(350, 200)
    sys.exit(app.exec_())