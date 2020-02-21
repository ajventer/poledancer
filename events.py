
from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow
from poledancer_about import Ui_About
from poledancer_settings import Ui_Settings
from time import sleep
from settings import Settings
import camera
import os

class MainwindowEvents(object):
    def __init__(self, app, mainwindow):
        self.camera = None
        self.app = app
        self.mainwindow = mainwindow
        self.settings = Settings()
        self.reset = Settings()
        self.settings.load()
        self.reset.load()
        self.mainwindow.actionQuit.triggered.connect(self.quitApplication)
        self.mainwindow.StatusBarButton.clicked.connect(self.Sequence)
        self.mainwindow.actionAbout.triggered.connect(lambda: self.showAbout('about'))
        self.mainwindow.actionLicense.triggered.connect(lambda: self.showAbout('license'))
        self.mainwindow.actionManual.triggered.connect(lambda: self.showAbout('manual'))
        self.mainwindow.actionCamera_Simulator_for_testing.triggered.connect(self.SimulatorConnect)
        self.mainwindow.actionPrefferences.triggered.connect(self.showSettings)
        self.mainwindow.statusbar.showMessage('Connect your camera to start')
        for cam in self.mainwindow.CameraMenu:
            cam.triggered.connect(lambda: self.CameraConnect(cam.objectName()))

    def quitApplication(self):
        if self.camera:
            self.camera.exit()
        self.app.closeAllWindows()

    def updateSettings(self, task):
        print (task)
        if task == 'reset':
            self.Settings.driftTime.setValue(self.reset['DriftTimer'])                
        elif task == 'restore':
            self.settings.restore_defaults()
            self.Settings.driftTime.setValue(self.settings['DriftTimer'])
        elif task == 'cancel':
            self.SettingsDLG.close()
        elif task == 'save':
            self.settings['DriftTimer'] = int(self.Settings.driftTime.text())
            self.settings.save()
            self.reset.load()
            self.SettingsDLG.close()

    def showSettings(self):
        print ("Showing settings dialog")
        self.SettingsDLG = QtWidgets.QDialog()
        self.Settings = Ui_Settings()
        self.Settings.setupUi(self.SettingsDLG)
        self.Settings.driftTime.setValue(self.settings['DriftTimer'])
        self.Settings.settingsReset.clicked.connect(lambda: self.updateSettings('reset'))
        self.Settings.settingsRestore.clicked.connect(lambda: self.updateSettings('restore'))
        self.Settings.settingsSave.clicked.connect(lambda: self.updateSettings('save'))
        self.Settings.settingsCancel.clicked.connect(lambda: self.updateSettings('cancel'))
        self.SettingsDLG.exec_()


    def showAbout(self, doc):
        here = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
        self.AboutDlg = QtWidgets.QDialog()
        self.About = Ui_About()
        self.About.setupUi(self.AboutDlg)
        if doc == 'about':
            self.AboutDlg.setWindowTitle("About Poledancer")
            self.About.AboutText.setSource(QtCore.QUrl('file://%s/Docs/ABOUT.html' %here))
        elif doc == 'license':
            self.AboutDlg.setWindowTitle("Poledancer license")
            self.About.AboutText.setSource(QtCore.QUrl('file://%s/Docs/COPYING.html' %here))
        elif doc == 'manual':
            self.AboutDlg.setWindowTitle("Poledancer User's Manual")
            self.About.AboutText.setSource(QtCore.QUrl('file://%s/Docs/MANUAL.html' %here))
            self.AboutDlg.showMaximized()
        self.About.CloseAboutBtn.clicked.connect(self.closeAbout)        
        self.AboutDlg.show()
        self.AboutDlg.exec_()

    def closeAbout(self):
        self.AboutDlg.close()


    def SimulatorConnect(self):
        self.camera = camera.CameraSimulator()
        self.camera.driftDelay = self.settings["DriftTimer"]
        self.mainwindow.StatusBarButton.setEnabled(True)
        self.mainwindow.statusbar.showMessage('Simulator connected. Press start to begin')


    def CameraConnect(self, cam):
        print ("Trying to connect to ", cam)
        self.camera = camera.Camera()
        self.camera.driftDelay = self.settings["DriftTimer"]
        self.camera.connect(cam)
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
