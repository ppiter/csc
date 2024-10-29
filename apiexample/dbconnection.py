## https://www.geeksforgeeks.org/how-to-connect-python-with-sql-database/

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ANSKk08aPEDbFjDO",
    port = 3306
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE geeksforgeeks")


# Printing the connection object 
print(mydb)