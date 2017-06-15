__author__ = 'Luis Liscano'
import sys,re
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QDialog,QMessageBox,QLineEdit,QPushButton, QVBoxLayout
from PyQt5 import uic #carga el archivo ui del designer
from PyQt5.QtGui import QFont,QIcon#el tipo de fuente
from PyQt5.QtCore import Qt,QRect,QCoreApplication
from PyQt5.QtGui import QPainter ,QPixmap

from os import startfile
from pdfG import *



#import ctypes #getSystemnMetrics

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #self.resize(600/2,600)
        #self.setMinimumSize(600/2,600)
        #self.setMaximumSize(600/2,600)
        self.setWindowTitle("Pdf SSAS")
        self.etiquetaS=QLabel(self)
        #self.textbox = QLineEdit(self)
        uic.loadUi("ui/generandopdf.ui",self)
        self.setWindowTitle("Servicio Tecnico SSAS 1")
        """self.boton = QPushButton("soy el dialogo 1", self)
        self.boton.resize(150, 40)
        self.boton.move(400 / 2 - 150 / 2, 200 / 2 - 40)"""
        self.boton2.clicked.connect(self.buttonClicked)


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'img/fondo.jpg')
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        qp.drawPixmap(QRect(0, 0, 600, 600), pixmap)

    def buttonClicked(self):
        C_seriales=(self.ct)
        #ce=int(input("cantidad de equipos ?=:"))
        cadena="cadena"
        Base.equiposE=range(C_seriales)
        Base.ne=C_seriales
        if (Base.ne>12):
            N_P=("1/2")
        else:
            N_P=("1/1")
        nombre_archivo=(str(a.year)+b+str(a.day)+"-ST-001"+".pdf")





        dos=Base(nombre_archivo,N_P,str(Base.ne),hora,dia,cadena,str("luis"))
        dos.invocarPdf()
        startfile(nombre_archivo)

        C_seriales=range(self.ct)
        for i in (C_seriales):
            print(self.lista[i].text())








#class constructor de ventanas
class Ventana(QMainWindow):
    #metodo constructor
    def __init__(self):        
        #iniciar el objeto QMainWindows
        QMainWindow.__init__(self)
        label = QLabel(self)
        pixmap = QPixmap()
        label.setPixmap(pixmap)        
        #cargar configuraciones del disigner
        uic.loadUi("ui/main.ui",self)
        self.cadena.setPlaceholderText("Cadena")
        self.setWindowIcon(QIcon("img/logoCasa.png"))

        #self.salir=QPushButton("salir",self)
        #self.salir.move(0,50)

        self.setWindowTitle("Generador de Nota Servicio Tecnico SSAS ")
        self.resize(420,315)
        self.setMinimumSize(420,315)
        self.setMaximumSize(420,315)
        self.dialogo=Dialogo()
        self.cantidadE.valueChanged.connect(self.validar_cantidadE)
        self.cadena.textChanged.connect(self.validar_cadena)

        #self.salir.clicked.connect(self.close)

        self.boton.clicked.connect(self.capturarValores )
        #self.boton.clicked.connect(QCoreApplication.instance().quit)





    def validar_cadena(self):
        cadena=self.cadena.text()
        validar=re.match('^[a-z \]ñ]+$', cadena, re.I)
        if cadena =="":
            self.cadena.setStyleSheet("border:1px solid yellow;")
            return False
        elif not validar:
            self.cadena.setStyleSheet("border:1px solid red;")
            return False
        else:
            self.cadena.setStyleSheet("border:1px solid green;")
            return True and cadena

    def validar_cantidadE(self):
        cantidadE=self.cantidadE.value()
        return cantidadE

    def capturarValores(self):
        """print(self.cadena.text())
        print(self.cadena2.text())
        print(self.cadena3.text())
        print(self.cadena4.text())
        print(self.cadena5.text())"""

        if self.validar_cadena():
            seriales=range(self.validar_cantidadE())
            self.dialogo.resize(300,650)
            self.dialogo.lista = []
            for i in seriales:
                i+=1

                self.dialogo.i=QLineEdit(self.dialogo)
                self.dialogo.i.move(15,25*i)
                self.dialogo.i.resize(130,30)
                self.dialogo.i.setPlaceholderText("serial: "+str(i))
                self.dialogo.i.setMaxLength(16)
                self.dialogo.lista.append(self.dialogo.i)


                #print(self.dialogo.i)

                #print(self.dialogo.lista)

            #print("desde qui")
            #print(self.dialogo.lista)
            self.dialogo.ct=i
            self.dialogo.exec_()


        else:
            QMessageBox.warning(self,"Ingrese datos Valido","Validacion incorrecta", QMessageBox.Discard)

        '''serialU="desarrollo"
        ce=(self.validar_cantidadE())
        cadena=self.validar_cadena()
        Base.equiposE=range(ce)
        Base.ne=ce
        if (Base.ne>12):
            N_P=("1/2")
        else:
            N_P=("1/1")
        nombre_archivo=(str(a.year)+b+str(a.day)+"-ST-001"+".pdf")
        dos=Base(nombre_archivo,N_P,str(Base.ne),hora,dia,cadena,serialU)
        dos.invocarPdf()
        startfile(nombre_archivo)
        '''
        #print (self.validar_cantidadE())
       # print(self.validar_cadena())






    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'img/fondo2.jpeg')
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        #qp.drawPixmap(QRect(90,90, 175,175), pixmap)
        #mostrar la ventana maximizada
        #self.showMaximized()
        #fijar el tamaño de la ventana
        #tamaño minimo




        #mover la ventana y centrarla en el escritorio


        """resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(self.frameSize().width()/2)
        top=(resolucion_alto/2)-(self.frameSize().height()/2)        
        print (str(left)+"<--left//alto-->"+str(top))
        print (str(left*2)+"<--left//alto-->"+str(top*2))
        self.move(left,top)"""
        #Desactivar la ventana
        #self.setEnabled(True)    
        #Asignar un tipo de fuente
        qfont=QFont("Rockwell Condensed",12,QFont.Bold)
        self.setFont(qfont)        
        #Asignar un tipo de cursor
        self.setCursor(Qt.PointingHandCursor)
        #Asignando Estilops CSS
        #self.setStyleSheet("background-color:#262626; color:#fff;")        
       # self.boton.setStyleSheet("background-color; color:#fff;font-size:26px;radius:20px solid 10px;")
     
        
        

        
#Instancia para iniciar la app
app=QApplication(sys.argv)
#crear un objeto de la clase
_ventana=Ventana()
#Mostrar ventanaas
_ventana.show()
#ejecutamos la app
app.exec_()
