#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from app.ui_deploy import Ui_DialogDeploy
import sys
import os
import json


class Deploy(QWidget):
    loadprce = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_DialogDeploy()
        self.ui.setupUi(self)
        self.parent = parent
        self.init_view()
        self.init_connection()

    def init_view(self):
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowIcon(QIcon('./icon.png'))
        self.com = ''
        self.ui.progressBar.hide()
        coms = [i for i in os.listdir('/dev/') if i.startswith('ttyUSB')]
        self.ui.combo_box_com.addItems(coms)

    def init_connection(self):
        self.ui.button_deploy.clicked.connect(self.button_deploy_clicked)
        self.loadprce.connect(self.progress_changed)

    def progress_changed(self, value):
        self.ui.progressBar.setValue(value)

    def button_deploy_clicked(self):
        self.ui.progressBar.show()
        self.ui.progressBar.setValue(0)
        self.com = '/dev/' + self.ui.combo_box_com.currentText()

    def show(self):
        pw = self.parent.width()
        ph = self.parent.height()
        px = self.parent.geometry().x()
        py = self.parent.geometry().y()

        w = self.width()
        h = self.height()
        self.move(px+(pw-w)/2, py+(ph-h)/2)
        super().show()


class DeployHotLoad(Deploy):

    def __init__(self, parent, pwd):
        super().__init__(parent)
        self.pwd = pwd

    def init_view(self):
        super().init_view()
        self.setWindowTitle('Deploy Hotload Framework to ESP')
        try:
            with open('./.hotload/config.json', 'r') as f:
                self.config = json.loads(f.read())
        except:
            self.config = dict(wifi_pwd='', wifi_name='', is_developing='1')
        self.ui.line_edit_wifi.setText(self.config['wifi_name'])
        self.ui.line_edit_pwd.setText(self.config['wifi_pwd'])

    def button_deploy_clicked(self):
        super().button_deploy_clicked()

        self.config['wifi_name'] = self.ui.line_edit_wifi.text()
        self.config['wifi_pwd'] = self.ui.line_edit_pwd.text()

        if self.config['wifi_name'] and self.config['wifi_pwd'] and self.com:

            with open('./.hotload/config.json', 'w') as f:
                f.write(json.dumps(self.config))

            total = len(os.listdir('./.hotload'))

            for index, i in enumerate(os.listdir('./.hotload')):
                os.system(
                    'echo \'{0}\' | sudo -S ampy -p {1} put {2}/{3}'.format(self.pwd, self.com, './.hotload', i))

                self.loadprce.emit(100*int(index)/total)

            self.ui.progressBar.hide()
            self.close()

        else:
            QMessageBox.warning(self, 'waring', '请将选项设置完整')


class DeployClear(Deploy):
    def __init__(self, parent, pwd):
        super().__init__(parent)
        self.pwd = pwd

    def init_view(self):
        super().init_view()
        self.ui.line_edit_pwd.hide()
        self.ui.line_edit_wifi.hide()
        self.setWindowTitle('Deploy Clear Script to ESP')

    def button_deploy_clicked(self):
        super().button_deploy_clicked()
        if self.com:
            os.system(
                'echo \'{0}\' | sudo ampy -p {1} put {2}/{3}'.format(self.pwd, self.com, './.clear', 'main.py'))
        else:
            QMessageBox.warning(self, 'waring', '请将选项设置完整')

        self.ui.progressBar.hide()
        self.close()
