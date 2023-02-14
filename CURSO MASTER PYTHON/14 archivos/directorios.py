import os

#crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("ya existe el direcctorio")

#eliminar carpeta

#os.rmdir("./mi_carpeta")

#renombrar
os.rename("./mi_carpeta", "./nueva_carpeta")