#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui import Ui_Widget

class Task(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Task, self).__init__(parent)
        self.setupUi(self)

        self.loginBtn.clicked.connect(self.login)
        self.endBtn.clicked.connect(self.end)

    def login(self):
        slogin, ok = QInputDialog.getText(self, 'Logowanie', 'Podaj login:')
        if ok:
            password, ok = QInputDialog.getText(self, 'Logowanie', 'Podaj haslo:')
            if ok:
                if not login or not password:
                    QMessageBox.warning(
                        self, 'Błąd', 'Pusty login lub hasło!', QMessageBox.Ok)
                    return
                QMessageBox.information(
                    self, 'Dane logowania',
                    'Podano: ' + slogin + ' ' + password, QMessageBox.Ok)

    def end(self):
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    winapp = Task()
    winapp.show()
    winapp.move(350, 200)
    sys.exit(app.exec_())