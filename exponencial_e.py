#proposito: ejercicio 3
# autor: DRM
# Fecha: 06/01/2021
x= int(input("introdce un numero: "))
fac= 1
constanteE= 1
iteracion= 1
variableFac= 1

for i in range (15) :
  variableFac= iteracion
  while variableFac > 0 :
   fac = fac * variableFac
   variableFac -=1

  constanteE = constanteE + x ** iteracion/fac
  iteracion += 1
  fac= 1
print(f"la constante e es: {constanteE}")
