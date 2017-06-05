__author__ = 'HICC2'
from pdfG import *
if (Base.ne>12):
    N_P=("1/2")
else:
    N_P=("1/1")

nombre_archivo=(str(a.year)+b+str(a.day)+"-ST-001"+".pdf")
dos=Base(nombre_archivo,N_P,str(Base.ne),hora,dia)
dos.invocarPdf()
startfile(nombre_archivo)

