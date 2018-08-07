# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser.setObjectName("text_browser")
        self.verticalLayout.addWidget(self.text_browser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.line_edit_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_ip.setObjectName("line_edit_ip")
        self.horizontalLayout_2.addWidget(self.line_edit_ip)
        self.button_path = QtWidgets.QPushButton(self.centralwidget)
        self.button_path.setObjectName("button_path")
        self.horizontalLayout_2.addWidget(self.button_path)
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setObjectName("button_start")
        self.horizontalLayout_2.addWidget(self.button_start)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 29))
        self.menubar.setObjectName("menubar")
        self.menuDEPLOY = QtWidgets.QMenu(self.menubar)
        self.menuDEPLOY.setObjectName("menuDEPLOY")
        self.menuABOUT = QtWidgets.QMenu(self.menubar)
        self.menuABOUT.setObjectName("menuABOUT")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_init_hotload = QtWidgets.QAction(MainWindow)
        self.action_init_hotload.setObjectName("action_init_hotload")
        self.action_about_1zlab = QtWidgets.QAction(MainWindow)
        self.action_about_1zlab.setObjectName("action_about_1zlab")
        self.action_clean_up = QtWidgets.QAction(MainWindow)
        self.action_clean_up.setObjectName("action_clean_up")
        self.menuDEPLOY.addAction(self.action_init_hotload)
        self.menuDEPLOY.addAction(self.action_clean_up)
        self.menuABOUT.addAction(self.action_about_1zlab)
        self.menubar.addAction(self.menuDEPLOY.menuAction())
        self.menubar.addAction(self.menuABOUT.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.line_edit_ip.setPlaceholderText(_translate("MainWindow", "ESP32 IP"))
        self.button_path.setText(_translate("MainWindow", "指定工程路径"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.menuDEPLOY.setTitle(_translate("MainWindow", "TOOLS"))
        self.menuABOUT.setTitle(_translate("MainWindow", "ABOUT"))
        self.action_init_hotload.setText(_translate("MainWindow", "deploy hotload to esp32"))
        self.action_about_1zlab.setText(_translate("MainWindow", "1ZLAB"))
        self.action_clean_up.setText(_translate("MainWindow", "clean up esp32"))

