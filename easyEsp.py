#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtNetwork import QUdpSocket
from PyQt5.QtNetwork import QHostAddress
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from libs.ui_app import Ui_MainWindow
from libs.ui_config import Ui_Dialog
from libs.handler import FileEventHandler
from watchdog.observers import Observer
import time
import sys
import os
import json


class pwdDialog(QWidget):

    confirmed = pyqtSignal(str)

    def __init__(self, parent, taskcode):
        super().__init__()
        self.parent = parent
        self.line_edit_pwd = QLineEdit(self)
        self.line_edit_pwd.setPlaceholderText('sudo password')
        self.line_edit_pwd.returnPressed.connect(self.send_pwd)
        self.line_edit_pwd.setEchoMode(QLineEdit.Password)
        self.taskcode = taskcode

    def send_pwd(self):
        # test password
        ret = os.system('echo \'%s\' | sudo -S pwd' % self.line_edit_pwd.text())
        if ret == 0:
            self.confirmed.emit(self.line_edit_pwd.text())
            self.close()
            self.dialog = ConfigDialog(self.taskcode, self.line_edit_pwd.text())
            self.dialog.show()
        else:
            self.line_edit_pwd.clear()
            self.line_edit_pwd.setPlaceholderText('wrong password, try again')


class ConfigDialog(QWidget):
    loadprce = pyqtSignal(int)

    def __init__(self, taskcode, pwd):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_view(taskcode)
        self.init_connection()
        self.pwd = pwd

    def init_view(self, taskcode):
        self.taskcode = taskcode
        if self.taskcode == 1:
            self.windowTitle = 'clear esp'
        elif self.taskcode == 0:
            self.windowTitle = 'deploy to esp'
        self.com = ''
        try:
            with open('./.hotload/config.json', 'r') as f:
                self.config = json.loads(f.read())
        except:
            self.config = dict(wifi_pwd='', wifi_name='', is_developing='1')
        self.ui.progressBar.hide()
        coms = [i for i in os.listdir('/dev/') if i.startswith('ttyUSB')]
        self.ui.combo_box_com.addItems(coms)
        self.ui.line_edit_wifi.setText(self.config['wifi_name'])
        self.ui.line_edit_pwd.setText(self.config['wifi_pwd'])

    def init_connection(self):
        self.ui.button_deploy.clicked.connect(self.button_deploy_clicked)
        self.loadprce.connect(self.progress_changed)

    def progress_changed(self, value):
        self.ui.progressBar.setValue(value)

    def button_deploy_clicked(self):
        self.ui.progressBar.show()
        self.ui.progressBar.setValue(0)
        self.com = '/dev/' + self.ui.combo_box_com.currentText()
        self.config['wifi_name'] = self.ui.line_edit_wifi.text()
        self.config['wifi_pwd'] = self.ui.line_edit_pwd.text()

        if not self.config['wifi_name'] == '' and not self.config['wifi_pwd'] == '':

            with open('./.hotload/config.json', 'w') as f:
                f.write(json.dumps(self.config))

            if self.taskcode == 0:
                total = len(os.listdir('./.hotload'))
                pwd_confirm = pwdDialog(self)

                for index, i in enumerate(os.listdir('./.hotload')):
                    os.system(
                        'echo \'{0}\' | sudo -S ampy -p {1} put {2}/{3}'.format(self.pwd, self.com, './.hotload', i))

                    if not r == 0:
                        break

                    self.loadprce.emit(100*int(index)/total)

            else:
                os.system(
                    'echo \'{0}\' | sudo ampy -p {1} put {2}/{3}'.format(self.pwd, self.com, './.clear', 'main.py'))

            self.ui.progressBar.hide()
            self.close()

        else:
            QMessageBox.warning(self, 'waring', '请将选项设置完整')


class EzEspGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_not_start = True
        self.init_data()
        self.init_view()
        self.init_connection()

    def init_data(self):
        self.path = ''
        self.pwd = ''

    def init_view(self):
        self.setWindowTitle('1ZLAB/EzEsp')

    def init_connection(self):
        self.ui.action_init_hotload.triggered.connect(self.deploy_hotload)
        self.ui.action_clean_up.triggered.connect(self.clear_up)
        self.ui.button_path.clicked.connect(self.select_path)
        self.ui.button_start.clicked.connect(self.start_hot_load)
        # 启动GUI 验证 password

    def set_pwd(self, pwd):
        self.pwd = pwd
        print(self.pwd)

    def select_path(self):
        self.path = QFileDialog.getExistingDirectory()
        if not os.path.exists(self.path+'/main.py'):
            os.system('cp ./libs/main.py %s' % self.path)
        self.setWindowTitle('1ZLAB/EzEsp--->%s' % self.path.split('/')[-1])
        try:
            os.system('code %s' % self.path)
        except:
            pass
        # return path

    # def sniff_ip(self):
    #     while self.sniffer.hasPendingDatagrams():
    #         msglist = self.sniffer.readDatagram(5555)
    #         print(msglist)
    #         msg = msglist[0].decode(encoding='utf-8')
    #         self.ui.line_edit_ip.setText(msg)
            # self.host = msg

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

                self.observer.start()

        else:
            QMessageBox.warning(self, 'Waring', '请先指定工程路径和ESP IP')

    def deploy_hotload(self):
        if not self.pwd:
            self.pwd_confirm = pwdDialog(self, 0)
            self.pwd_confirm.confirmed.connect(self.set_pwd)
            self.pwd_confirm.show()
        else:
            self.c = ConfigDialog(0, self.pwd)
            self.c.show()

    def clear_up(self):
        if not self.pwd:
            self.pwd_confirm = pwdDialog(self, 1)
            self.pwd_confirm.confirmed.connect(self.set_pwd)
            self.pwd_confirm.show()
        else:
            self.c = ConfigDialog(1, self.pwd)
            self.c.show()

    def print_logs(self, log):

        self.ui.text_browser.setText(
            self.ui.text_browser.toPlainText()+"\n"+log)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = EzEspGui()
    w.show()
    sys.exit(app.exec_())
