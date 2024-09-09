cadena = "hola"

for letra in cadena:
    print(f"el caracter es: {letra*5}")

print("ok")

lista = [1, 2, 3, 4, 5, True, 3.4, "Hola", [4,5,6]]

for elemento in lista:

    if type(elemento) == list:
        for item in elemento:
            print(elemento)