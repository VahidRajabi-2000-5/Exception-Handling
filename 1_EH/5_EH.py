import os
os.system('cls')

a = 10
b = int(input("enter number: "))

try: #  Try to run this code
    # print(a/b)
    b = C+10
except ZeroDivisionError as z:  # if this exception happended
    print("EXCEPTIONs: ", z)
except ModuleNotFoundError as m:  # if this exception happended
    print("EXCEPTIONss: ", m)
except Exception as e:  # if this exception happended
    print("EXCEPTIONsss: ", e)
#اتفاق نیوفتاده باشد try در حالتی است که هیچ اروری در else
else:  # If there is no error
    print("Not Error.")
# چه به ارور خوردی چه به ارور نخوردی فاینالی رو اجرا کن
# مثلا در ماشینی رو باز کردی و به ارور خوردی در باز موند در فاینالی میای و اون در رو میبندی
finally:
    print("FINALLY")

print("END.")
