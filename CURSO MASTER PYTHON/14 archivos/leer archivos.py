#leer contenido de ficheros

from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivos_lectura = open(ruta, "r")


contedio = archivos_lectura.read()

for i in contedio:
    print(i.upper(), end="")





archivos_lectura.close()

