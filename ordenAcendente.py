numero1=int(input("escribe un numero:"))
numero2=int(input("escribe un numero:"))
numero3=int(input("escribe un numero:"))
if numero1 >= numero2:

   if numero1 >= numero3:

     if numero2 >= numero3:
        print(f"el orden es: {numero3}, {numero2}, {numero1}")
     if numero2 < numero3:
        print(f"el orden es: {numero2} ,{numero3} ,{numero1}")
   if numero3 > numero1:

    print(f"el orden es: {numero2}, {numero1} ,{numero3}")

if numero2 >= numero1:

    if numero2 >= numero3:
        if numero1 >= numero3:
            print(f"el orden es {numero3} ,{numero1} ,{numero2}")
        if numero1 < numero3:
            print(f"el orden es {numero1} ,{numero3} ,{numero2}")
    if numero3 > numero2:
      print(f"el orden es {numero1} ,{numero2} ,{numero3}")







