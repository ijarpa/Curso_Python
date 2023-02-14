"""
pedir dos numeros al usuario y mostrar los numeros entre ellos
"""

numero1 = int(input("ingresa un numero: "))
numero2 = int(input("ingresa otro numero: "))

for i in range(numero1, numero2):
    if numero1 < numero2:
        print(i)
    else:
        print("el numero 2 debe ser mayor que el numero 1") #no supe como lograr tirar los numeros si el numero 2 es mayor