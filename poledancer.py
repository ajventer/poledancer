#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow
from events import MainwindowEvents
from mainwindow_control import PoleDancerMainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PoleDancerMainWindow()
    ui.setupUi(MainWindow)
    events = MainwindowEvents(app, ui)
    MainWindow.show()
    sys.exit(app.exec_())