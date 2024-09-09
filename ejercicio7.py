#proposito: tarea figuras tortuga
# autor: DRM
# Fecha: 22/12/2020
numero= 1
suma= 0
contador= 0
while contador !=1000:
    contador += 2
    for i in range(4):
        numero += contador
        suma = suma + numero

print(f"la suma de las diagonales es : {suma + 1}")