import clases
print("")
persona = clases.Persona()
persona.setNombre("Ivan Jarpa")
persona.setEdad(30)
persona.setPais("Chile")

print(f"mi nombre es {persona.getNombre()}, soy de {persona.getPais()} y tengo {persona.getEdad()} años")
print(persona.hablar())

print("\n##### ###### ###### ####### ###### ###### ####### ####### ##### ###### ######\n")

informatico = clases.Informatico()
informatico.setNombre("Pedro Sanchez")
informatico.setEdad(29)
informatico.setPais("Noruega")

print(f"mi nombre es {informatico.getNombre()}, soy de {informatico.getPais()} y tengo {informatico.getEdad()} años")

print(informatico.getLenguajes())
print(informatico.programar())

