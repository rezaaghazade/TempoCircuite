from GUI import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class MyClass:
    def __init__(self):
        print("init")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
