class Item:
    
    pay_rate = 0.8 # The pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Validate received arguments
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"

        # Assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculate_total_price(self)->float:
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= self.pay_rate
        
    
    
    
item1 = Item("Phone", 100, 6)
print(f"Name: {item1.name} Price: {item1.price} Quantity: {item1.quantity}")
item2 = Item("Laptops", 1000)
print(f"Name: {item2.name} Price: {item2.price} Quantity: {item2.quantity}")
#New attribute
item2.has_big_screen = False
print(item2.has_big_screen)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(f"Class attributes {Item.__dict__}")
print(f"Instance attributes {item1.__dict__}")


print(f"Item 2, before discount {item2.price}")
item2.pay_rate = 0.7
item2.apply_discount()
print(f"Item 2, after new discount {item2.price}")

print(f"Item 1, Before discount: {item1.price}")
item1.apply_discount()
print(f"Item 1, After discount: {item1.price}")
