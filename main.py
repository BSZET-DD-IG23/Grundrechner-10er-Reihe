from PyQt6 import QtWidgets, uic
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

    def on_pBtn_init_pressed(self):
        # reverse list: 10-0
        for i in range(10, 0 - 1, -1):
            self.liWi_z1.addItem(str(i))

        # normal list: 0-10
        for i in range(0, 10 + 1):
            self.liWi_z2.addItem(str(i))

        # disable button since initializing once is enough
        self.pBtn_init.setDisabled(True)

    def update_calc(self):
        if not self.liWi_z1.currentItem():
            self.lbl_ergebnis.setText("keine erste Zahl gewählt")
            return

        if not self.liWi_z2.currentItem():
            self.lbl_ergebnis.setText("keine zweite Zahl gewählt")
            return

        # ich hasse Python
        # warum darf ich die Bedingung nicht auf mehre Zeilen schreiben
        # fucking whitespace sensitive my ass
        # und nach der funktionalität von Radioknöpfen ist es sowieso nicht möglich
        # aber es ist gefordert :/
        if not self.rBtn_add.isChecked() and not self.rBtn_sub.isChecked() and not self.rBtn_div.isChecked() and not self.rBtn_multi.isChecked():
            self.lbl_ergebnis.setText("keine Operation gewählt")
            return

        z1 = int(self.liWi_z1.currentItem().text())
        z2 = int(self.liWi_z2.currentItem().text())

        if z2 == 0 and self.rBtn_div.isChecked():
            self.lbl_ergebnis.setText("division durch 0 nicht möglich")
            return

        result = 0
        if self.rBtn_add.isChecked():
            result = z1 + z2
        elif self.rBtn_sub.isChecked():
            result = z1 - z2
        elif self.rBtn_div.isChecked():
            result = z1 / z2
        elif self.rBtn_multi.isChecked():
            result = z1 * z2

        self.lbl_ergebnis.setText("Ergebnis: " + str(result))

    def on_liWi_z1_currentItemChanged(self):
        self.update_calc()

    def on_liWi_z2_currentItemChanged(self):
        self.update_calc()

    # nicht gefordert update kalkulation, auch wenn anderer Radioknopf ausgewählt wird
    def on_rBtn_add_clicked(self):
        self.update_calc()

    def on_rBtn_sub_clicked(self):
        self.update_calc()

    def on_rBtn_div_clicked(self):
        self.update_calc()

    def on_rBtn_multi_clicked(self):
        self.update_calc()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
