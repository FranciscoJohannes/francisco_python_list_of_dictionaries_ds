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
    print(f"Name: {product.get('name')}, category: {product.get('section')}, id: {product.get('email')} supplier: {product.get('supplier')}, price: {product.get('price')}")







if __name__ == '__main__':
    app.run(debug=True)