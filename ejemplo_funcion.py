def mayorTres(num1,num2,num3):
    """obtiene el mayor de tres numeros"""

    mayor=0

    if num1 >= num2 and num1>= num3:
        mayor = num1
    if num2 >= num1 and num2 >= num3:
            mayor = num2
    if num3 >= num2 and num3 >= num1:
            mayor = num3
    return mayor
print(mayorTres(4,45,8))
print(mayorTres(3,5,8))
print(mayorTres(40,45,8))