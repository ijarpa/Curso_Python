import mysql.connector

def conectar():
    database = mysql.connector.connect(
        user = 'root',
        passwd = '',
        host = 'localhost',
        database = 'master_python',
        port=3308 
    )
   
    cursor = database.cursor(buffered=True) # buffered=True permite realizar varias consultas con el mismo cursor

    return [database, cursor]