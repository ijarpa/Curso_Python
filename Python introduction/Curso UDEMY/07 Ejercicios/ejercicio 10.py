"""
pedir notas de 15 alumnos, mostrar en pantalla cuantos aprueban y cuantos reprueban
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota =int(input(f"nota alumno {contador}: "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    
    contador += 1

print(f"alumnos aprobados :{aprobados}")
print(f"alumnos Suspendidos :{suspendidos}")