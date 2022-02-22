import mysql.connector
#establishing the connection
conn = mysql.connector.connect( user='root', password='Lithesh55', host='127.0.0.1', database='MYDATABASE')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE( FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Lithesh', 'Gadikota', 20, 'M', 200000)"""
# Executing the SQL command
cursor.execute(sql)
# Commit your changes in the database conn.commit()
# Closing the connection
conn.close()
