# -*- coding utf-8 -*-
from __future__ import unicode_literals
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant


class TabModel(QAbstractTableModel):
    """
    Table model of data
    """

    def __init__(self, cells = [], data = [], parent = None):
        super(TabModel, self).__init__()
        self.cells = cells
        self.table = data


    def update(self, data):
        """
        assigns data source to model
        """
        print(data) # only testmode
        self.table = data

    def rowCount(self, parent = QModelIndex()):
        """
        :param parent: ???
        :return: numbers of row
        """
        return len(self.table)

    def columnCount(self, parent = QModelIndex()):
        """
        :param parent:
        :return: numbers of column
        """
        if self.table:
            return len(self.table[0])
        else:
            return 0

    def data(self, index, role = Qt.DisplayRole):
        """
        display data
        :return: string
        """
        i = index.row()
        j = index.column()

        if role == Qt.DisplayRole:
            return "{0}".format(self.table[i][j])
        else:
            return QVariant()

