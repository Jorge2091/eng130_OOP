# s = 'python is fun'
# c = 'I'
# print(s.find(c))
#
y = [-1, 9, 0, 8, -5, 6, -24]
# print(y.sort())

def max(data):
    # we get a list and consecutively add the range of best profit and the index of the start of that range, print out the index and the range

    # make a for function that goes one by one
    # add the value from the a profit of 0, if there is a profit, the output will be positive
    start = 0
    ind = 0
    range = 0
    good_range = 0
    index_start = 0
    max_profit = 0
    last = 0
    state = True
    ran = False
    last_profit = 0
    for profit in data:
        if ran:
            range += 1
        start = profit + last
        if start > max_profit:
            max_profit = profit + last
            last = profit + last
            if state:
                index_start = ind
                state = False
            ind += 1
            ran = True
        elif max_profit < 0:
            range = 0
            state = True
            ren = False

        else:
            ind += 1

    return [index_start, range]




fruits = {"apple", "banana", "cherry"}
fruit = ["apple", "banana", "cherry"]
fruit.add("jock")

print(fruits)