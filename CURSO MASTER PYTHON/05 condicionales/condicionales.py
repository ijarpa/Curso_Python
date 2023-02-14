"""
Si se_cumple_esta_condicion:
    ejecutar estas instrucciones
Si_NO:
    ejecutar otras instrucciones

"""

print("##########  EJEMPLO 1  ##########")

color = "azul"
if color == "rojo":
    print("el color es ROJO")
else:
    print("el color no es ROJO")

#ejemplo 2 if anidados
print("\n##########  EJEMPLO 2  ##########")
edad = 26
mayoria_edad = 18
pais = "Chile"

if edad >= mayoria_edad:
    print("eres mayor de edad")
    
    if pais == "Chile":
        print("eres chileno")
    else:
        print("tu no eres chileno")

else:
    print("no eres mayor de edad")