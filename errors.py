
try:
    num = int(input("Enter a number "))
    print(num)
except ZeroDivisionError as err: #this prints if you divide by zero --"as" assigns the error description to the variable "err"
    print(err)
except ValueError: #this prints if you give the wrong type of value
    print("invalid input")
#except:
#    pass
#pass should only be used if you know there can't be an error that could cause problems
