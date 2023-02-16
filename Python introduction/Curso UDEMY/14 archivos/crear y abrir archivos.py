from io import open
import pathlib

#abrir archivos
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

print(ruta)

archivos = open(ruta, "a+")

#escribir dentro de archivo

archivos.write("####### este es un texto de prueba #######\n")

#cerrar archivos
archivos.close()