class Item:
    
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self):
        return self.price * self.quantity
        
    
item1 = Item("Phone", 50, 6)
print(f"Name: {item1.name} Price: {item1.price} Quantity: {item1.quantity}")
item2 = Item("Laptops", 45)
print(f"Name: {item2.name} Price: {item2.price} Quantity: {item2.quantity}")
#New attribute
item2.has_big_screen = False
print(item2.has_big_screen)

print(item1.calculate_total_price())