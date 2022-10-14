# Python Object-Oriented Programming
## 4 Pillars of OOP
### Methods/functions
#### Modules
##### Lib - Packages

#### Use case - benefits - examples of builtin modules - packages
- Lucky draw, inside python modules, we have one called random. Everytime you print something using this module, it will give you a random number between 0 and 1.
```python
import random

print(random.random())
```

# OOP use
### Animal 

```python
# create a class  called animal - file name start with a - class name start with A
# add the common attribute/car behaviour/function
# syntax class name: - class animal:

class Animal:  # fallow the correct naming convention & best practices
    # we need to initialise with builtin method called __init__(self)
    # self refers current class
    def __init__(self):  # any attributes attached to the class should be part of init method
        # self.var = true
        self.alive = True
        self.spine = True
        self.eyes = True

    # let's create some methods to add common behaviours
    def breath(self):
        return "Keep breathing to stay alive "

    # let's add one more behaviour
    def eat(self):
        return "time to eat"


# create an object of this class
# cat = Animal()  # creating an object of our Animal class
# print(cat.breath())  # calling a method using object of the Animal class
# print(cat.eat())
```
### reptile

```python
# create a class called Reptile
# how do we make the Animal class a parent class - how could we inherit from the Animal class


from animal import Animal # importing everything from Animal class


class Reptile(Animal): # Inherit from Animal class
    def __init__(self):
        super().__init__() # super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "keep working hard to find food! "
    def use_venom(self):
        return "if i have it, i will use it "

# smart_reptile = Reptile()
# print(smart_reptile.breath())
```
### Snakes

```python
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tounge = True

    def use_tongue_to_smell(self):
        return "if I can touch it, I can smell it"


smart_snake = Snake()
print(f"This function is called from parent class {smart_snake.hunt()}")
print(f"This function is called from the current class {smart_snake.use_tongue_to_smell()}")
print(f"This function is called from the gran parent class {smart_snake.breath()}")

# use the same .md file to add this code with your documentation 
```
