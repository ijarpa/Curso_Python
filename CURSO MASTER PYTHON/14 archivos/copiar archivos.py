from io import open
import pathlib
import shutil

ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_copiado = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"

shutil.copyfile(ruta_original, ruta_copiado)

