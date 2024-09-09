def nPerfecto(numero):
    lista = []
    for i in range (1,numero):
        if numero % i == 0:
            lista.extend([i])
    suma=0
    for j in lista:
        suma += j
    if suma == numero:
        return True
      #print("es un numero perfecto")
    else:
       return False
     #print("no es perfecto")
valor = int(input("introduce un valor: "))
if nPerfecto(valor) == True:
    print(f"{valor} es un numero perfecto")
else:
    print(f"{valor} no es un numero perfecto")



