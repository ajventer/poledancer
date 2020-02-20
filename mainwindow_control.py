from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow
from starcanvas import starCanvas

class PoleDancerMainWindow(Ui_MainWindow):
    '''
    All UI code not done via QT-Designer,
    thus allowing it to not be overridden when the QTDesigner code 
    is changed.
    '''
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.starcanvas = starCanvas(MainWindow, self)
        MainWindow.setCentralWidget(self.starcanvas)
        MainWindow.showMaximized()
        self.statusbar.showMessage('Connect your camera to start')
        self.StatusBarButton = QtWidgets.QPushButton(self.centralwidget)
        #self.StatusBarButton.setGeometry(QtCore.QRect(290, 300, 112, 31))
        self.StatusBarButton.setObjectName("pushButton")
        self.StatusBarButton.setText ('Start')
        self.StatusBarButton.setEnabled(False)

        self.statusbar.addPermanentWidget(self.StatusBarButton)




