# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/pwd.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pwd(object):
    def setupUi(self, Pwd):
        Pwd.setObjectName("Pwd")
        Pwd.resize(380, 70)
        Pwd.setMinimumSize(QtCore.QSize(380, 70))
        Pwd.setMaximumSize(QtCore.QSize(380, 70))
        self.verticalLayout = QtWidgets.QVBoxLayout(Pwd)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_edit_pwd = QtWidgets.QLineEdit(Pwd)
        self.line_edit_pwd.setObjectName("line_edit_pwd")
        self.verticalLayout.addWidget(self.line_edit_pwd)

        self.retranslateUi(Pwd)
        QtCore.QMetaObject.connectSlotsByName(Pwd)

    def retranslateUi(self, Pwd):
        _translate = QtCore.QCoreApplication.translate
        Pwd.setWindowTitle(_translate("Pwd", "Form"))

