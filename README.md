Coffee Shop Project
Overview
This Python-based Coffee Shop project models the interactions between Customers, Coffees, and Orders using Object-Oriented Programming (OOP). The project demonstrates concepts like classes, instances, object relationships, and aggregate methods. It includes three main models:
•	Customer: Represents customers who place orders.
•	Coffee: Represents the types of coffee available at the shop.
•	Order: Represents an order placed by a customer for a specific coffee with a defined price.
Table of Contents
•	Features
•	Running the Application
•	Tests
•	License
Features
1. Customer
•	Create a customer with a name.
•	Fetch all orders placed by the customer.
•	Fetch all coffees ordered by the customer.
•	Place a new order (creates an association with Coffee).
2. Coffee
•	Create a coffee with a name.
•	Fetch all orders for a particular coffee.
•	Fetch all unique customers who ordered a particular coffee.
•	Get the total number of orders for a coffee.
•	Calculate the average price of orders for a coffee.
3. Order
•	Create an order with a customer, coffee, and price.
•	Associate the order with both a customer and a coffee.
•	Fetch the customer and coffee associated with the order.
Setup Instructions
1. Clone the Repository
Start by cloning the private repository (which you will need to create on GitHub).
’’’
Copy code
git clone https://github.com/tony-g30/Mock-Code-Challenge---Coffee-Shop-Object-Relationships-.git
cd coffee-shop
’’’
2. Create a Virtual Environment
’’’
python3 -m venv my_env
source my_env/bin/activate
’’’
4. Test the Application
The core of the project is in the Python modules (customer.py, coffee.py, order.py). You can test the functionality by using codium vs code extension.
License
This project is licensed under the MIT License - see the LICENSE file for details.
