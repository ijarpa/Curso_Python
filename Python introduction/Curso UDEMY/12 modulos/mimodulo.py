def holaMundo(nombre):
    return f"hola mundo {nombre}"

def calculadora():
    print("""Que operacion quieres realizar
    1) SUMA
    2) RESTA
    3) MULTIPLICACION
    4) DIVISION """)

    operacion = int(input("selecciona una operacion: "))

    if operacion == 1:
        print("que numeros quieres sumar?")
        numero1 = int(input(": "))
        print(" + ")
        numero2 = int(input(": "))
        resultado = (numero1 + numero2)

        return f"El resultado de sumar {numero1} + {numero2} es {resultado}"
    
    elif operacion == 2:
        print("que numeros quieres restar?")
        numero1 = int(input(": "))
        print(" - ")
        numero2 = int(input(": "))
        resultado = (numero1 - numero2)

        return f"El resultado de restar {numero1} - {numero2} es {resultado}"
