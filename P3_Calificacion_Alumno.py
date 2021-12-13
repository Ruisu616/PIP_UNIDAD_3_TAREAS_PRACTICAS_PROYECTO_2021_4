import sys
import statistics as stats

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P3_Calificacion_Alumno.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.suma = 0
        self.nombremayor = ""
        self.nombremenor = ""
        self.califmayor = ""
        self.califmenor = ""
        self.listaop=[]
        ##########################################################################
        ###LEER ARCHIVO

        archivo = open("Archivos/Datos_Calificaciones.txt", "r")
        contenido = archivo.readlines()  # leer el contenido completo del archivo
        print(contenido)

        # Listas de comprensión
        self.lista = [linea.split("\t") for linea in contenido]
        print(self.lista)

        self.lista = [[registro[0], int(registro[1])] for registro in self.lista]
        print(self.lista)


        for i in self.lista:
            self.suma += i[1]
            self.listaop.append(i[1])
            self.lw_alumnos.addItem(i[0])  #se añade únicamente el nombre del alumno
            print(i[1],"osi",)
            if self.suma==8:
                self.nombremayor = i[0]
                self.nombremenor = i[0]
                self.califmayor = i[1]
                self.califmenor = i[1]
            elif self.califmayor < i[1]:
                self.nombremayor = i[0]
                self.califmayor = i[1]
            elif self.califmenor > i[1]:
                self.nombremenor = i[0]
                self.califmenor = i[1]
        for i in self.lista:
            if i[1]>=(self.suma / len(self.lista)):

                self.lw_alto.addItem(i[0]+", "+str(i[1]))
            else:
                self.lw_bajo.addItem(i[0]+", "+str(i[1]))
        self.txt_promedio.setText(str(self.suma / len(self.lista)))
        valor=float(stats.variance(self.listaop))
        self.txt_desviacion.setText(str("{0:.2f}".format(valor)))
        valor=float(stats.stdev(self.listaop))
        self.txt_varianza.setText(str("{0:.2f}".format(valor)))
        self.lw_mayor.addItem(self.nombremayor)
        self.lw_menor.addItem(self.nombremenor)
        self.txt_mayor.setText(str(self.califmayor))
        self.txt_menor.setText(str(self.califmenor))
        self.lw_alumnos.currentRowChanged.connect(self.cambioFila)


    def cambioFila(self):
        try:
            indice = self.lw_alumnos.currentRow()
            print("indice: ", indice)

            calificacion = self.lista[indice][1] #calificacion

            self.txt_calificacion.setText(str(calificacion))

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


    #Práctica. Realizar una interfaz gráfica basada en el programa 7, que permita
    # aplicar un analisis estadistico sencillo a los datos del archivo
    #
    #Añadir botones para:
    #   Obtener calificación y nombre del alumno con menor calificacion
    #   Obtener calificación y nombre del alumno con mayor calificacion
    #   Obtener calificación y nombres de los alumnos con calificacion arriba del promedio
    #   Obtener calificación y nombres de los alumnos con calificacion abajo del promedio
    #   Calcular el promedio del grupo
    #   Calcular la Desviación Estandar y Varianza del Grupo

    