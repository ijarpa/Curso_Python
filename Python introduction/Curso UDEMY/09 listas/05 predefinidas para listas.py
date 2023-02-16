cantantes = ["eminem", "julio iglesias", "camilo", "yatra"]

numero = [1,2,5,6,8,4,9]

#ordenar listas

print(numero)
numero.sort()
print(numero)

#agregar elementos
cantantes.append("tini")
print(cantantes)

cantantes.insert(1, "maroon 5")
print(cantantes)

#eliminar elementos
cantantes.pop(2)
print(cantantes)
cantantes.remove("yatra")
print(cantantes)

#dar la vuelta a la lista / cambiar el orden
print(numero)
numero.reverse()
print(numero)

#buscar dentro de lista
print("maroon 5" in cantantes)

#cuantas veces aparece un elemento
print(numero.count(1))

#conseguir indices
print(cantantes.index("maroon 5"))

#unir listas
cantantes.extend(numero)
print(cantantes)