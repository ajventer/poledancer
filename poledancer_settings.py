# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poledancer_settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(510, 300)
        self.widget = QtWidgets.QWidget(Settings)
        self.widget.setGeometry(QtCore.QRect(10, 40, 491, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DriftTimeLabel = QtWidgets.QLabel(self.widget)
        self.DriftTimeLabel.setObjectName("DriftTimeLabel")
        self.horizontalLayout_2.addWidget(self.DriftTimeLabel)
        self.driftTime = QtWidgets.QSpinBox(self.widget)
        self.driftTime.setMinimum(1)
        self.driftTime.setMaximum(600)
        self.driftTime.setObjectName("driftTime")
        self.horizontalLayout_2.addWidget(self.driftTime)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingsReset = QtWidgets.QPushButton(self.widget)
        self.settingsReset.setAutoDefault(False)
        self.settingsReset.setObjectName("settingsReset")
        self.horizontalLayout.addWidget(self.settingsReset)
        self.settingsRestore = QtWidgets.QPushButton(self.widget)
        self.settingsRestore.setAutoDefault(False)
        self.settingsRestore.setObjectName("settingsRestore")
        self.horizontalLayout.addWidget(self.settingsRestore)
        self.settingsSave = QtWidgets.QPushButton(self.widget)
        self.settingsSave.setAutoDefault(False)
        self.settingsSave.setObjectName("settingsSave")
        self.horizontalLayout.addWidget(self.settingsSave)
        self.settingsCancel = QtWidgets.QPushButton(self.widget)
        self.settingsCancel.setObjectName("settingsCancel")
        self.horizontalLayout.addWidget(self.settingsCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.DriftTimeLabel.setText(_translate("Settings", "Drift time (seconds):"))
        self.settingsReset.setText(_translate("Settings", "Reset"))
        self.settingsRestore.setText(_translate("Settings", "Restore Defaults"))
        self.settingsSave.setText(_translate("Settings", "Save/Apply"))
        self.settingsCancel.setText(_translate("Settings", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
