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
        self.resize(80,60)
        #self.setMinimumSize(600,600)
        #self.setMaximumSize(600,600)
        self.setWindowTitle("Pdf SSAS")
        self.etiquetaS=QLabel(self)
        #self.textbox = QLineEdit(self)
        uic.loadUi("ui/generandopdf.ui",self)
        self.setWindowTitle("Servicio Tecnico SSAS 1")
        """self.boton = QPushButton("soy el dialogo 1", self)
        self.boton.resize(150, 40)
        self.boton.move(400 / 2 - 150 / 2, 200 / 2 - 40)"""
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'img/fondo.jpg')
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        qp.drawPixmap(QRect(0, 0, 600, 600), pixmap)
        self.boton2.clicked.connect(self.buttonClicked)
    def buttonClicked(self):

        print ("Estoy aqui")
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
        self.resize(440,290)
        self.dialogo=Dialogo()
        self.cantidadE.valueChanged.connect(self.validar_cantidadE)
        self.cadena.textChanged.connect(self.validar_cadena)

        #self.salir.clicked.connect(self.close)

        self.boton.clicked.connect(self.capturarValores )
        self.boton.clicked.connect(QCoreApplication.instance().quit)





    def validar_cadena(self):
        cadena=self.cadena.text()
        validar=re.match('^[a-z\]ñ]+$', cadena, re.I)
        #validar=re.match('^[farmatodo,unicasa\]ñ]+$', cadena, re.I)
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
        print (self.validar_cantidadE())
        print(self.validar_cadena())

        if self.validar_cadena():
            seriales=range(self.validar_cantidadE())
            self.dialogo.acomodo =QVBoxLayout(self)
            #self.dialogo.acomodo.alignment(self)


            for i in seriales:

                self.dialogo.i=QLineEdit(self.dialogo)
                #self.dialogo.i.move(100,25*i)
                self.dialogo.i.resize(60,60)
                self.dialogo.i.setPlaceholderText("serial: "+str(1+i))
                self.dialogo.acomodo.addWidget(self.dialogo.i)


            self.dialogo.setLayout(self.dialogo.acomodo)
            self.dialogo.exec_()






        else:
            QMessageBox.warning(self,"Ingrese datos Validppo","Validacion incorrectaaaa", QMessageBox.Discard)

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
        self.setMinimumSize(440,290)
        self.setMaximumSize(440,290)



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
