
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4 import QtCore, QtGui, uic


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('script.ui', self)
        self.show()

        self.connect(self.btn_close, QtCore.SIGNAL("clicked()"),
                     QtGui.qApp.quit)

        self.connect(self.btn_start, QtCore.SIGNAL("clicked()"),
                     QtGui.qApp.quit)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())