import os
os.system('cls')


def fact(num):
    # در حالتی هست که اتفاقی به هیچ وجه نباید بیوفته اگر افتاد ارور بده با متن رو به روش
    assert num >=0, "fact should not be a negetive number!"
    result = 1
    for i in range(1,num+1):
        result *= i
    return result


user_number = int(input("enter number: "))
print(fact(user_number))
