import sys
from PyQt5 import uic, QtWidgets
import matplotlib.pyplot as plt

qtCreatorFile = "P1_MenuBar.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.actionAbrir_Widget_2.triggered.connect(self.widget)
        self.actionAbrir_Dialog_2.triggered.connect(self.dialog)
        self.actionSalir.triggered.connect(self.salir)
        self.actionAcerca.triggered.connect(self.acerca)
        self.convertir.clicked.connect(self.accion)


        self.cb_grados.addItem("Fahrenheit", 0)
        self.cb_grados.addItem("Celsius", 1)
        self.cb_grados.addItem("Kelvin", 2)

        self.lw_grados.addItem("Fahrenheit")
        self.lw_grados.addItem("Celsius")
        self.lw_grados.addItem("Kelvin")
        self.lw_grados.currentRowChanged.connect(self.cambioFila)

        self.conversion.setText("0")
        self.valor.setText("0")
        self.list = 0

    def accion(self):
        valor=int(self.valor.text())
        combo = self.cb_grados.currentData()
        if combo != self.list:
            if self.list == 0 and combo == 1:#F -> C
                self.conversion.setText(str("{0:.2f}".format((valor-32)/1.8)))
            elif self.list == 0 and combo == 2:  # F -> K
                self.conversion.setText(str("{0:.2f}".format(5/9*(valor-32) + 273.15)))
            elif self.list == 1 and combo == 0:#C -> F
                self.conversion.setText(str("{0:.2f}".format(valor*1.8+32)))
            elif self.list == 1 and combo == 2:#C -> K
                self.conversion.setText(str("{0:.2f}".format(valor+273.15)))
            elif self.list == 2 and combo == 0:#K -> F
                self.conversion.setText(str("{0:.2f}".format(1.8*(valor-273.15)+32)))
            elif self.list == 2 and combo == 1:#K -> C
                self.conversion.setText(str("{0:.2f}".format(valor-273.15)))
        else:
            self.conversion.setText(str(valor))

    def cambioFila(self):
        self.list = self.lw_grados.currentRow()

    def widget(self):
        self.mensaje("Abriste un Widget")

    def dialog(self):
        self.mensaje("Abriste un Dialog")

    def salir(self):
        sys.exit()

    def acerca(self):
        self.mensaje("Acerca de ♥")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
