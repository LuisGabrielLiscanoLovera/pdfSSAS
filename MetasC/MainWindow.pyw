# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel

from PyQt5 import uic #carga el archivo ui del designer
from PyQt5.QtGui import QFont#el tipo de fuente
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QPainter ,QPixmap



import ctypes #getSystemnMetrics
#class constructor de ventanas
class Ventana(QMainWindow):
    #metodo constructor
    def __init__(self):        
        #iniciar el objeto QMainWindows
        QMainWindow.__init__(self)
        label = QLabel(self)
        pixmap = QPixmap('fondo5.jpg')
        label.setPixmap(pixmap)
        
        #cargar configuraciones
        uic.loadUi("MainWindow.ui",self)
        self.setWindowTitle("Cambiando el titulo de lla ventana")
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'fondo5.jpg')
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        qp.drawPixmap(QRect(0, 0, 1280, 720), pixmap)
        
        
        
        #mostrar la ventana maximizada
        self.showMaximized()
        #fijar el tamaño de la ventana
        #tamaño minimo
        self.setMinimumSize(500,500)
        self.setMaximumSize(500,500)
        #mover la ventana y centrarla en el escritorio
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(self.frameSize().width()/2)
        top=(resolucion_alto/2)-(self.frameSize().height()/2)        
        print (str(left)+"<--left//alto-->"+str(top))
        print (str(left*2)+"<--left//alto-->"+str(top*2))
        self.move(left,top)
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
