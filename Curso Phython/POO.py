# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:53:04 2022

@author: adria
"""

#POO
#Programacion orientada a objetos

#Acciones
#Atributos / propiedades
"""
class Telefono():
    #clase que reprecenta un telefono
    
    def __init__  (self,t,camaras,numero_IMEI,SO,s_h,modelo,color): #constructor que recibe variables
   
        self. tamaño = t
        self.camaras = camaras
        self.numero_IMEI = numero_IMEI
        self.sensor_huella = s_h
        self.sistema_operativo = SO
        self.modelo = modelo
        self.color = color
        self.sonido = False
    

    def llamada(self):
        print("El telefono esta llamando")
        
    def camara(self):
        print("Se esta tomando una fotografia")
        
    def camara_video(self):
        print("Se esta tomando un video")
        
    def mensaje(self):
        print("se esta mandando un mensaje")
        
    def alterar_sonido(self):
        if self.sonido == False:
            self.sonido = True
        if self.sonido == True:
            self.sonido = False
            
            
        

miTelefono = Telefono(6.5,2,1234567890,"Android",True,"Samsung","negro")

miTelefono.llamada()

print(miTelefono.tamaño)
print(miTelefono.camaras)
print(miTelefono.numero_IMEI)
print(miTelefono.sistema_operativo)
print(miTelefono.sensor_huella)
print(miTelefono.modelo)
print(miTelefono.color)

class Telefono_chiquito(Telefono):
    def __init__ (self,t,camaras,numero_IMEI,SO,s_h,modelo,color,bt):
        super().__init__(t, camaras, numero_IMEI, SO, s_h, modelo, color)
        self.bluetooth = bt
        
    def alterar_bluetooth(self):
         if self.bluetooth == False:
            self.bluetooth= True
         if self.bluetooth == True:
            self.bluetooth= False
    pass

class Radio():
    
    def transmitir_señal(self):
        print("Enviando señal...")
        
    def sintonizar_señal(self):
        print("Recibiendo señal...")



miRadio = Radio()


#miRadio.sintonizar_señal()
#miRadio.transmitir_señal()


telefono2 = Telefono_chiquito(4,1,987654321,"Android",True,"Honor","negro chiquito")
print(telefono2.tamaño)
print(telefono2.camaras)
print(telefono2.numero_IMEI)
print(telefono2.sistema_operativo)
print(telefono2.sensor_huella)
print(telefono2.modelo)
print("el estado 1 es:" , telefono2.bluetooth)

telefono2.alterar_bluetooth()
print("El metodo 2, despues de ejevutar el metodo es ", telefono2.bluetooth)

"""


#Objeto que se guarda en memoria

lista= [1,2,3,4,5]

print (lista)
lista.append(20)
print(lista)
lista.pop(1)
print(lista)


lista =[120,35,467,67,45]
print (lista)
lista.sort()
print(lista)







