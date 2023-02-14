tabla = [
    {
        "Categoria": "ACCION",
        "Juegos":["GTA", "COD", "PUBG"]
    },
    {
        "Categoria": "AVENTURA",
        "Juegos":["ASSASSINS CREED", "CRASH", "PRINCE OF PERSIA"]
    },
    {
        "Categoria": "DEPORTES",
        "Juegos":["FIFA", "PES", "MOTO 21"]
    }
]

for categoria in tabla: 
    print(f"--------- {categoria['Categoria']} ---------")