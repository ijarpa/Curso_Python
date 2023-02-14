"""
hacer un programa que muestre todos los numeros impares entre 2 
numeros que decida el usuario
"""

num1 = int(input("introduce un numero: "))
num2 = int(input("introduce otro numero: "))


for i in range(num1,num2):
    if i%2 != 0:
        print(i)
    else: 
        print("numero 1 debe ser mayor a numero 2")