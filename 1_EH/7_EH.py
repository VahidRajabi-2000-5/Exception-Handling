import os
os.system('cls')

# چک کردن ورودی گرفتن


def check_input():
    result = None
    while True:
        user_number = input("Enter number: ")
        try:
            result = int(user_number)
            break
        except ValueError:
            try:
                result = float(user_number)
                break
            except ValueError:
                print("Try again !")

    print(type(result))
    print(f"Result: {result}")


check_input()
