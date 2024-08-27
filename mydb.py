import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'cmatt',
    passwd = 'Chitanda11'

    )

#Prepare a cursor object
cursorObject = dataBase.cursor()

#Create database
cursorObject.execute("CREATE DATABASE Veterinary")

print("All Done!")