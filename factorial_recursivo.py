def factorialRecursivo(numero):
    #caso base
    if numero == 0:
        return 1
    if numero == 1 :
        return 1
    #general
    return numero * factorialRecursivo(numero-1)
numero = int(input("introduce un numero:"))
print(factorialRecursivo(numero))