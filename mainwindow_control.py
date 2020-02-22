from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow
from starcanvas import starCanvas
import camera

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
        self.StatusBarButton = QtWidgets.QPushButton(self.centralwidget)
        self.StatusBarButton.setObjectName("pushButton")
        self.StatusBarButton.setText ('Start')
        self.StatusBarButton.setEnabled(False)
        self.HistoryButton = QtWidgets.QLabel(self.centralwidget)
        self.HistoryButton.setObjectName("historyButton")
        self.HistoryButton.setText ('History')
        self.HistoryButton.setEnabled(True)        

        self.statusbar.addPermanentWidget(self.HistoryButton)
        self.statusbar.addPermanentWidget(self.StatusBarButton)


        self.CameraMenu = []
        for cam in camera.Camera().camera_list():
            self.CameraMenu.append(QtWidgets.QAction(MainWindow))
            self.CameraMenu[-1].setObjectName(cam[1])    
            self.CameraMenu[-1].setText(cam[0])
            self.menuConnect.addAction(self.CameraMenu[-1])


        self.statusbar.showMessage('Connect your camera to start')




