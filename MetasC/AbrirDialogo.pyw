import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPainter ,QPixmap
from PyQt5.QtCore import QCoreApplication,QRect
class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(300,300)
        self.setWindowTitle("Cuadro de dialogo")
        self.etiqueta=QLabel(self)
        uic.loadUi("Stylecss.ui",self)
        
        
        
class Ventana(QMainWindow):    
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600,600)
        self.boton=QPushButton(self)
        self.boton.setText("abrir cuadro de dialog?")
        self.boton.resize(600,30)
        self.dialogo=Dialogo()        
        self.boton.clicked.connect(self.abrirDialogo)
        self.boton.clicked.connect(QCoreApplication.instance().quit)
   
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'fondo5.jpg')
    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        qp.drawPixmap(QRect(0, 0, 1280, 720), pixmap)
        
        
        
    def abrirDialogo(self):
        self.dialogo.etiqueta.setText("Dialogo abierto desde la ventana principal")
        self.dialogo.exec_()
app=QApplication(sys.argv)
ventana=Ventana()
ventana.show()
app.exec_()