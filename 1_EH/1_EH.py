import os
os.system('cls')

print("START")

user_number = int(input("enter number: "))

try:
    print("first")
    print(100/user_number)
    print("Third")
except:
    print("exception occured")


print("END")

# خروچی اول
# START
# enter number: 10
# first
# 10.0
# Third
# END
# ====================
# خروجی دوم
# START
# enter number: 0
# first
# exception occured
# END
