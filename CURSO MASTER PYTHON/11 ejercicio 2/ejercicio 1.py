numeros = [12,124,55,15,2,6,78,59,86,42]

for i in numeros:
    print(i)

print("######## PARTE 2 #########")

numeros.sort()
print(numeros)

print(len(numeros))


try:
    busqueda = numeros.index(10)
    print(busqueda)
except:
    print("el numero no existe")

