import sys, re
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5 import uic


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("validacion.ui",self)
        self.nombre.textChanged.connect(self.validar_nombre)
        self.email.textChanged.connect(self.validar_email)
        self.boton.clicked.connect(self.validar_formulario)
    
    
    
    
    def validar_nombre(self):
        nombre = self.nombre.text()
        validar=re.match('^[a-z\]ñ]+$', nombre, re.I)
        if nombre =="":
            self.nombre.setStyleSheet("border:1px solid yellow;")
            return False
        elif not validar:
            self.nombre.setStyleSheet("border:1px solid red;")
            return False
        else:
            self.nombre.setStyleSheet("border:1px solid green;")
            return True
        
    
    
    
    
    
    
    
    
    
    
    def validar_email(self):
        email = self.email.text()
        validar=re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email,re.I)
        if email =="":
            self.email.setStyleSheet("border:1px solid yellow;")
            return False
        elif not validar:
            self.email.setStyleSheet("border:1px solid red;")
            return False
        else:
            self.email.setStyleSheet("border:1px solid green;")
            return True
        
    def validar_formulario(self):
        if self.validar_nombre()and self.validar_email():
            QMessageBox.warning(self,"Formulario correcta","Validacion correcta", QMessageBox.Discard)
        else:
            QMessageBox.warning(self,"Formulario Incorrecto","Validacion incorrecta", QMessageBox.Discard)
app=QApplication(sys.argv)

dialogo =Dialogo()
dialogo.show()
app.exec_()

            
            
            
            
            
            
            
            
            
            
            
            
            