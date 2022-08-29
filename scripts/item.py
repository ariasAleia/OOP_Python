import csv


class Item:
    
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Validate received arguments
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"

        # Assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute 
        Item.all.append(self)
        
    def calculate_total_price(self)->float:
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= self.pay_rate
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            for item in reader:
                Item(
                    name = item.get("name"),
                    price = float(item.get("price")),
                    quantity = int(item.get("quantity"))
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            return num.is_integer()
        return False
           

      


    