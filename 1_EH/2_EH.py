import os
os.system('cls')

# raise
# عمل میکنه و دیگه نیاز نداره و می تونی متن ارور رو تغییر بدی return مثل
# except رو نمایش نده تا بری برسی به  raise خط های بعد از
# ندیدی ارور رو نمایش بده except اگر هم


def calc_income(income):
    if income < 0:
        raise Exception("Income Should not be a negetive number!")
    return income * 2


user_number = int(input("Enter Number: "))

print(calc_income(user_number))
