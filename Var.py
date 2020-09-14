
character_one = "sick af"
character_one_age = "-0"

print("there was once a man named " + character_one + ", ")
print("he was " + character_one_age + " years old")
print("he really liked the name " + character_one + "")
print("but didn't like being " + character_one_age + ".")
character_one_age = "0"
print("luckily after waiting a year his new age was " + character_one_age + ".")

num = 1
#print(num + character_one_age)
#doesn't work because str and int or float can't be added
age = int(character_one_age) #change variable string to integer
print(num + age)
num = float(1.5) #number with a decimal is a float
#this was unecessary to declare as a float but I declared it anyway
print(num + age) #float and int are compatible in most situations
answer = "True"
answer = bool(answer) #converts any string except 0 or blank to boolean True
print(answer)
#if variable is formatted correctly when declared it will automatically
# format type. Values from input are always strings.
