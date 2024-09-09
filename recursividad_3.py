#proposito: tarea recursividad ejercicio 4
# autor: DRM
# Fecha: 24/01/2021
def lista(frase, subc):
    indice = frase.find(subc)

    if indice == -1:
        print("")

    else:
        print(indice)
        frase = frase.replace(subc, ("*" * 2 ),1)

        lista(frase, subc)

frase = input("introduce una frase: ")
subc = input("introduce la palabra a buscar: ")
lista (frase,subc)
