#programación orientada a obejtos (POO o OOP)

#definir una clase(molde para mas objetos del mismo tipo)
#crear coche con caracteristicas similares

class Coche:

    #Atributos o Propiedades (Variables)
    #Caracteristicas del coche
    color = "Rojo"
    marca = "ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje =  500
    plazas = 2

    #metodos, acciones que realiza el coche (Funciones)
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

    #CAMBIAR VARIABLES/PROPIEDADES
    def setColor(self, color):
        self.color = color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    #Extraer valor de propiedad
    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo
    

#fin definicion clase

#CREAR OBJETO / INSTANCIAR LA CLASE
coche = Coche()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

coche.setColor("Morado")
coche.setModelo("Turismo R")

print("el color del coche es:", coche.color)
print("la velocidad actual del coche es:", coche.velocidad)
print("modelo:", coche.getModelo())
print("Color:", coche.getColor())
