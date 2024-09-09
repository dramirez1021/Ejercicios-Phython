#proposito: determinar que tipo de triangulo es
# autor: DRM
# Fecha: 10/11/20
lado1 = int(input("introduce el primer lado: "))
lado2 = int(input("introduce el segundo lado: "))
lado3 = int(input("introduce el tercer lado: "))
if lado1 < 0 and lado2 < 0 and lado3 < 0 :
    print("no se puede formar un triangulo")
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1 :
    if lado1 == lado2 == lado3:
        print("es un triangulo equilatero")
    elif lado3 != lado2 != lado1 :
        print("es un triangulo escaleno")
    elif lado3 == lado2 or lado1 == lado2 or lado3 == lado1:
        print("es un triangulo isoseles")
    else:
        print("no es un triangulo")

