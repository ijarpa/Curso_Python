nombre = "Ivan Jarpa"

#funciones generales
print(type(nombre))

#detectar tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print("es un string")


####### Limpiar espacios ##########
frase = "     mi contenido    "
print(frase)
print(frase.strip())

#### Eliminar variables ####
year = 2020
print(year)
del year
#print(year)

#comprobar variables vacias
texto = "  vacia   "
if len(texto)<=0:
     print("variable vacia")
else:
    print(f"la variable tiene contenido {len(texto)}")

#encontrar caracteres
frase = "La vida es Bella"
print(frase.find("vida"))

# reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)