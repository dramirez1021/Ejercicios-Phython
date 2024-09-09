import random
numero = random.randint(0,10)
numerovidas = 3
valorusuario = 0
while numerovidas > 0 :
    valorusuario = int(input("adivina el numero: "))
    if valorusuario == numero :
        print("ganaste")
    else:
        numerovidas -= 1
        print("prueba de nuevo")
if numerovidas == 0:
   print(f"perdiste, el numero es:{numero}")
