#pedir numeros indefinidamente hasta ingresas el 111

numero_ingresado = 0

guardados = []

while numero_ingresado != 111:
    
    numero_ingresado = int(input("ingresa un numero: "))
    guardados.append(numero_ingresado)
    
    
    if numero_ingresado == 111:
        print(f"\nlos numeros ingresados fueron los siguientes: {guardados}, en total fuerno {len(guardados)} intentos")
        break
        