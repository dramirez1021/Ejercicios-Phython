#proposito: tarea recursividad ejercicio 1
# autor: DRM
# Fecha: 24/01/2021
def hanoi(discos, a, b, c):
    if discos == 1:
        print(f"Mover el disco 1 de la torre {a} a la torre {c}:")
        return
    hanoi(discos - 1, a, c, b)
    print(f"Mover el disco {discos} de la torre {a} a la torre {c}:")
    hanoi(discos - 1, b, a, c)

discos = int(input("Introduce el número de discos: "))
hanoi(discos, 'A', 'B', 'C')