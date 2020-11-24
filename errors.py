
try:
    num = int(input("Enter a number "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
