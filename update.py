import mysql.connector
#establishing the connection
conn = mysql.connector.connect( user='root', password='Lithesh55', host='127.0.0.1', database='MYDATABASE')
 #Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Preparing the query to update the records
sql = '''UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M' '''
# Execute the SQL command 
cursor.execute(sql)
# Commit your changes in the database
conn.commit()

#Retrieving data
sql = '''SELECT * from EMPLOYEE'''

#Executing the query
cursor.execute(sql)

#Displaying the result
print(cursor.fetchall())

#Closing the connection
conn.close()
