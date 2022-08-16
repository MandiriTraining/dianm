from flask import Flask, render_template, request
from flask import jsonify
import mysql.connector


dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = "retail_db"
)  

@app.route('/', methods = ["GET"]) 
def getAllCustomer():
  cust = "select * from customers limit 10"
  # query customer
  # execute
  cursorObject.execute(cust)
  result = cursorObject.fetchall()
  response = jsonify(result)

@app.route('/customerid', methods = ["GET"])
def getCustomerbyID(id):
  cust = "Select * from customers where customer_id = " + id
  cursorObject.execute("cust")
  result = cursorObject.fetchone()
  response = jsonify(result)

@app.route('/departments', methods = ["GET"])
def getProducts():
  cursorObject.execute("select * from departments")
  result = cursorObject.fetchall()
  response = jsonify(result)

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8001,debug = True)
   app.run()
