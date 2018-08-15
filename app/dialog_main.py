#!/usr/bin/python3
# -*- coding: utf-8 -*-
from watchdog.observers import Observer
from .handler import FileEventHandler
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from .ui_main import Ui_MainWindow
from .dialog_deploy import DeployHotLoad
from .dialog_deploy import DeployClear
from .dialog_pwd import Pwd
import time
import sys
import os
import json


class EasyEsp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_data()
        self.init_view()
        self.init_connection()

    def init_data(self):
        self.is_not_start = True
        self.path = ''
        self.pwd = ''

    def init_view(self):
        self.setWindowTitle('1ZLAB/EasyEsp')
        self.setWindowIcon(QIcon('./icon.png'))

    def init_connection(self):
        self.ui.action_init_hotload.triggered.connect(self.deploy_hotload)
        self.ui.action_clean_up.triggered.connect(self.clear_up)
        self.ui.button_path.clicked.connect(self.select_path)
        self.ui.button_start.clicked.connect(self.start_hot_load)
        # 启动GUI 验证 password

    def set_pwd(self, pwd):
        self.pwd = pwd
        # print(self.pwd)

    def select_path(self):
        self.path = QFileDialog.getExistingDirectory()

        self.setWindowTitle('1ZLAB/EzEsp--->%s' % self.path.split('/')[-1])

    def start_hot_load(self):
        if self.path and self.ui.line_edit_ip.text():

            self.ui.button_path.setEnabled(not self.is_not_start)
            self.ui.line_edit_ip.setEnabled(not self.is_not_start)
            self.is_not_start = not self.is_not_start
            if self.is_not_start:
                self.ui.button_start.setText('Start')
                self.observer.stop()
            else:
                self.ui.button_start.setText('Stop')

                self.event_handler = FileEventHandler(
                    self.ui.line_edit_ip.text(), self.path)
                print(self.path)
                self.observer = Observer()
                self.observer.schedule(self.event_handler, self.path, True)
                self.event_handler.logs.connect(self.print_logs)

                if not os.path.exists(self.path+'/main.py'):
                    os.system('cp ./libs/main.py %s' % self.path)
                try:
                    os.system('code %s' % self.path)
                except:
                    pass

                self.observer.start()

        else:
            QMessageBox.warning(self, 'Waring', '请先指定工程路径和ESP IP')

    def deploy_hotload(self):
        if not self.pwd:
            self.pwd_confirm = Pwd(self, 0)
            self.pwd_confirm.confirmed.connect(self.set_pwd)
            self.pwd_confirm.show()
        else:
            self.deploy = DeployHotLoad(self, self.pwd)
            self.deploy.show()

    def clear_up(self):
        if not self.pwd:
            self.pwd_confirm = Pwd(self, 1)
            self.pwd_confirm.confirmed.connect(self.set_pwd)
            self.pwd_confirm.show()
        else:
            self.deploy = DeployClear(self, self.pwd)
            self.deploy.show()

    def print_logs(self, log):

        self.ui.text_browser.setText(
            self.ui.text_browser.toPlainText()+"\n"+log)
    

    def get_dialog(self, taskcode, pwd):
        if taskcode == 0:
            dialog = DeployHotLoad(self, pwd)
        elif taskcode == 1:
            dialog = DeployClear(self, pwd)

        return dialog

    def show(self):
        desktop = QApplication.desktop()
        self.move((desktop.width()-self.width())/2,
              (desktop.height()-self.height())/2)

        super().show()