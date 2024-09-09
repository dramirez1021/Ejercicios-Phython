# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:10:10 2022

@author: adria
"""

numero_actual  = 0
numero_par = 0
numero_prim = 0
contador = 0
numero_modulo = 2
"""
while (numero_actual <= 10000):
    if numero_actual % 2 == 0:
      numero_par = numero_actual
    numero_actual += 1
"""   
while (numero_actual <= 100):
   
    if numero_actual <= 1 :
       numero_actual += 1
    elif numero_actual == 2:
        numero_prim = numero_actual
        numero_actual += 1
    else:
        while numero_modulo < numero_actual:
            if numero_actual % numero_modulo == 0:
               numero_modulo += 1
               contador += 1 
            else:
                numero_modulo += 1
        if contador == 0 :
                numero_prim = numero_actual
        numero_actual +=1
        numero_modulo = 2
        contador = 0
    
        