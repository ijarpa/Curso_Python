#ejemplo  1 de acceder a listas

lista_1 = ["spiderman", "superman", "iron man", "avengers", "star wars"]

for peliculas in lista_1:
    print(peliculas)



nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una pelicula: ")
    lista_1.append(nueva_pelicula)


for peliculas in lista_1:
    print(f"{lista_1.index(peliculas)+1}. {peliculas}")