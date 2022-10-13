# Lucky draw
# key word called import
# import random
#
# print(random.random())
#each  time it's run, it generates a random number

# from random import random
# import math
#
# print(random())
# calculate DOB or year of birth

# number = 23.66
# any number - to round the figure up
# number .50 above to round up
# number 1.49 or less round down to 1
# print(math.ceil(number)) # ceil will round the figure up
# print(math.ceil(number)) # floor will help you round the figure to bottom

# import os
# import datetime, sys
# print(os.cpu_count()) # this will result in number of cpu based on your OS
# print(datetime.date.today()) # this will result today's date
# print(sys.path)
# don't repeat yourself (DRY)
# reusable - saves time - save money
# let's build some function
# it's part of your exam
# syntax def name() - def name(): - def name:
# def greeting():
#     # greet the user
#     print("Hello Dear")
#     pass
    # keyword called pass
# unless the function is called it does nothing
# greeting()
# greet the user with their name


# def greeting_user(name): # create a function that takes an arg - the name
#     print("Hello Dear " + name) # adding the 2 string user input()
#     pass
#
# greeting_user("sparta")
# let's create a function that takes int as an args
# def add(value1, value2):
#     # print(value1 + value2)
# # return statement
#     return value1 + value2
#
# add(2, 2)






#   create a simple calculate
# the functions are *, / and reminder

def multiply(value1, value2): # takes in two values from the user
    return value1 * value2 # returns the answer to user after multiplying them
def divide(value1, value2): # takes in two value from user
    return value1/value2 # returns the two values after dividing value1 over value2
def remainder(value1, value2): #takes in two values from the user
    return value1%value2 # return the remainder when your divide value1 over value2
print(multiply(2, 3)) # prints the return statement after calling "multiply" function
print(divide(9, 3))
print(remainder(9, 4))



