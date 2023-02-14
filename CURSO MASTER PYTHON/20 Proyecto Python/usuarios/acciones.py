import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registrar_usuario(self):
        nombre = input("ingresa tu nombre: ")
        apellidos = input("ingresa tus apellidos: ")
        email = input("ingresa tu email: ")
        password = input("ingresa tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1]} te has registrado correctamente")
        
        else:
            print("no te has registrado correctamente")


    def login_usuario(self):

        try:
            email = input("ingresa tu email: ")
            password = input("ingresa tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.login()

            if email == login[3]:
                print(f"\nbienvenido {login[1]} has ingresado al sistema\n")
                self.proximasacciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"el login de ha sido incorrecto")   
        


    def proximasacciones(self, usuario):
        print("##### ACCIONES DISPONIBLES #####")
        print("""
        - crear nota (crear)
        - mostrar tus notas (mostrar)
        - eliminar notas (eliminar)
        - salir (salir)
        """)

        accion = input("que quieres hacer?: ").lower()
        hacer = notas.acciones.Acciones()

        if accion == "crear":
            print("crear\n")
            hacer.crear(usuario)
            self.proximasacciones(usuario)
            print("")

        elif accion == "mostrar":
            print("mostrar\n")
            hacer.mostrar(usuario)
            self.proximasacciones(usuario)
            print("")

        elif accion == "eliminar":
            print("eliminar\n")
            hacer.borrar(usuario)
            self.proximasacciones(usuario)
            print("")
            
        elif accion == "salir":
            exit()
        else:
            print("\nAcción Incorrecta")
            print(" ")
            self.proximasacciones(usuario)

        return None

        