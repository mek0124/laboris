from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from pages.translated.main import Ui_w_MainWindow

import sys


class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pb_clock_in.clicked.connect(self.clock_in_user)
        self.pb_meal_out.clicked.connect(self.meal_out)
        self.pb_meal_in.clicked.connect(self.meal_in)
        self.pb_clock_out.clicked.connect(self.clock_out_user)

    def clock_in_user(self) -> None:
        print("User Clocked In")

    def meal_out(self) -> None:
        print("User Started Meal")

    def meal_in(self) -> None:
        print("User Ended Meal")

    def clock_out_user(self) -> None:
        print("User Clocked Out")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())