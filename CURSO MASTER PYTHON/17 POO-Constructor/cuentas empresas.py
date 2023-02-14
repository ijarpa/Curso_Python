#entregar información de las empresas

#definir objetos
class Empresa:
    def __init__(self, codigoEmpresa, nombreEmpresa, rut):
        self.codigoEmpresa = codigoEmpresa
        self.nombreEmpresa = nombreEmpresa
        self.rut = rut

class Banco(Empresa):
     def __init__(self, codigoEmpresa, nombreEmpresa, rut, Banco, cuenta):
         self.codigoEmpresa = codigoEmpresa
         self.nombreEmpresa = nombreEmpresa
         self.rut = rut
         self.banco = Banco
         self.cuenta = cuenta

empresaLtda = Banco(1, "Copelec Ltda", "80.237.700-2", ["Santander", "BCI", "ITAU"], ["6342501816", "67071171", "0209445709"])
empresaSA = Banco(2, "Comercial Copelec", "80.237.700-2", ["Santander", "BCI", "ITAU"], ["6342501816", "67071171", "0209445709"])#cambiar datos
empresaAliados = Banco(3, "Servicios Aliados", "80.237.700-2", ["Santander", "BCI", "ITAU"], ["6342501816", "67071171", "0209445709"])#cambiar datos
empresaFINCOP = Banco(6, "Fincop", "76.177.725-4", ["Santander", "BCI", "ITAU"], ["6342501816", "67071171", "0209445709"])#cambiar datos



def MostrarInfo():
    print("########### EMPRESAS ##########")
    print("""EMPRESAS:\n 
    codigo | Empresa
    1)       Copelec Ltda
    2)       Comercial Copelec SA
    3)       Servicios Aliados
    6)       Fincop
    """)

    seleccionEmpresa = int(input("Selecciona una Empresa: "))
    
    if seleccionEmpresa == 1: # seleccion 1 COPELEC LTDA
        print("########### CUENTAS ##########")
        print("""BANCOS:\n 
    1) Santander
    2) BCI
    3) ITAU
        """)
        seleccionBanco = int(input("Selecciona un banco: "))
        if seleccionBanco == 1:  # SELECCION 1 SANTANDER
            print(f"\nnombre: {empresaLtda.nombreEmpresa}")
            print(f"rut: {empresaLtda.rut}")
            print(f"Banco: {empresaLtda.banco[0]}")
            print(f"cuenta: {empresaLtda.cuenta[0]}")
        elif seleccionBanco == 2: # SELECCION 2 BCI
            print(f"\nnombre: {empresaLtda.nombreEmpresa}")
            print(f"rut: {empresaLtda.rut}")
            print(f"Banco: {empresaLtda.banco[1]}")
            print(f"cuenta: {empresaLtda.cuenta[1]}")
        elif seleccionBanco == 3: # SELECCION 3 ITAU
            print(f"\nnombre: {empresaLtda.nombreEmpresa}")
            print(f"rut: {empresaLtda.rut}")
            print(f"Banco: {empresaLtda.banco[2]}")
            print(f"cuenta: {empresaLtda.cuenta[2]}")
        else:
            print("INGRESA UN NUMERO CORRECTO")
        
    elif seleccionEmpresa == 2: # seleccion 1 COPELEC SA
        print("########### CUENTAS ##########")
        print("""BANCOS:\n 
    1) Santander
    2) BCI
    3) ITAU
        """)
        seleccionBanco = int(input("Selecciona un banco: "))
        if seleccionBanco == 1:  # SELECCION 1 SANTANDER
            print(f"\nnombre: {empresaSA.nombreEmpresa}")
            print(f"rut: {empresaSA.rut}")
            print(f"Banco: {empresaSA.banco[0]}")
            print(f"cuenta: {empresaSA.cuenta[0]}")
        elif seleccionBanco == 2: # SELECCION 2 BCI
            print(f"\nnombre: {empresaSA.nombreEmpresa}")
            print(f"rut: {empresaSA.rut}")
            print(f"Banco: {empresaSA.banco[1]}")
            print(f"cuenta: {empresaSA.cuenta[1]}")
        elif seleccionBanco == 3: # SELECCION 3 ITAU
            print(f"\nnombre: {empresaSA.nombreEmpresa}")
            print(f"rut: {empresaSA.rut}")
            print(f"Banco: {empresaSA.banco[2]}")
            print(f"cuenta: {empresaSA.cuenta[2]}")
        else:
            print("INGRESA UN NUMERO CORRECTO")
    
    elif seleccionEmpresa == 3: # seleccion SERVICIOS ALIADOS
        print("########### CUENTAS ##########")
        print("""BANCOS:\n 
    1) Santander
    2) BCI
    3) ITAU
        """)
        seleccionBanco = int(input("Selecciona un banco: "))
        if seleccionBanco == 1:  # SELECCION 1 SANTANDER
            print(f"\nnombre: {empresaAliados.nombreEmpresa}")
            print(f"rut: {empresaAliados.rut}")
            print(f"Banco: {empresaAliados.banco[0]}")
            print(f"cuenta: {empresaAliados.cuenta[0]}")
        elif seleccionBanco == 2: # SELECCION 2 BCI
            print(f"\nnombre: {empresaAliados.nombreEmpresa}")
            print(f"rut: {empresaAliados.rut}")
            print(f"Banco: {empresaAliados.banco[1]}")
            print(f"cuenta: {empresaAliados.cuenta[1]}")
        elif seleccionBanco == 3: # SELECCION 3 ITAU
            print(f"\nnombre: {empresaAliados.nombreEmpresa}")
            print(f"rut: {empresaAliados.rut}")
            print(f"Banco: {empresaAliados.banco[2]}")
            print(f"cuenta: {empresaAliados.cuenta[2]}")
        else:
            print("INGRESA UN NUMERO CORRECTO")
    
    elif seleccionEmpresa == 6: # seleccion 1 FINCOP
        print("########### CUENTAS ##########")
        print("""BANCOS:\n 
    1) Santander
    2) BCI
    3) ITAU
        """)
        seleccionBanco = int(input("Selecciona un banco: "))
        if seleccionBanco == 1:  # SELECCION 1 SANTANDER
            print(f"\nnombre: {empresaFINCOP.nombreEmpresa}")
            print(f"rut: {empresaFINCOP.rut}")
            print(f"Banco: {empresaFINCOP.banco[0]}")
            print(f"cuenta: {empresaFINCOP.cuenta[0]}")
        elif seleccionBanco == 2: # SELECCION 2 BCI
            print(f"\nnombre: {empresaFINCOP.nombreEmpresa}")
            print(f"rut: {empresaFINCOP.rut}")
            print(f"Banco: {empresaFINCOP.banco[1]}")
            print(f"cuenta: {empresaFINCOP.cuenta[1]}")
        elif seleccionBanco == 3: # SELECCION 3 ITAU
            print(f"\nnombre: {empresaFINCOP.nombreEmpresa}")
            print(f"rut: {empresaFINCOP.rut}")
            print(f"Banco: {empresaFINCOP.banco[2]}")
            print(f"cuenta: {empresaFINCOP.cuenta[2]}")
        else:
            print("\nINGRESA UN NUMERO CORRECTO")

    else:
        print("\nINGRESA UN NUMERO CORRECTO")

    
funcionando = 0
while funcionando == 0:
    MostrarInfo()
    print("\nQUIERES REALIZAR OTRA ACCION? ")
    respuesta = input("SI / NO: ").upper()
    if respuesta == "SI":
        funcionando = 0
    else:
        funcionando = 1
        break

