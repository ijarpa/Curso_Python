import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"{usuario[1]} vamos a crear una nueva nota: \n")
        titulo = input("Introduce el titulo de la nota: \n")
        descripcion = input("introduce el contenido de tu nota: \n")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        
        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")
    
    def mostrar(self, usuario):
        print(f"vamos a mostrar las notas del usuario {usuario[1]}\n")
        
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.mostrar()

        for notas in notas:
            print(f"Titulo: {notas[2]}")
            print(f"Fecha: {notas[4]}\n")
            print(f"Contenido: {notas[3]}\n")

    def borrar(self, usuario):
        print(f"\nOkey {usuario[1]}!! Vamos a borrar notas")

        titulo = input("introduce el titulo de la nota que quieres borrar: ")

        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se ha borrado la nota: {nota.titulo}")
        else:
            print(f"No se ha borrado la nota, intenta de nuevo")