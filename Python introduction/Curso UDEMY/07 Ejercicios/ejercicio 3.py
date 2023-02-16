"""
imprimir el cuadrado de los primeros 60 numeros naturales
resolverlo con bucle FOR y WHILE
"""

#parte 1 FOR
for i in range(1,61):
    print(i**2)
    
#parte 2 WHILE

print("\n########### PARTE 2 ###############\n")

cuadrado = 0

while cuadrado < 60:
    cuadrado+=1
    print(cuadrado**2)
