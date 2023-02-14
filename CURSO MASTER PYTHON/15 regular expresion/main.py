import re

texto = "hola estos es un texto de prueba"

buscar = re.search("prueba", texto)

print(buscar)
print("")

buscarTodos = re.findall("e", texto)
print(buscarTodos)
print("")

separar = re.split("\s", texto, 1)
print(separar)

sustitur = re.sub("a", "x", texto)
print(sustitur)


"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string
"""