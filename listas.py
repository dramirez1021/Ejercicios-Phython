lista= [2,4,5,True,"cadena",[1,2]]
print(f"{len(lista)}")
lista2= ["hola"]
print(f"{lista + lista2}")
print(f"{lista *3}")
print(f"{lista[3]}")
print(f"{lista[2:6]}")
lista[3]= False
print(f"{lista}")
lista.append("phyton")
print(f"{lista}")
del lista[3]
print(f"{lista}")
del lista[3:-2]#corta la lista, en -2 corta una después
print(f"{lista}")

