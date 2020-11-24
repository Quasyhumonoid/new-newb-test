employees = open("employees.txt", "r")
# r: read
# w: write
# a: append (add too the end)
# r+: read and write
print(employees.readable())
print(employees.read())
print(employees.readline())
print(employees.readline()) #prints the following line
print(employees.readlines()) #puts lines in array and prints it
for employee in employees.readlines():
    print(employee)
employees.close()

employees = open("employees.txt", "a")
employees.write("\ntoby")
employees.close()
employees = open("employees.txt", "w")
employees.write()
employees.close()