numero = int(input("ingresa el numero de tu tabla: "))

def tablamultiplicar(numero):

    for contador in range(11):
        resultado = numero*contador
        print(f"{numero} x {contador} = {resultado}")

tablamultiplicar(numero)