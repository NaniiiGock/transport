"""module for logistic system"""

class Item:
    """items to bye"""
    def __init__(self, name, price):
        """initialisation"""
        self.name = name
        self.price = price
    def __str__(self):
        """
        >>> str(Item('book',110))
        'book, price: 110'
        """
        return f'{self.name}, price: {self.price}'

class Vehicle:
    """
    vehicles in logistic system
    shows only if the vehicle
    with current number is available
    """
    def __init__(self, vehicleNo,isAvailable=True):
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

class Location:
    """special location for each postoffice"""
    def __init__(self, city, postoffice):
        """initialisation"""
        self.city = city
        self.postoffice = postoffice

class Order:
    """to make objects with all order info"""
    def __init__(self, user_name, city, postoffice, items, vehicle=None):
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = vehicle
        self.orderId = hash((self.user_name, self.location, tuple(self.items)))

    def calculateAmount(self):
        """summarise the price for order
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> my_order.calculateAmount()
        154
        """
        amount = 0
        for item in self.items:
            amount += item.price
        return amount

    def __str__(self):
        """shows the order id
        # >>> my_items = [Item('book',110), Item('chupachups',44)]
        # >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        # >>> str(my_order)
        # 'Your number is 6072428283865159028'
        """
        return f'Your number is {self.orderId}.'

    def assignVehicle(self, vehicle):
        """assigns vehicle outside the initialisation"""
        self.vehicle = vehicle

class logSystem:
    """general class for making orders"""
    def __init__(self, vehicles, orders=[]):
        """initialisation"""
        self.vehicles = vehicles
        self.orders= orders

    def placeOrder(self, order):
        """chooses an available vehicle for the order"""
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.assignVehicle(vehicle)
                vehicle.isAvailable = False
                self.orders.append(order)
                break
        else:
            print('there is no available vehicle to deliver an order')

    def trackOrder(self, Id):
        """allows to see details about the order by its number"""
        for order in self.orders:
            if order.orderId == Id:
                price = order.calculateAmount()
                print(f'Your order is sent to {order.city}. Total price: {price} UAH.')
                break
        else:
            print("no such order")
