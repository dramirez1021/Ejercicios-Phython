palindromo=int(input("introduce un numero de 7 digitos : "))
if palindromo % 10  == palindromo  % 10000000 // 1000000 :
    if palindromo % 100 // 10  == palindromo  % 1000000 // 100000 :
        if palindromo % 1000 // 100  == palindromo  % 100000 // 10000 :
            if palindromo % 10000 // 1000  == palindromo  % 10000 // 1000 :
                if palindromo % 100000 // 10000  == palindromo  % 1000 // 100 :
                    if palindromo % 1000000 // 100000  == palindromo  % 100 // 10 :
                        if palindromo % 10000000 // 1000000  == palindromo  % 10 :
                            print("El numero es un palindromo")
if palindromo % 10  != palindromo  % 10000000 // 1000000 :
    if palindromo % 100 // 10 != palindromo % 1000000 // 100000 :
        if palindromo % 1000 // 100 != palindromo % 100000 // 10000 :
           print("No es un palindromo")
if palindromo // 10000000 != 0 :
  print("El numero no contiene los digitos necesarios")