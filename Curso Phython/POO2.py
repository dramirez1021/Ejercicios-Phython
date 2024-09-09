# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:42:09 2022

@author: adria
"""


class Telefono():
    
    __numero_telefonico = 5521318967
    
    def llamada(self):
        print("Estoy haciendo una llamada a otro dispositivo")
    def __nmap (self):
        print("estoy escaneando los puertos de otro dispositivo")
        
    def ejecutra_nmap(self):
        self.__nmap()
    def get_numero_telefonico(self):
        return self.numero_telefonico
    def set_numero_telefonico(self,numero_nuevo):
        self.__numero_telefonico = numero_nuevo


class Tablet():
    
    def llamada (self):
        print("estoy haciendo una llamada a otro dispositivo")
        
dispositivo1 = Telefono()
dispositivo1.llamada()
dispositivo1.ejecutra_nmap()

dispositivo1.set_numero_telefonico(5529106592)
print("Nuevo numeror:",dispositivo1.get_numero_telefonico())

class Telefono_fijo():
    def llamada (self):
        print("estoy haciendod una llamada a otro lugar")
        

class Radio():
    def llamada(self):
        print("estoy hacinedo una llamaca de radio")
        
 #polimorfismo       
def hacer_llamada (algo):
    algo.llamada()

nuevo_dispositivo = Tablet()

hacer_llamada(nuevo_dispositivo)


dispositivo2 = Tablet()

dispositivo2.llamada()