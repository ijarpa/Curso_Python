import mysql.connector

#conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

print(database)

cursor = database.cursor()

#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)

#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10, 2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)"""
)

