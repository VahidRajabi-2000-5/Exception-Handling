import os
os.system('cls')


def fact(num):
    assert num >=0, "fact should not be a negetive number!"
    result = 1
    for i in range(1,num+1):
        result *= i
    return result


user_number = int(input("enter number: "))
print(fact(user_number))
