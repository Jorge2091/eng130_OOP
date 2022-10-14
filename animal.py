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
