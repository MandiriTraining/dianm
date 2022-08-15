from flask import Flask, render_template, request
import mysql.connector

dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = "employees"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
  
# creating table
dept = "select employees, departments from employees limit 10"
  
# table created
cursorObject.execute(emp)

result = cursorObject.fetchall()

print(result)
  