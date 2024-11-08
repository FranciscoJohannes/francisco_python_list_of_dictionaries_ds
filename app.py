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

books = [
{"name": "F. Scott Fitzgerald", "title": "SalesHuman Resources", "id": 1, "genre": "Fiction", "Published_Year": "1925", "ISBN": "978-0743273565", "stock": "20", "price": "15.99"},
{"name": "Harper Lee", "title": "To Kill a Mockingbird", "id": 2, "genre": "Fiction", "Published_Year": "1960", "ISBN": "978-0060935467", "stock": "35", "price": "10.99"},
{"name": "George Orwell", "title": "1984", "id": 3, "genre": "Dystopian", "Published_Year": "1949", "ISBN": "978-0451524935", "stock": "40", "price": "9.99"},
{"name": "J.D. Salinger", "title": "The Catcher in the Rye", "id": 4, "genre": "Fiction", "Published_Year": "1951", "ISBN": "978-0316769488", "stock": "25", "price": "8.99"},
{"name": "Stephen Hawking", "title": "A Brief History of Time", "id": 5, "genre": "Non-Fiction", "Published_Year": "1988", "ISBN": "978-0553380163", "stock": "10", "price": "18.99"}
]

for book in books:
    print(f"Name: {book.get('name')}, title: {book.get('title')}, id: {book.get('id')} genre: {book.get('genre')}, ISBN: {book.get('ISBN')}, stock: {book.get('stock')}, price: {book.get('price')}")

universities = [
{"name": "University of the Philippines", "location": "Quezon City", "id": 1, "Established_Year": "1908", "type": "Public", "website": "www.up.edu.ph"},
{"name": "Ateneo de Manila University", "location": "Quezon City", "id": 2, "Established_Year": "1859", "type": "Private", "website": "www.ateneo.edu"},
{"name": "De La Salle University", "location": "Manila", "id": 3, "Established_Year": "1911", "type": "Private", "website": "www.dlsu.edu.ph"},
{"name": "University of Santo Tomas", "location": "Manila", "id": 4, "Established_Year": "1611", "type": "Private", "website": "www.ust.edu.ph"},
{"name": "Polytechnic University of the Philippines", "location": "Manila", "id": 5, "Established_Year": "1904", "type": "Public", "website": "www.pup.edu.ph"}
]

for university in universities:
    print(f"Name: {university.get('name')}, location: {university.get('location')}, id: {university.get('id')} Established_Year: {university.get('Established_Year')}, type: {university.get('type')}, website: {university.get('website')}")

restaurants = [
{"name": "Vikings Luxury Buffet", "location": "Pasay City", "id": 1, "Cuisine_Type": "Buffet", "Established_Year": "2011", "website_or_contact": "www.vikings.ph"},
{"name": "Antonio's Restaurant", "location": "Tagaytay", "id": 2, "Cuisine_Type": "Fine Dining", "Established_Year": "2002", "website_or_contact": "www.antoniosrestaurant.ph"},
{"name": "Mesa Filipino Moderne", "location": "Makati City", "id": 3, "Cuisine_Type": "Filipino", "Established_Year": "2009", "website_or_contact": "www.mesa.ph"},
{"name": "Manam Comfort Filipino", "location": "Quezon City", "id": 4, "Cuisine_Type": "Filipino", "Established_Year": "2013", "website_or_contact": "www.manam.ph"},
{"name": "Ramen Nagi", "location": "Various Locations", "id": 5, "Cuisine_Type": "Japanese", "Established_Year": "2013", "website_or_contact": "www.ramennagi.com.ph"}
]

for restaurant in restaurants:
    print(f"Name: {restaurant.get('name')}, location: {restaurant.get('location')}, id: {restaurant.get('id')} Cuisine_Type: {restaurant.get('Cuisine_Type')}, Established_Year: {restaurant.get('Established_Year')}, website_or_contact: {restaurant.get('website_or_contact')}")

if __name__ == '__main__':
    app.run(debug=True)