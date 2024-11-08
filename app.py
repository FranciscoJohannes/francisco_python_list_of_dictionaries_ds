from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello, World!")

products = [
{"name": "Laptop", "category": "Electronics", "id": 1, "supplier": "supplier1@gmail.com", "price": 750, "stock": 50},
{"name": "Desk Chair", "category": "Furniture", "id": 2, "supplier": "supplier2@gmail.com", "price": 100, "stock": 200},
{"name": "Smartwatch", "category": "Electronics", "id": 3, "supplier": "supplier3@gmail.com", "price": 200, "stock": 150},
{"name": "Notebook","category": "Stationery", "id": 4, "supplier": "supplier4@gmail.com", "price": 5, "stock": 500},
{"name": "Running Shoes", "category": "Apparel", "id": 5, "supplier": "supplier5@gmail.com", "price": 80, "stock": 100}
]

for product in products:
    print(f"Name: {product.get('name')}, category: {product.get('section')}, id: {product.get('id')} supplier: {product.get('supplier')}, price: {product.get('price')}")

employees = [
{"name": "John Doe", "department": "SalesHuman Resources", "id": 1, "email": "john.doe@company.com", "age": 30},
{"name": "Jane Smith", "department": "Electronics", "id": 2, "email": "jane.smith@company.com", "age": 25},
{"name": "Mark Johnson", "department": "IT", "id": 3, "email": "mark.johnson@company.com", "age": 40},
{"name": "Lisa Wong", "department": "Marketing", "id": 4, "email": "lisa.wong@company.com", "age": 28},
{"name": "Paul McDonald", "department": "Finance", "id": 5, "email": "paul.mcdonald@company.com", "age": 35}
]

for employee in employees:
    print(f"Name: {employee.get('name')}, department: {employee.get('department')}, id: {employee.get('id')} email: {employee.get('email')}, age: {employee.get('age')}")



if __name__ == '__main__':
    app.run(debug=True)