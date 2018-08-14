# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/qtcreator_deploy_hotload.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogDeploy(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setGeometry(QtCore.QRect(0, 0, 413, 290))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.combo_box_com = QtWidgets.QComboBox(Dialog)
        self.combo_box_com.setCurrentText("")
        self.combo_box_com.setObjectName("combo_box_com")
        self.verticalLayout.addWidget(self.combo_box_com)
        self.line_edit_wifi = QtWidgets.QLineEdit(Dialog)
        self.line_edit_wifi.setObjectName("line_edit_wifi")
        self.verticalLayout.addWidget(self.line_edit_wifi)
        self.line_edit_pwd = QtWidgets.QLineEdit(Dialog)
        self.line_edit_pwd.setObjectName("line_edit_pwd")
        self.verticalLayout.addWidget(self.line_edit_pwd)
        self.button_deploy = QtWidgets.QPushButton(Dialog)
        self.button_deploy.setObjectName("button_deploy")
        self.verticalLayout.addWidget(self.button_deploy)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("DialogDeployHotload", "Deploy Hotload"))
        self.line_edit_wifi.setPlaceholderText(_translate("DialogDeployHotload", "wifi name"))
        self.line_edit_pwd.setPlaceholderText(_translate("DialogDeployHotload", "wifi password"))
        self.button_deploy.setText(_translate("DialogDeployHotload", "Deploy"))

