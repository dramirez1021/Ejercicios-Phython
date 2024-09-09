cadena= input("introduce cadena: ")
entero= int(input("introduce un entero: "))
lista= cadena.split()
for elemento in lista :
  tamanio= len(elemento)
  if tamanio == entero:
     print(f"{elemento}")

