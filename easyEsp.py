#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from libs.ui_app import Ui_Dialog
import sys
import os


class EzEspGui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.is_not_start = True
        self.path = ''
        self.init_view()
        self.init_connection()

    def init_view(self):
        self.setWindowTitle('1ZLAB/EzEsp')
        coms = [i for i in os.listdir('/dev/') if i.startswith('ttyUSB')]
        self.ui.combo_box_com.addItems(coms)

    def init_connection(self):
        self.ui.button_path.clicked.connect(self.select_path)
        self.ui.button_start.clicked.connect(self.start_hot_load)

    def select_path(self):
        self.path = QFileDialog.getExistingDirectory()
        self.setWindowTitle('1ZLAB/EzEsp--->%s' % self.path.split('/')[-1])
        # return path

    def start_hot_load(self):
        if self.path:
            self.ui.combo_box_com.setEnabled(not self.is_not_start)
            self.ui.button_path.setEnabled(not self.is_not_start)
            self.is_not_start = not self.is_not_start
            if self.is_not_start:
                self.ui.button_start.setText('Start')
            else:
                self.ui.button_start.setText('Stop')

        else:
            QMessageBox.warning(self, 'Waring', '请先指定工程路径')

    def get_params(self):
        if not is_not_start:
            return self.ui.combo_box_com.currentText(), self.path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = EzEspGui()
    w.show()
    sys.exit(app.exec_())
