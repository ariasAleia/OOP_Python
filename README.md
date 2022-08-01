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


Hey! Remember it!!! All methods in a class must have as parameter the object itself! We do it by writing *self* in the method.

## Constructor

Well, basically the function that is called when we make an instance of a class.

We write it with *def __*. Those methods with double underscore are usually codes magic methods.

This in a constructor. We can also assign the attributes. **These attributes are called instance attributes**

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

## Specifying the type of a variable(they are really objects!) in a function

Yep! I really like learning. I didn't know how to do this before and now I will learn it! :D I really feel better when I can make progress and understand! Understand. Wow! Definitely one of my favorite verbs.

So! **Really important:** In Python, we don't have variables, we have objects. And each object know its type. We will come back to this later. In functions, we can specify the type of the arguments we are passing. We can do it by using : followed by the type after the name of the parameter. For example:

```python
def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
```

However!!! And here comes sth important, Python won't complain or throw an error if the argument that we pass doesn't match the type of the parameter perse (if we access to attributes that the arguments don't have it will for sure throw an error but we are not referring to that.) And you may ask why? Well... Das ist sicher eine gute Frage. It's because Python follows the next principle:


<p style="text-align:right"><b> "We're all consenting adults here"</b>"</p>

Btw, this [link](https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in) has a great answer explaining this.

But now we may ask: is there any way we can check if an argument has the type we are expecting to receive in the function? And the answer is: Yap. We can. We can check it by doing sth like this:

```python
def pick(l: list, index: int = 0) -> int:
    if not isinstance(l, list):
        raise TypeError
    return l[index]
```

But we shouldn't actually do it then remember, we are all supposed to be adults.

But it's anyway good to indicate what we are expecting to have and also as a return if we have one. For example:

```python
def calculate_total_price(self)->float:
        return self.price * self.quantity
```

In this case, we return a float.

## Validate received arguments in a function with *assert*

So! Ok, we can indicate what kind of type we expect to receive in a function but we already know that python won't complain but that if we want it to do then we can use sth like isinstance but that we shouldn't really do it because we are all adults but... We can do some things. Oh yeah. We can check for example if an argument makes sense. For example in the function when we receive price and quantity of a product we want these values to be greater than 0. And! There's a really short way to do it: We can use assert. We basically check if a condition is met and if not, there will be an assertion error. We can also write a message that will appear in case the condition is not met.


```python
def __init__(self, name: str, price: float, quantity: int = 0):
        # Validate received arguments
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"

        # Assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity
```


## Class attributes and instance attributes

Attributes that will be shared with all the objects or instances created of that class. It belongs to the class itself. 

We declare it inside the class, not inside the init function:

```python
class Item:
    
    pay_rate = 0.8 # The pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        ...
``` 

And then we can access them directly from the class or from an instance of it:

```python
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
```

Why? Well, it's a class attribute and therefore we can access it directly from the class just typing the name of it, in this case *Item*. And we also can access it from the instance. Why? Well, the attributes in an instance are first searched in the instance attributes (those that are found in the init function). If the instance doesn't find those attributes in the instance level, then it will search that in the class level as a class attribute. 

We can now use the class attribute in a function that we define in our class. Remember, we can do it from the class level (as in the example below using Item.pay_rate) or we can do it from the instance level (that would be using self.pay_rate)

```python
    def apply_discount(self):
        self.price *= Item.pay_rate
```
Or:
```python
    def apply_discount(self):
        self.price *= self.pay_rate
```

However!!! The really interesting thing is that those two methods may or may not behave in the same way. Understood? Yep. Really?... Not really. Ok, let's see an example!

Let's imagine that we have the method with the attribute *Item.pay_rate*, that means that it's in the class level. If the pay rate is equal to 0.8 then every time that we call the function *apply_discount()* we will get the value of 0.8 multiplied by the price. But!!!! And here comes the interesting. What if we have another item and we want it to have a different pay rate but we want the rest to keep having the same pay rate? Well, no problem (LY Python :) ) we can do it. How?...

Well, we must modify the parameter *pay_rate* for the item, that means in instance level. But that's not all. We also must use the second way of the function apply_discount because we want it to take the attribute in the instance level. And that would be all!

