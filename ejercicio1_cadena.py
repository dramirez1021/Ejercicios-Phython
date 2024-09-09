cadena=input("introduce una cadena: ")
longitud= len(cadena)
if longitud >=3:
    if cadena[ -3 : ] == "ing":
      print (cadena + "ly")
    else:
        print(cadena + "ing")

else:
    print(f"{cadena}")
