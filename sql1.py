import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='Lithesh55', host='127.0.0.1', database='MYDATABASE' )

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
# Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Creating table as per requirement
sql = '''CREATE TABLE EMPLOYEE( FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT )'''

cursor.execute(sql)
#Closing the connection 
conn.close() 
