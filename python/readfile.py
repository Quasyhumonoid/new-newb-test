employees = open("employees.txt", "r")
# r: read
# w: write
# a: append (add too the end)
# r+: read and write
print(employees.readable()) #checks if file can be read
print(employees.read()) #prints the file contents
print(employees.readline()) #prints the first line of the file
print(employees.readline()) #prints the following line
print(employees.readlines()) #puts lines in a list and prints it
for employee in employees.readlines():
    print(employee)
employees.close()

employees = open("employees.txt", "a")
employees.write("\ntoby")
employees.close()
employees = open("employees.txt", "w") #if the file listed doesn't exist it will be created.
employees.write()
employees.close()