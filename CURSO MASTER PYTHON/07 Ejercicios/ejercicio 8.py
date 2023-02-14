"""
sacar el porcentaje de un numero X introducido por el usuario
"""

numero = int(input("introduce un numero: "))
print(f"el numero que elegiste es {str(numero)}")

#porcentaje
porcentaje = int(input(f"introduce el porcentaje que quieras sacar del numero {numero}: "))


nuevo_numero = (porcentaje*numero)/100
nuevo_numero = float(nuevo_numero)
print(f"el {porcentaje}% de {numero} es {round(nuevo_numero,2)}")