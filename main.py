from PyQt6 import QtWidgets, uic
import sys


class MainWindow(QtWidgets.QWidget):
    # feldern (widgets) einen Typen geben
    # dasselbe wie: self.lblErgebnis = QtWidgets.QLabel()
    lblErgebnis     : QtWidgets.QLabel
    lbl_z1          : QtWidgets.QLabel
    lbl_z2          : QtWidgets.QLabel

    lstwNumOne      : QtWidgets.QListWidget
    lstwNumTwo      : QtWidgets.QListWidget

    btnInit         : QtWidgets.QPushButton

    rdbtnAdd        : QtWidgets.QRadioButton
    rdbtnSub        : QtWidgets.QRadioButton
    rdbtnDiv        : QtWidgets.QRadioButton
    rdbtnMult       : QtWidgets.QRadioButton

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        # Lade UI-Datei und initialisiere Widgets
        uic.loadUi('main_window.ui', self)

    def on_btnInit_pressed(self):
        # reverse list: 10-0
        for i in range(10, 0 - 1, -1):
            self.lstwNumOne.addItem(str(i))

        # normal list: 0-10
        for i in range(0, 10 + 1):
            self.lstwNumTwo.addItem(str(i))

        # disable button since initializing once is enough
        self.btnInit.setDisabled(True)

    def update_calc(self):
        if not self.lstwNumOne.currentItem():
            self.lblErgebnis.setText("keine erste Zahl gewählt")
            return

        if not self.lstwNumTwo.currentItem():
            self.lblErgebnis.setText("keine zweite Zahl gewählt")
            return

        # Note(Freemaker):
        # ich hasse Python
        # warum darf ich die Bedingung nicht auf mehre Zeilen schreiben
        # fucking whitespace sensitive my ass
        # und nach der funktionalität von Radioknöpfen ist es sowieso nicht möglich
        # aber es ist gefordert :/

        # Note(n0ffie): Is halt so. fuckt mich auch ab...
        if not self.rdbtnAdd.isChecked() and not self.rdbtnSub.isChecked() and not self.rdbtnDiv.isChecked() and not self.rdbtnMult.isChecked():
            self.lblErgebnis.setText("Keine Operation gewählt")
            return

        z1 = int(self.lstwNumOne.currentItem().text())
        z2 = int(self.lstwNumTwo.currentItem().text())

        if z2 == 0 and self.rdbtnDiv.isChecked():
            self.lblErgebnis.setText("Division durch 0 nicht möglich")
            return

        result = 0
        rest = 0
        if self.rdbtnAdd.isChecked():
            result = z1 + z2
        elif self.rdbtnSub.isChecked():
            result = z1 - z2
        elif self.rdbtnDiv.isChecked():
            result = z1 // z2
            rest = z1 % z2
        elif self.rdbtnMult.isChecked():
            result = z1 * z2

        if rest != 0:
            self.lblErgebnis.setText("Ergebnis: " + str(result) + "  Rest: " + str(rest))
        else:
            self.lblErgebnis.setText("Ergebnis: " + str(result))


    def on_lstwNumOne_currentItemChanged(self):
        self.update_calc()

    def on_lstwNumTwo_currentItemChanged(self):
        self.update_calc()

    # nicht gefordert update kalkulation, auch wenn anderer Radioknopf ausgewählt wird
    def on_rdbtnAdd_clicked(self):
        self.update_calc()

    def on_rdbtnSub_clicked(self):
        self.update_calc()

    def on_rdbtnDiv_clicked(self):
        self.update_calc()

    def on_rdbtnMult_clicked(self):
        self.update_calc()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
