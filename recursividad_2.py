#proposito: tarea recursividad ejercicio 3
# autor: DRM
# Fecha: 24/01/2021
def listaRepetida (palabra,lista):
    if lista == 0:
        return None

    else:
     print(lista[0])
    return listaRepetida(lista[ len(palabra): ],palabra)
palabra= input("introduce una palabra")
lista = input("introduce una oracion")
listaRepetida(palabra,lista)