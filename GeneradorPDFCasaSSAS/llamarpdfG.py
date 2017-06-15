__author__ = 'Luis Liscano'
from os import startfile
from pdfG import *
ce=int(input("cantidad de equipos ?=:"))
cadena=input("cadena=:")
Base.equiposE=range(ce)
Base.ne=ce
if (Base.ne>12):
    N_P=("1/2")
else:
    N_P=("1/1")
nombre_archivo=(str(a.year)+b+str(a.day)+"-ST-001"+".pdf")
dos=Base(nombre_archivo,N_P,str(Base.ne),hora,dia,cadena,str("luis"))
dos.invocarPdf()
startfile(nombre_archivo)

