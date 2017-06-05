import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,QPushButton,QDialog)
from PyQt5.QtGui import QPixmap

from PyQt5 import uic
class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.resize(300,300)
        self.setWindowTitle("Cuadro de dialogo")
        self.etiqueta=QLabel(self)
        uic.loadUi("Stylecss.ui",self)

class Example(QWidget):    
    def __init__(self):
        super().__init__()
        self.title='Luis Liscano'
        self.left = 10
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap('fondo.jpg')
        label.setPixmap(pixmap)
        self.resize(600,600)
        self.boton=QPushButton(self)
        self.boton.setText("abrir cuadro de dialog?")
        self.boton.resize(600,30)
        self.dialogo=Dialogo()
        self.boton.clicked.connect(self.abrirDialogo)
    def abrirDialogo(self):
        self.dialogo.exec_()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())