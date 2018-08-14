#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from .ui_pwd import Ui_Pwd
from .dialog_deploy import get_dialog
import os



class Pwd(QWidget):

    confirmed = pyqtSignal(str)

    def __init__(self, taskcode):
        super().__init__()
        self.ui = Ui_Pwd()
        self.ui.setupUi(self)
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
            self.dialog = get_dialog(self.taskcode,self.ui.line_edit_pwd.text())
            self.dialog.show()
        else:
            self.ui.line_edit_pwd.clear()
            self.ui.line_edit_pwd.setPlaceholderText('wrong password, try again')