But wait... you may be asking... If we change it to the instance level using *self.pay_rate* it will work for the item in which we modified the attribute but not for the all, will it? And the answer is that it will still work because if the instance doesn't find the attribute in the instance level it will look for it in the class level and it will find the class attribute. So! We will have the same discount for all the instances, the one that is in the class level, and a different discount only for the instance that has the attribute in the instance level!

Yep.. Ok, that was great but a little bit (tooooooo) much. Let's summarize it in this:

**When using attributes with self, the route will be the following:**

The attribute will be searched in the instance level, if it's found great, we take it. If it's not found there, it will be searched in class level.

In instance level are those attributes that were directly assigned in the function init. In class level are the ones that are assigned in the class, outside any method.


Here the code:
```python
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

print(f"Item 2, before discount {item2.price}")
#Modifying in instance level the attribute for the instance item2 and calling the function:
item2.pay_rate = 0.7
item2.apply_discount()
print(f"Item 2, after new discount {item2.price}")

#Seeing that item1 keeps accessing the attribute from class level and therefore the pay rate is still 0.8
print(f"Item 1, Before discount: {item1.price}")
item1.apply_discount()
print(f"Item 1, After discount: {item1.price}")
```

Output: 
```shell
Item 2, before discount 1000
Item 2, after new discount 700.0
Item 1, Before discount: 100
Item 1, After discount: 80.0
```

So conclusion! If we want to be able to change attributes individually for each instance we may want to use *self* in the methods when we call a class attribute. On the other hand, if we want to have the same class attribute for allllll the instances then it's better to call the attribute directly from the class level using the name of the class, in this case: *Item.pay_rate*
## Magic attributes

Those things are really nice. Basically, we can do magic things with them. (There are also magic functions! Everything that comes with __ double underscore is kind of magic! Like the function init. Jap. It also belongs to the magic group as a magic function)

In this case, we can see:

### .__dict__

With this magic attribute we can have in a dictionary all the attributes! If we apply it to a class, then we will have all the class attributes. If we apply it to an instance, then we will have all the instance attributes. Taraaaaaaaaaaaan:

```python
print(f"Class attributes {Item.__dict__}")
print(f"Instance attributes {item1.__dict__}")
```

That is just the Hammer! (ein bisschen Deutsch hier, oder?) because in that way we can kind of debug or we can even check if there are more attributes in an specific instance since we already know that we can assign attributes to specific instances individually. :D

## Extension to check spell mistakes!

Yap, I know it may be not part of the topics of OOP but this was toooo good that I had to mention it. We just installed an extension called Code Spell Checker. The problem was that it was reporting the spell mistakes as problems in the code. We just fixed that modifying the settings.json file and it was greaaat. First time I did it understanding. For more info visit this [link](https://stackoverflow.com/questions/50309834/vs-code-enable-inline-spell-checker-but-disable-spell-check-in-the-problems).

Now yes, let's go on with OOP.

## Creating a list to save all instances of a class

Well, now let's say that we will continue to create many instances of a class. It would be really nice to have access to all the instances that we created. We can do this by having a class attribute of type list. In this list we can append the instances just when we create them. This can be done in the init method for example.

Class attribute and appending action when an instance is created:

```python
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
    ...
```

Now if want to know which instances we have, we can directly know it accessing to the attribute *all*. That sounds good, however if we directly print the list or an element with the print function, doing this:

```python
print(Item.all)
print(item3)
```

We will get an output that doesn't have the info but the location in memory of the variable (object), like this:

```shell
[<__main__.Item object at 0x000002C10BF3AFD0>, <__main__.Item object at 0x000002C10BF3AF70>, <__main__.Item object at 0x000002C10BF3AEB0>, <__main__.Item object at 0x000002C10BF3ADC0>, <__main__.Item object at 0x000002C10BF3AD60>]
<__main__.Item object at 0x000002C10BF3AEB0>
```

And yes... we understand it but! We can fix it by doing the following thing: Magic! Yes. Here comes a magic method called __repr __. In this we define the output that we want to get when we directly print an instance of a class.

In our case:

```python
def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity})"
```

And if we print again then we will get an output exactly with the format that we specified:

```shell
[Item('Phone', 80.0, 6), Item('Laptops', 700.0, 0), Item('Cable', 10, 5), Item('Mouse', 50, 5), Item('Keyboard', 75, 5)]
Item('Cable', 10, 5)
```

Yes. Magic is magic!
