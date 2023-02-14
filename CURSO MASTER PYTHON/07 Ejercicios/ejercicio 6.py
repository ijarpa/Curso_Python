"""
mostrar todas las tablas de multiplicar del 1 al 10 
mostrando el titulo de la tabla y luego la multiplicación
"""

#tablas de multiplicar
for i in range (1,11):
    print("la tabla de ",i)
    for j in range (1,11):
        producto = i*j
        print(f"el resultado de {i} * {j} es: {producto}")
    print("\n")