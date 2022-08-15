from flask import Flask, render_template, request
import mysql.connector

dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = "employees"
)  

#
# creating table
dept = "select * from employees limit 10"
  
# table created
cursorObject.execute(dept)

result = cursorObject.fetchall()

print(result)
if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8001,debug = True)
   app.run()
