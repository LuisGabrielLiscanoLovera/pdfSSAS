#coding: utf-8
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from reportlab.lib.pagesizes import letter, A4
from datetime import datetime as t
from os import startfile
a=t.now()

if (a.month <10):
    b=("0"+str(a.month))
else:
    b=str(a.month)
dia="[ "+str(a.day)+"/"+b+"/"+str(a.year)+" ]"
min=a.minute
if (min <10):
    min="0"+str(a.minute)
hora="[ "+str(a.hour)+":"+str(min)+":"+str(a.second)+" ]"#hora 24H
class Base:
    ne=int(input("cuanto esquipos ?"))
    equiposE=range(ne)
    def __init__(self,nombreA,np,ne,h,d):
        #self.color=cl
        self.nombre_archivo=nombreA
        self.N_P=np
        self.N_E=ne
        self.hora=h
        self.dia=d

    def invocarPdf(self):
      c=canvas.Canvas(self.nombre_archivo)
      def BasePdf():
        c.drawImage("img/LM.png", 30, 740, 80, 80,preserveAspectRatio=True)
        c.drawImage("img/logoCASA.png", 475, 740, 80, 80,preserveAspectRatio=True)
        c.setFont('Helvetica',7)
        c.drawString(120,810,"REPÚBLICA BOLIVARIANA DE VENEZUELA MINISTERIO DEL PODER POPULAR PARA ALIMENTACIÓN")
        c.drawString(180,795,"CORPORACIÓN DE ABASTECIMIENTO Y SERVICIOS AGRÍCOLAS")
        c.drawString(160,780,"GERENCIA DE SISTEMA SUPERIOR DE ABASTECIMIENTO SEGURO (GSSAS)")
        c.drawString(270,765,"MARICHES")
        c.setFont('Helvetica',17)
        c.drawString(100+50,810-70,"Servicio Técnico / Nota de Entrega")
      #-----------------------------------------------------------------------------------------------------------------------
                                              #Numero de control
        c.setFont('Helvetica',12)
        c.rect(360,682,220,30)
        c.drawString(365,686,"Fecha de Elaboración:      "+self.dia)#***************finish
        c.drawString(365,700,"Número de Control:   "+str(a.year)+b+str(a.day)+"-ST-")#<------------------------------------------------fata
        c.setFont('Helvetica',9)
        c.drawString(540,673,"PAG  "+self.N_P)#<------------------------------------------------fata
        #-----------------------------------------------------------------------------------------------------------------------
                                                #codigo de cadena
        c.setFont('Helvetica',10)
        c.drawString(30,705,"Código: PRI-00032")#<------------------------------------------------fata
        c.drawString(30,690,"Cadena: FARMATODO")#<------------------------------------------------fata
        #------------------------------------------------------------------------------------------------------------
                                               # lines and rect
        c.setFillColor(gray)
        #linias dvicion cuadro iz
        c.line(30,430,30,632)
        c.line(50,430,50,632)
        c.line(100,430,100,632)
        c.line(210,430,210,632)
        c.line(225,430,225,632)
        c.line(240,430,240,632)
        c.line(255,430,255,632)
        c.line(270,430,270,632)
        c.line(285,430,285,632)
        c.line(300,430,300,632)
        #linias dvicion cuadro derecho
        c.line(310,430,310,632)
        c.line(333,430,333,632)
        c.line(356,430,356,632)
        c.line(376,430,376,632)
        c.line(399,430,399,632)
        c.line(421,430,421,632)
        c.line(443,430,443,632)
        c.line(465,430,465,632)
        c.line(487,430,487,632)
        c.line(509,430,509,632)
        c.line(531,430,531,632)
        c.line(580,430,580,632)
        c.line(30,430,580,430)#ultima linia horizontal
        c.rect(210,395,206,15,fill=1)#cantida de equipos enatregados
        c.rect(310,650,270,20,fill=1)#cuadro derecha
        c.rect(310,632,270,15,fill=1)#INDIQUE LA FALLA DEL EQUIPO
        c.rect(310,617,23,15,fill=1)#PAN
        c.rect(333,617,23,15,fill=1)#LEC
        c.rect(356,617,23,15,fill=1)#SOF
        c.rect(376,617,23,15,fill=1)#TEC
        c.rect(399,617,23,15,fill=1)#FAN
        c.rect(421,617,23,15,fill=1)#ELE
        c.rect(443,617,23,15,fill=1)#DD
        c.rect(465,617,23,15,fill=1)#MEM
        c.rect(487,617,23,15,fill=1)#TAR
        c.rect(509,617,23,15,fill=1)#LIC
        c.rect(531,617,49,15,fill=1)#CAM
        c.rect(30,650,270,20,fill=1)#header information
        c.rect(30,617,20,30,fill=1)#label N°
        c.rect(50,617,50,30,fill=1)#equipo
        c.rect(100,617,110,30,fill=1)#serial equipo
        c.rect(210,632,30,15,fill=1)#CAR
        c.rect(210,617,15,15,fill=1)#S
        c.rect(225,617,15,15,fill=1)#N
        c.rect(240,632,30,15,fill=1)#CAB
        c.rect(240,617,15,15,fill=1)#s
        c.rect(255,617,15,15,fill=1)#N
        c.rect(270,632,30,15,fill=1)#CAJA
        c.rect(270,617,15,15,fill=1)#N
        c.rect(285,617,15,15,fill=1)#S
        c.rect(30,270,550,40)#leyenda
        c.line(35,338,575,338)#linias de observaciones
        c.line(35,323,575,323)#linias de observaciones
        c.rect(550,360,10,10)#generar no entrega
        #ENTREGA y DEVOLUCION
        c.rect(30,170,550,100)#RECTANGULO 1
        c.rect(30,260,550,15, fill=1)
        c.rect(30,70,550,100)#RECTANGULO 2
        c.rect(30,155,550,15, fill=1)
        #---------------------------------------Texto de del cuadro Izquierdo y dere ----------------------------------
        c.setFillColor(black)
        c.drawString(35,655,"INFORMACIÓN                                          ACCESORIOS")
        c.drawString(35,627,"N°")
        c.drawString(56,627,"EQUIPO")
        c.drawString(105,628,"SERIAL DEL EQUIPO")
        c.drawString(350,655,"DEPARTAMENTO DE SOPORTE TÉCNICO")
        c.drawString(385,635,"INDIQUE LA FALLA DEL EQIPO")
        c.drawString(212,399,"CANTIDAD DE HICC  ENTREGADOS: "+str(self.N_E))#+"/")+str(self.N_E))#Cantidad de equipos entregados
        c.setFont('Helvetica',8)
        c.drawString(216,635,"CAR")
        c.drawString(215,620,"S")
        c.drawString(230,620,"N")
        c.drawString(246,635,"CAB")
        c.drawString(245,620,"S")
        c.drawString(260,620,"N")
        c.drawString(276,635,"CAJA")
        c.drawString(275,620,"S")
        c.drawString(288,620,"N")
        c.drawString(313,620,"PAN")
        c.drawString(336,620,"LEC")
        c.drawString(358,620,"SOF")
        c.drawString(379,620,"TEC")
        c.drawString(401,620,"FAN")
        c.drawString(423,620,"ELE")
        c.drawString(445,620,"HDD")
        c.drawString(467,620,"MEM")
        c.drawString(489,620,"TAR")
        c.drawString(513,620,"LIC")
        c.drawString(538,620,"CAMBIO")
        c.drawString(35,340,"OBSERVACIONES:")
        c.drawString(357,363,"Generar Nota de Entrega de Cambios por Garantia")
        c.drawString(35,300,"LEYENDA DE FALLAS:  PAN:Pantalla  LEC:Lectora  SOF:software  TEC: Teclado  FAN:Ventilador  ELE:Corriente  HDD:Disco duro")#leyenda
        c.drawString(35,285,"MEN:Memoria  TAR:Tarjeta  LIC:Licencia  CAMBIO: Cambio de equipo HICC")
        #recivo
        c.drawString(230,265,"RECEPCION DEL EQUIPO PARA REVISIÓN")
        c.drawString(35,243,"Entregado por:    Nombre y Apellido:  _________________                              Recibido por:    Nombre y apellido:  _______________")
        c.drawString(35,223,"Cédula:  _______________         Telf:_________________                              Cédula:  _______________       Telf:______________")
        c.drawString(35,203,"Fecha:  "+self.dia)
        c.drawString(346,203,"Fecha:  "+self.dia)
        c.drawString(35,185,"Hora:    "+self.hora)
        c.drawString(346,185,"Hora:    "+self.hora)
        c.drawString(150,185,"       Firma: _______________                                                                            Firma: _______________")
        c.drawString(230,160,"ENTREGA Y/O DEVOLUCIÓN DEL EQUIPO")
        c.drawString(100,45,"Solo para ser llenado por la Gerencia de Sistema Superior de Abastecimiento Seguro (GSSAS)Autorizado por:")
        c.drawString(70,25,"Nombre Y apellido: _______________________  Fecha: "+self.dia+"  Hora: "+self.hora+"  Firma:__________________________")
        #entrega
        c.drawString(35,142,"Entregado por:    Nombre y Apellido:  _________________                              Recibido por:    Nombre y apellido:  _______________")
        c.drawString(35,122,"Cédula:  _______________         Telf:_________________                              Cédula:  _______________       Telf:______________")
        c.drawString(35,102,"Fecha:  [     /     /     ]                                                                                            Fecha:  [     /     /     ]")
        c.drawString(150,85,"       Firma: _______________                                                                            Firma: _______________")
        c.setFillColor(white)
        c.rect(300,430,10,240,fill=1)#Horizontal que borra linesas intermedio
        c.showPage()
      for i in self.equiposE:
       i*=15
       c.setFont("Helvetica",10)
       c.line(30,595-i,580,595-i)
       c.drawString(35,598-i,""+str(round((i/15)+1)))
       c.drawString(60,598-i,"HICC")
       c.drawString(102,598-i,"GWRHICC0000"+input("serial 1:"))
       '''if (ne>12):
         self.N_E=str(round(i/15)+1)
         print(self.N_E)'''
       if (i==165):
         break
      if (self.ne>12):
        BasePdf()
        self.N_P=("2/2")
      for i in self.equiposE:
        i*=15
        if(i>165):
          c.setFont("Helvetica",10)
          c.line(30,775-i,580,775-i)
          c.drawString(102,780-i,"GWRHICC0000"+input("serial 2:"))
          c.drawString(60,780-i,"HICC")
          c.drawString(35,780-i,""+str(round((i/15)+1)))
          #self.N_E=str(round(i/15)-11)
      BasePdf()
      c.save()
