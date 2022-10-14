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

