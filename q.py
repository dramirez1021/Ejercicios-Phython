numero=3
cuadros={}
for num in range(1,numero+1):
    cuadros[num]= num ** 2
for num, valor in cuadros.items():
    print(f"{num}->{valor}",end=" ")