from PyQt5.QtWidgets import QApplication
from app.dialog_main import EasyEsp
import sys



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = EasyEsp()
    w.show()
    sys.exit(app.exec_())