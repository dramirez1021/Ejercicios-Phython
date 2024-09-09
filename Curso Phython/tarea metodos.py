# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:30:29 2022

@author: adria
"""

#Investigar el metodo con el que se deben re realizar los sig enunciados: 
#1) Agregar el contendio de una lista en otra lista
l1 = [1, 2, 3]
l2 = [100, 200, 300]
l1.extend(l2)

#2) Agregar el juntar los caracteres de una lista en una sola cadena de caracteres
l3 = ["h","o","l","a"] 
cadena = "".join(l3)

#3) Convertir La Pimer Letra De Cada Palabra En Mayuscula
l3 = "este es un texto de pruebas"
cadena = l3.title()

#4) Remplazar las letras a, e, i, o, u por @,3,1,0,~ respectivamente
l4 ="murcielago"
cadena = l4.replace("a","@")
cadena = cadena.replace("e","3")
cadena = cadena.replace("i","1")
cadena = cadena.replace("o","0")
cadena = cadena.replace("u","-")

#5) Con un metodo, sumarle un valor a la variable
l5 = 24
a = l5._add_(25)