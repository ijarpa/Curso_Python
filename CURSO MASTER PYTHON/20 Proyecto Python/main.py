"""
Proyecyo Python y MySql
-Abrir asistente
-Login o Registro
-regitros - crear usuario en BD
-login - identificarnos en la BD
-CREAR MOSTRAR o BORRAR Notas
"""

print("""
Acciones disponibles:
    - registro
    - login
""")

accion = input("¿que quieres hacer?: ").lower()

from usuarios import acciones
hacer = acciones.Acciones()

if accion == "registro":
    print("OK! vamos a registrarte en el sistema")
    hacer.registrar_usuario()
elif accion == "login":
    print("OK! vamos a logearte")
    hacer.login_usuario()
else:
    print("accion incorrecta")          
    