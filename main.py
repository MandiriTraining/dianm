from flask import Flask, request
from flask import jsonify
import mysql.connector

app = Flask(__name__)

dataBase = mysql.connector.connect(
  host ="188.166.221.246",
  user ="training",
  passwd ="training",
  database = "retail_db"
)  

@app.route('/') 
def getAllCustomer():
  cust = "select * from customers limit 10"
  # query customer
  # execute
  cursorObject = dataBase.cursor(dictionary=True)
  cursorObject.execute(cust)
  result = cursorObject.fetchall()
  response = jsonify(result)

@app.route('/customerid/<id>')
def getCustomerbyID(id):
  cust = "Select * from customers where customer_id = " + id
  cursorObject = dataBase.cursor(dictionary=True)
  cursorObject.execute("cust")
  result = cursorObject.fetchone()
  response = jsonify(result)

@app.route('/departments')
def getProducts():
  cursorObject = dataBase.cursor(dictionary=True)
  cursorObject.execute("select * from departments")
  result = cursorObject.fetchall()
  response = jsonify(result)

@app.route('/departmentid/<id>')
def getProductsbyID(id):
  cursorObject = dataBase.cursor(dictionary=True)
  cursorObject.execute("select * from departments where department_id" + id)
  result = cursorObject.fetchall()
  response = jsonify(result)

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8001,debug = True)
   app.run()
