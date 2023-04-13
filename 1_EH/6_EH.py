import os
os.system('cls')

# ساخت ارور دلخواه و تغییر آن به کمک وراثت

class NegetiveAgeError(Exception):
    def __init__(self, massage, age):
        self.massage = massage
        self.age = age


def check_age(age): 
    if age < 0:
        raise NegetiveAgeError('Your age can not be negetive', age)
    return age * 2


user_age = int(input("enter your age: "))

try:
    print(check_age(user_age))
except NegetiveAgeError as e:
    print(e.massage, e.age)
