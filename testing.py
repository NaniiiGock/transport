from main import Vehicle, Item, Location, logSystem, Order


vehicles = [Vehicle(1), Vehicle(2)]
logSystem = logSystem(vehicles)

"""1. order"""
my_items = [Item('book',110), Item('chupachups',44)]
my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)

print(my_order)
# Your number is -7034054118153310427.

logSystem.placeOrder(my_order)
logSystem.trackOrder(my_order.orderId)
# Your order is sent to Lviv. Total price: 154 UAH.

"""2. order"""
my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
my_order2 = Order('Andrii', 'Odessa', 3, my_items2)

print(my_order2)
# Your number is -5003810793544645465.

logSystem.placeOrder(my_order2)
logSystem.trackOrder(my_order2.orderId)
# Your order is sent to Odessa. Total price: 164.33 UAH.

"""3. order"""
my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)

print(my_order3)
# Your number is -761159483278610152.

logSystem.placeOrder(my_order3)
# there is no available vehicle to deliver an order
logSystem.trackOrder(my_order3.orderId)
# no such order
