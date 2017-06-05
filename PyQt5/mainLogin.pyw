import sys,re
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QDialog,QPushButton
from PyQt5 import uic #carga el archivo ui del designer
from PyQt5.QtGui import QFont#el tipo de fuente
from PyQt5.QtCore import Qt,QRect, QCoreApplication
from PyQt5.QtGui import QPainter ,QPixmap

#import ctypes #getSystemnMetrics

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(600,600)
        self.setMinimumSize(600,600)
        self.setMaximumSize(600,600)

        self.setWindowTitle("Pdf SSAS")
        self.etiqueta=QLabel(self)
        uic.loadUi("generandopdf.ui",self)
        self.setWindowTitle("Servicio Tecnico SSAS ")

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'dondo.jpg')
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        qp.drawPixmap(QRect(0, 0, 600, 600), pixmap)
      
        
        #boton = QPushButton("Button 1", self)
        #boton1.resize(150, 40)
        #btn1.move(400 / 2 - 150 / 2, 200 / 2 - 40)
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
        uic.loadUi("main.ui",self)
        self.cadena.setPlaceholderText("Cadena")
        
        self.setWindowTitle("Generador de Nota Servicio Tecnico SSAS ")
        self.resize(440,290)
        self.dialogo=Dialogo()
        
        self.cadena.textChanged.connect(self.validar_cadena)
        self.boton.clicked.connect(self.abrirDialogo)
        self.boton.clicked.connect(QCoreApplication.instance().quit)        
        
    def validar_cadena(self):
        cadena=self.cadena.text()
        validar=re.match('^[a-z\]ñ]+$', cadena, re.I)
        print(cadena)

    def abrirDialogo(self):
        #self.dialogo.etiqueta.setText("generandor de reporte asistencia Tecnica")
        print("desde dialogo")
        self.dialogo.exec_()
    """def validar_cantidad_equipo(self):
        cantidadE2 = self.validar_cantidad_equipo.text()
        validar=re.match('^[a-z\]ñ]+$', cantidadE2, re.I)
        return print (self.cantidadE2)"""

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'f.jpeg')
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
