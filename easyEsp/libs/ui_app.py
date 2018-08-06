# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 164)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_browser = QtWidgets.QTextBrowser(Dialog)
        self.text_browser.setObjectName("text_browser")
        self.horizontalLayout.addWidget(self.text_browser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.combo_box_com = QtWidgets.QComboBox(Dialog)
        self.combo_box_com.setObjectName("combo_box_com")
        self.verticalLayout.addWidget(self.combo_box_com)
        self.button_path = QtWidgets.QPushButton(Dialog)
        self.button_path.setObjectName("button_path")
        self.verticalLayout.addWidget(self.button_path)
        self.button_start = QtWidgets.QPushButton(Dialog)
        self.button_start.setObjectName("button_start")
        self.verticalLayout.addWidget(self.button_start)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_path.setText(_translate("Dialog", "指定工程路径"))
        self.button_start.setText(_translate("Dialog", "Start"))

