#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from libs.ui_app import Ui_MainWindow
from libs.ui_config import Ui_Dialog
from libs.handler import FileEventHandler
import sys
import os
import json


class ConfigDialog(QWidget):
    def __init__(self, taskcode):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_view(taskcode)
        self.init_connection()

    def init_view(self, taskcode):
        print('i am in')
        self.taskcode = taskcode
        self.com = ''
        try:
            with open('./config.json', 'r') as f:
                self.config = json.loads(f.read())
        except:
            self.config = dict(wifi_pwd='', wifi_name='', is_developing='1')

        # self.setWindowTitle(taskcode)

        coms = [i for i in os.listdir('/dev/') if i.startswith('ttyUSB')]
        self.ui.combo_box_com.addItems(coms)
        self.ui.line_edit_wifi.setText(self.config['wifi_name'])
        self.ui.line_edit_pwd.setText(self.config['wifi_pwd'])


    def init_connection(self):
        self.ui.button_deploy.clicked.connect(self.button_deploy_clicked)


    def button_deploy_clicked(self):
        self.com = '/dev/' + self.ui.combo_box_com.currentText()
        self.config['wifi_name'] = self.ui.line_edit_wifi.text()
        self.config['wifi_pwd'] = self.ui.line_edit_pwd.text()

        if self.config['wifi_name'] and self.config['wifi_pwd'] and self.com:

            with open('./config.json', 'w') as f:
                f.write(json.dumps(self.config))
            
            if self.taskcode == 0:
                for i in os.listdir('./.hotload'):
                    os.system('sudo ampy -p {0} put {1}/{2}'.format(self.com, './.hotload', i))

            else:
                os.system('sudo ampy -p {0} put {1}/{2}'.format(self.com, './.clear', 'main.py'))

            self.close()

        else:
            QMessageBox.warning(self,'waring','请将选项设置完整')



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

    def init_view(self):
        self.setWindowTitle('1ZLAB/EzEsp')


    def init_connection(self):
        self.ui.action_init_hotload.triggered.connect(self.deploy_hotload)
        self.ui.action_clean_up.triggered.connect(self.clear_up)
        self.ui.button_path.clicked.connect(self.select_path)
        self.ui.button_start.clicked.connect(self.start_hot_load)

    def select_path(self):
        self.path = QFileDialog.getExistingDirectory()
        self.setWindowTitle('1ZLAB/EzEsp--->%s' % self.path.split('/')[-1])
        # return path

    def start_hot_load(self):
        if self.path and self.ui.line_edit_ip.text():
            self.ui.combo_box_com.setEnabled(not self.is_not_start)
            self.ui.button_path.setEnabled(not self.is_not_start)
            self.ui.line_edit_ip.setEnabled(not self.is_not_start)
            self.is_not_start = not self.is_not_start
            if self.is_not_start:
                self.ui.button_start.setText('Start')
            else:
                self.ui.button_start.setText('Stop')

        else:
            QMessageBox.warning(self, 'Waring', '请先指定工程路径和ESP IP')

    def deploy_hotload(self):
        self.c =  ConfigDialog(0)
        self.c.show()

    def clear_up(self):
        self.c =  ConfigDialog(1)
        self.c.show()

        
    # host = host
    #     observer = Observer()
    #     event_handler = FileEventHandler(host)
    #     observer.schedule(event_handler, path, True)
    #     observer.start()
    #     try:
    #         while True:
    #             time.sleep(1)
    #     except KeyboardInterrupt:
    #         observer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = EzEspGui()
    w.show()
    sys.exit(app.exec_())
