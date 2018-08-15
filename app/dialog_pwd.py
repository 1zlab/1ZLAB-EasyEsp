#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from .ui_pwd import Ui_Pwd
# from .dialog_deploy import get_dialog
import os


class Pwd(QWidget):

    confirmed = pyqtSignal(str)

    def __init__(self, parent, taskcode):
        super().__init__()
        self.ui = Ui_Pwd()
        self.ui.setupUi(self)
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowIcon(QIcon('./icon.png'))
        self.setWindowTitle('Input Password')
        self.ui.line_edit_pwd.setPlaceholderText('sudo password')
        self.ui.line_edit_pwd.returnPressed.connect(self.send_pwd)
        self.ui.line_edit_pwd.setEchoMode(QLineEdit.Password)
        self.taskcode = taskcode


    def send_pwd(self):
        # test password
        ret = os.system('echo \'%s\' | sudo -S pwd' %
                        self.ui.line_edit_pwd.text())
        if ret == 0:
            self.confirmed.emit(self.ui.line_edit_pwd.text())
            self.close()
            self.dialog = self.parent.get_dialog(
                self.taskcode, self.ui.line_edit_pwd.text())
            self.dialog.show()
        else:
            self.ui.line_edit_pwd.clear()
            self.ui.line_edit_pwd.setPlaceholderText(
                'wrong password, try again')

    def show(self):
        pw = self.parent.width()
        ph = self.parent.height()
        px = self.parent.geometry().x()
        py = self.parent.geometry().y()

        w = self.width()
        h = self.height()
        self.move(px+(pw-w)/2, py+(ph-h)/2)
        super().show()
