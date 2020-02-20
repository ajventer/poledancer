# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poledancer_about.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(516, 350)
        About.setFocusPolicy(QtCore.Qt.TabFocus)
        self.CloseAboutBtn = QtWidgets.QPushButton(About)
        self.CloseAboutBtn.setGeometry(QtCore.QRect(220, 320, 112, 31))
        self.CloseAboutBtn.setObjectName("CloseAboutBtn")
        self.AboutText = QtWidgets.QTextBrowser(About)
        self.AboutText.setGeometry(QtCore.QRect(0, 0, 521, 311))
        self.AboutText.setSource(QtCore.QUrl("file:///home/metalpoetza/Source/poledancer/Docs/ABOUT.html"))
        self.AboutText.setObjectName("AboutText")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Poledancer"))
        self.CloseAboutBtn.setText(_translate("About", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
