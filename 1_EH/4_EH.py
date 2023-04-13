import os
os.system('cls')

try:
    import zz
    # print(2/0)
    # داشته باشی "as" متونی محتوای ارور رو با
# except ZeroDivisionError as e:

# بذاری تمام ارور ها رو میگیره و محتواشونو ذخیره میکنه"Exception" اما اگر
except Exception as e:
    print("EXCEPTION: ", e)
