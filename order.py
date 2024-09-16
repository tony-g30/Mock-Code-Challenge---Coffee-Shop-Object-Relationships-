# order.py
class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        # Delay importing to avoid circular import
        from customer import Customer
        from coffee import Coffee

        if isinstance(customer, Customer) and isinstance(coffee, Coffee):
            self._customer = customer
            self._coffee = coffee
        else:
            raise TypeError("Invalid types for customer or coffee")
        
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
