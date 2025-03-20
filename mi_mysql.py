import mysql.connector
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Morenito1!"
)

cursor = conexion.cursor()

cursor.execute("SHOW DATABASES")
 
for bd in cursor:
    print(bd)
