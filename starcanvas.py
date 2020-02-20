from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class starCanvas(QLabel):
    def __init__(self, mainwindow, ui_window):
        QLabel.__init__(self)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.mainwindow = mainwindow
        self.ui_window = ui_window
        self.pixmap = QPixmap("Resources/icon.png")
        self.setPixmap(self.pixmap)
        self.installEventFilter(self)
        self.setMouseTracking(True)
        self.Clicked = None
        self.previous = None
        self.drift = None
        self.stage = 1
        self.enabled = True


    def eventFilter(self, source, event):
        if (source is self and event.type() == QEvent.Resize):
            self.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio))
        elif (source is self and event.type() == QEvent.MouseButtonRelease):
            self.handleClick(event.pos())
        return self.mainwindow.eventFilter(source, event)

    def updateImage(self, image):
        self.pixmap = QPixmap.fromImage(image)
        self.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio))
        self.update()


    def paintEvent(self, QPaintEvent):
        print (self.stage, self.previous, self.Clicked)
        super(starCanvas, self).paintEvent(QPaintEvent)
        if self.stage == 1 and self.previous and self.Clicked:
            print ('Drawing drift')
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red))
            painter.drawLine(self.previous.x(),self.previous.y(),self.Clicked.x(),self.previous.y())
            painter.setPen(QPen(Qt.blue))
            painter.drawLine(self.Clicked.x(),self.previous.y(),self.Clicked.x(),self.Clicked.y())
            return 
        if self.Clicked and self.stage > 1:       
            print ('Drawing crosshairs')          
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red))
            painter.drawLine(self.Clicked.x(),0,self.Clicked.x(),self.height())
            painter.drawLine(0,self.Clicked.y(),self.width(),self.Clicked.y())



    def drift_str(self):
        return 'Azimuth drift: '+str(self.drift[0])+' / Altitude drift:  '+str(self.drift[1])


    def calculate_drift(self):
        print (self.Clicked, self.previous)
        drift_az = self.Clicked.x() - self.previous.x()
        drift_alt = self.Clicked.y() - self.previous.y()
        self.drift = (drift_az, drift_alt)

    def handleClick(self, pos):
        if not self.enabled:
            return
        self.Clicked = pos
        if self.stage in  (2,3,4):
            self.ui_window.StatusBarButton.setEnabled(True)
        self.update()
