import pypyodbc
from config import connect

#connection string
conn_str = "DSN=" + connect["DSN"] + ";" + "Database=" + connect["Database"] + ";" + "UID=" + connect["UID"] + ";" + "PWD=" + connect["PWD"] + ""

DB = pypyodbc.connect(conn_str)

cursor = DB.cursor()

cursor.execute("SELECT Txt FROM test WHERE Cod = 'C005'")

row = cursor.fetchall()

print(row)

cursor.close()
DB.close()