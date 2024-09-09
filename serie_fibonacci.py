def fibonacci (terminos):
    num1 = 0
    num2 = 1
    serie = [0,1]
    contador = 0
    while contador <= terminos:
        serie.append(serie[num1] + serie[num2])
        contador +=1
        num1 += 1
        num2 += 1
    print(serie)
valor= int(input("define los terminos que deseas: "))
fibonacci(valor)

