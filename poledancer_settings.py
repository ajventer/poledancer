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
        Settings.setWindowModality(QtCore.Qt.WindowModal)
        Settings.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.DriftTimeLabel = QtWidgets.QLabel(Settings)
        self.DriftTimeLabel.setObjectName("DriftTimeLabel")
        self.gridLayout.addWidget(self.DriftTimeLabel, 0, 0, 1, 1)
        self.DriftTime = QtWidgets.QDoubleSpinBox(Settings)
        self.DriftTime.setObjectName("DriftTime")
        self.gridLayout.addWidget(self.DriftTime, 0, 1, 1, 1)
        self.SettingsButtons = QtWidgets.QDialogButtonBox(Settings)
        self.SettingsButtons.setOrientation(QtCore.Qt.Horizontal)
        self.SettingsButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Save)
        self.SettingsButtons.setObjectName("SettingsButtons")
        self.gridLayout.addWidget(self.SettingsButtons, 1, 0, 1, 2)

        self.retranslateUi(Settings)
        self.SettingsButtons.accepted.connect(Settings.accept)
        self.SettingsButtons.rejected.connect(Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.DriftTimeLabel.setText(_translate("Settings", "Drift time (seconds):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
