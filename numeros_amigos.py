def numerosAmigos(numero1,numero2):
    if getSumaDivisores(numero1) == numero2 and getSumaDivisores(numero2)== numero1:
      return True
    else:
       return False
def getSumaDivisores (numero):
    lista=[]
    for i in range (1,numero):
        if numero % i == 0:
            lista.extend([i])
    suma=0
    for j in lista:
        suma +=j
    return suma
num1= int(input("introduce un valor: "))
num2= int(input("introduce un valor: "))
if numerosAmigos(num1,num2) == True:
    print(f"{num1} y {num2} son amigos")
else:
    print(f"{num1} y {num2} no son amigos")