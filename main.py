from PyQt6 import QtWidgets, uic, QtCore
import sys


class MainWindow(QtWidgets.QWidget):

    # feldern (widgets) einen Typen geben
    # dasselbe wie: self.lbl_ergebnis = QtWidgets.QLabel()
    lbl_ergebnis: QtWidgets.QLabel
    lbl_z1: QtWidgets.QLabel
    lbl_z2: QtWidgets.QLabel
    liWi_z1: QtWidgets.QListWidget
    liWi_z2: QtWidgets.QListWidget
    pBtn_init: QtWidgets.QPushButton
    rBtn_add: QtWidgets.QRadioButton
    rBtn_sub: QtWidgets.QRadioButton
    rBtn_div: QtWidgets.QRadioButton
    rBtn_multi: QtWidgets.QRadioButton

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        uic.loadUi('main_window.ui', self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
