palindromo=int(input("introduce un numero de 7 digitos : "))
if palindromo % 10  == palindromo  % 10000000 // 1000000 :
    if palindromo % 100 // 10  == palindromo  % 1000000 // 100000 :
        if palindromo % 1000 // 100  == palindromo  % 100000 // 10000 :
                            print("El numero es un palindromo")
if palindromo % 10  != palindromo  % 10000000 // 1000000 :
    if palindromo % 100 // 10 != palindromo % 1000000 // 100000 :
        if palindromo % 1000 // 100 != palindromo % 100000 // 10000 :
           print("No es un palindromo")
if  palindromo / 10000000 < 0.1  :
    print("El numero no contiene los 7 digitos necesarios")
if palindromo // 10000000 != 0 :
  print("El numero tiene mas de 7 digitos")


