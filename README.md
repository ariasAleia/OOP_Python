# Object Oriented Programming in Python!


Yes! Welcome to the second part of this journey, if you haven't seen the beginning of this path, go and take a peek [here](https://github.com/ariasAleia/Learning_Python).


Now, we are in the second station. And the main character here is... Chan chan chaaan, Yap -> OOP. Object Oriented Programming.

<p style="text-align:right"><b> "Change is inevitable but transformation is by conscious choice</b>"<br>Heatherash Amara</p>


## Learning and always learning

In this repo, I will trace and take notes of the most important and useful things I will find in this [course](https://www.youtube.com/watch?v=Ej_02ICOIgs). Wish you a good trip. Hope you enjoy this path as much as I do :)


## Class

We can define a class and then create an instance or an object of the class. Object and instance creation mean the same.

```python
class Item:
    pass

item1 = Item()
```

Btw, the word *pass* is used when we haven't defined what is inside a function, a loop, a conditional or a class and we don't want to get a syntax error.

## Methods 

Those are basically functions that are inside a class. We must always pass as argument the object itself. That is done by writing *self* in the function parameters when we define the function. 

```python
class Item:
    def calculate_total_price(self):
        pass
```


Hey! Remember it!!! All methods in a class must have as parameter the object itsefl! We do it by writing *self* in the method.

## Constructor

Well, basically the function that is called when we make an instance of a class.

We write it with *def __*. Those methods with double underscore are usually codes magic methods.

This in a constructor. We can also assign the attributes of the class.

```python
class Item:
    
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
item1 = Item("Phone", 50, 6)
print(f"Name: {item1.name} Price: {item1.price} Quantity: {item1.quantity}")
item2 = Item("Laptops", 45)
print(f"Name: {item2.name} Price: {item2.price} Quantity: {item2.quantity}")
```

## Assign attributes to specific instances individually

Important and interesting to know. We can keep adding attributes directly to the instant that we created:
```python
class Item:
    
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
item1 = Item("Phone", 50, 6)
print(f"Name: {item1.name} Price: {item1.price} Quantity: {item1.quantity}")
item2 = Item("Laptops", 45)
print(f"Name: {item2.name} Price: {item2.price} Quantity: {item2.quantity}")
#New attribute
item2.has_big_screen = False
print(item2.has_big_screen)
```

In this case, the attribute *has_big_screen* was created after and it will be valid only for the object *item2* but the point here is that it was valid to add it. Yes, in the constructor we specify attributes that the instances of the class must have but it doesn't mean that we cannot add more attributes to specific instances that we created. 

## Specifying the type of a variable in a function

Yep! I really like learning. I didn't know how to do this before and now I will learn it! :D I really feel better when I can make progress and understand! Understand. Wow! Definitely one of my favorite verbs.

25:44