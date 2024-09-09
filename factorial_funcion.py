def factorial(numero):
    """calcula el factorial de un numero"""

    factorial= 1
    while numero >= 1:
        factorial = factorial * numero
        numero -= 1
    return factorial
for numero in range (1,51):
    print(f"{factorial(numero)}")



