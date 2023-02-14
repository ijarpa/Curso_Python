# FOR

contador = 0

resultado = 0
for contador in range(5):
    print("voy por el "+str(contador))

    resultado = resultado+contador
    
print(resultado)


print("############EJEMPLO 1 ####################")

numero_usuario=int(input("de que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### TABLA DE MULTIPLICAR N° {numero_usuario}")

for numero_tabla in range(1,10):
    print(f"{numero_usuario}x{numero_tabla}={numero_usuario*numero_tabla}")