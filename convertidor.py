print("Programa para convertir numeros")
print(" ")
print("1. Convertir base decimal a n")
print("2. Convertir base n a decimal")

sel = int(input("Que quieres hacer: "))
n = input("Dame el numero a convertir: ")
base = int(input("Dame la base: "))

def aCadena(n, base):
   cadenaConversion = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
   n = int(n)
   if n < base:
      return cadenaConversion[n]
   else:
      return aCadena(n//base,base) + cadenaConversion[n%base]

def base_n(n, base):
   ncadena = str(n)
   exp = len(ncadena) - 1
   resultado = 0
   cadena = "0123456789"
   dic = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16, "H" : 17, "I" : 18, "J" : 19, "K" : 20
   , "L" : 21, "M" : 22, "N" : 23, "Ñ" : 24, "O" : 25, "P" : 26, "Q" : 27, "R" : 28, "S" : 29, "T" : 30, "U" : 31, "V" : 32
   , "W" : 33, "X" : 34, "Y" : 35, "Z" : 36}
   for numero in ncadena:
      if numero in cadena:
         num = int(numero)
      if numero not in cadena:
         num = dic[numero]
      valor = num * (base ** exp)
      resultado += valor
      exp -= 1
   return resultado

if sel == 2:
   print(base_n(n, base))

if sel == 1:
   print(aCadena(n, base))