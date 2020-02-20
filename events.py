
from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow
from time import sleep

class MainwindowEvents(object):
    def __init__(self, app, mainwindow, camera):
        self.app = app
        self.camera = camera
        self.mainwindow = mainwindow
        self.mainwindow.actionQuit.triggered.connect(app.closeAllWindows)
        self.mainwindow.actionCameraConnect.triggered.connect(self.CameraConnect)
        self.mainwindow.StatusBarButton.clicked.connect(self.Sequence)

    def CameraConnect(self):
        self.camera.connect()
        self.mainwindow.StatusBarButton.setEnabled(True)
        self.mainwindow.statusbar.showMessage('Camera connected. Press start to begin')

    def startSequence(self):
        self.mainwindow.starcanvas.Clicked = None
        self.mainwindow.statusbar.showMessage('Click on a star. If you are unhappy, click elsewhere. Click next when ready')
        self.mainwindow.StatusBarButton.setEnabled(False)
        self.mainwindow.StatusBarButton.setText ('Next')
        new_image = self.camera.getImage()
        self.mainwindow.starcanvas.updateImage(new_image)
        self.mainwindow.starcanvas.stage = 2

    def sequence2(self):
        self.mainwindow.statusbar.showMessage('Please wait for some drifting to happen')
        self.mainwindow.starcanvas.enabled = False
        self.mainwindow.StatusBarButton.setEnabled(False)
        self.countdown = self.camera.driftDelay
        self.timer = QtCore.QTimer(self.app)
        self.timer.timeout.connect(self.timer_timeout)
        self.timer.start(1000)


    def timer_timeout(self):
        self.countdown -= 1
        if self.countdown > 0:
            self.mainwindow.StatusBarButton.setText ('Drifting: ' + str(self.countdown)+'s')
            self.mainwindow.StatusBarButton.update()            
        else:
            self.mainwindow.StatusBarButton.setText ('Next')
            self.mainwindow.StatusBarButton.setEnabled(True)
            self.mainwindow.starcanvas.stage = 3
            self.mainwindow.statusbar.showMessage('Click on the same star again. Click "Calculate" when ready')
            self.timer.stop()


    def sequence3(self):
        self.mainwindow.starcanvas.enabled = True
        self.mainwindow.starcanvas.previous = self.mainwindow.starcanvas.Clicked
        self.mainwindow.starcanvas.Clicked = None
        self.mainwindow.StatusBarButton.setEnabled(False)
        self.mainwindow.StatusBarButton.setText ('Calculate')
        new_image = self.camera.getImage()
        self.mainwindow.starcanvas.updateImage(new_image)
        self.mainwindow.starcanvas.stage = 4        

    def sequence4(self):
        self.mainwindow.starcanvas.calculate_drift()
        self.mainwindow.statusbar.showMessage(self.mainwindow.starcanvas.drift_str())
        self.mainwindow.StatusBarButton.setText ('Restart')
        self.mainwindow.starcanvas.stage = 1
        self.mainwindow.starcanvas.update()


    def Sequence(self):
        print (self.mainwindow.starcanvas.stage)
        if self.mainwindow.starcanvas.stage == 1:
            self.startSequence()
        elif self.mainwindow.starcanvas.stage == 2:
            self.sequence2()              
        elif self.mainwindow.starcanvas.stage == 3:
            self.sequence3()
        elif self.mainwindow.starcanvas.stage == 4:
            self.sequence4()




        


