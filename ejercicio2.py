#proposito: numero mayor
# autor: DRM
# Fecha: 22/12/2020
numeros = input("escribe una lista de numeros: ")
lista= numeros.split()
numero_masgrande=0
nMasgrande=int()
for elemento in lista :
    tamanio= int(elemento)
    if tamanio > numero_masgrande:
        nMasgrande= elemento
        numero_masgrande=tamanio
print(f"{nMasgrande}")
print(f"{lista}")