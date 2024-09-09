frase = input("escribe una frase: ")
lista= frase.split()
tamanio_masgrande=0
palabraMasgrande=""
for elemento in lista :
    tamanio= len(elemento)
    if tamanio > tamanio_masgrande:
        palabraMasgrande= elemento
        tamanio_masgrande=tamanio
print(f"{palabraMasgrande}")