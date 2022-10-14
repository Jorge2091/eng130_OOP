# class Assess:
def largest(numbers):
    a = 0
    for number in numbers:
        if a < number:
            a = number
        else:
            a = a
    return a

def is_twin(a, b):
    a = a.lower()
    b = b.lower()
    check = True
    for letter in b:
        if a.find(letter) == -1:
            check = False
            break
    return check

def password(passwords):
    if len(passwords)<5:
        return "Your password is too short"
    elif len(passwords)>20:
        return "Your password is too long and may be forgotten."
    else:
        return "Your password is an acceptable length"

def find_smallest_interval(lists):
    y = sorted(lists)
    last = y[0]
    n = 0
    last_interval = y[-1] - y[0]
    for number in y:
        interval = number - last
        if interval <= last_interval and n != 0:
            last_interval = interval
            last = number
            n += 1
        else:
            last = number
            n += 1
    return last_interval

