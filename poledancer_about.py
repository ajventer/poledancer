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
        About.resize(874, 531)
        About.setFocusPolicy(QtCore.Qt.TabFocus)
        self.gridLayout = QtWidgets.QGridLayout(About)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(1, 1, 1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AboutText = QtWidgets.QTextBrowser(About)
        self.AboutText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.AboutText.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.AboutText.setSource(QtCore.QUrl("file:///home/metalpoetza/Source/poledancer/Docs/ABOUT.html"))
        self.AboutText.setObjectName("AboutText")
        self.verticalLayout.addWidget(self.AboutText)
        self.CloseAboutBtn = QtWidgets.QPushButton(About)
        self.CloseAboutBtn.setObjectName("CloseAboutBtn")
        self.verticalLayout.addWidget(self.CloseAboutBtn)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

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
