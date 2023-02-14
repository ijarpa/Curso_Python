#CREAR UNA CLASE Y LUEGO TRASPASAR PROPIEDADES POR HERENCIA

class Persona:
    #Nombre
    #Edad
    #Pais
    def setNombre(self, nombre):
        self.nombre = nombre 
    def setEdad(self, edad):
        self.edad = edad
    def setPais(self, pais):
        self.pais = pais
    
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getPais(self):
        return self.pais

    def hablar(self):
        return "estoy hablando"


class Informatico(Persona):
    #lenguajes
    #experiencia
    
    #Constructor
    def __init__(self):
        self.lenguajes = "HTML ,Python, Ruby, JavaScript"
        self.experiencia = 2
    
    #definir Getters
    def getLenguajes(self):
        return self.lenguajes
    def getExperiencia(self):
        return self.experiencia

    #definir funciones
    def programar(self):
        return "Estoy programando"
