# Proposito estructura while
# Autor: DRM
# Fecha: 16/11/2020
numero=int(input("introduce en numero del que quieres saber el factorial: "))
contador=1
if numero == 0:
    print(f"el factorial de {numero}!: es 1")
while numero > 0:
    contador *=numero
    numero -=1
print(f"el factorial es: {contador}")


