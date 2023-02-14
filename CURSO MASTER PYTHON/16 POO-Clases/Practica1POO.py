#creando clase PERSONA para formulario

class Persona:
    #set
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def setSexo(self, sexo):
        self.sexo = sexo
    
    #get
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getSexo(self):
        return self.sexo

#agregar personas
def agregarpersona():
    respuestaPositiva = ["si", "SI", "S", "s"]
    pregunta1 = (input("Quieres agregar una persona? SI/NO: "))
    while pregunta1 in respuestaPositiva:
        persona1

    
