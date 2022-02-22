import mysql.connector
conn = mysql.connector.connect(user='root', password='Lithesh55', host='127.0.0.1')
cursor = conn.cursor()
cursor.execute("DROP database IF EXISTS MyDatabase")
sql = "CREATE database MYDATABASE";
cursor.execute(sql)
print("List of databases: ")
cursor.execute("SHOW DATABASES")
conn.close()
