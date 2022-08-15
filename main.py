from flask import Flask, render_template, request
import mysql.connector

dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
  
# creating table
emp = "select * fom employees limit 10"
  
# table created
cursorObject.execute(emp)

result = cursorObject.fetchall()

print(result)
  
app.run(host="localhost", port =5000)