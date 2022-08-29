from item import Item 

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones = 0):
        super().__init__(
            name, price, quantity
        )            
        # Validate received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} must be equal or greater than zero"
        
        # Assign attributes to self object
        self.broken_phones = broken_phones