
def blcnvrt(boolean_string):
    # the following is my solution for intuitively converting
    # a True/False string into a boolean. because bool(anything but zero
    # or nothing) returns True. I convert the value to a list, remove false,
    # if present and then convert to boolean.
    # try:, exempt: pass is the solution I found for ignoring an error and
    # continuing my code because I don't know of a better way to remove
    # something only if it is in a list yet.
    bltbl = [boolean_string]
    try:
        bltbl.remove("False")
    except:
        pass
    boolean = bool(bltbl)
    return boolean

is_male = blcnvrt(input("You are male. True/False: "))
print(is_male)
like_male = blcnvrt(input("You are interested in men. True/False: "))
print(like_male)
if is_male and like_male or not(is_male) and not(like_male):
    print("You're gay")
elif is_male and not(like_male) or not(is_male) and like_male:
    print("You're het")

def max_num(num1, num2, num3):
    if num1 != num2:
        if num1 > num2 and num1 >= num3:
            return num1
        elif num2 > num1 and num2 >= num3:
            return num2
        else:
            return num3
    elif num1 == num2:
        if num2 <= num3:
            return num3
        elif num2 > num3:
            return num2
nm1 = input("enter number ")
nm2 = input("enter number ")
nm3 = input("enter number ")
print(max_num(nm1, nm2, nm3))

#    this was a fun little project for I was working on while learning but
#    I realized it would be quite inefficient to do it this way.
#    Its purpose was to help someone figure out their gender identity terms
#
#is_int = blcnvrt(input("You were neither born biologically male nor female. True/False: "))
#print(is_int)
#is_male = False
#
#if not(is_int):
#    is_male = blcnvrt(input("You were born biologically male. True/False: "))
#    print(is_male)
#
#is_them = blcnvrt(input("You are commonly not gender conforming. True/False: "))
#print(is_them)
#
#is_he = blcnvrt(input("You prefer using he/him pronouns True/False: "))
#print(is_he)
#is_she = False
#
#if not(is_he):
#    is_she = blcnvrt(input("You prefer using she/her pronouns True/False: "))
#    print(is_she)
#
#like_them = blcnvrt(input("You are sexually attracted to people who don't appear gender conforming. True/False: "))
#print(like_them)
#
#like_men = blcnvrt(input("You are sexually attracted to Men. True/False: "))
#print(like_men)
#
#like_w = blcnvrt(input("You are sexually attracted to Women. True/False: "))
#print(like_w)
#
#like_zoo = blcnvrt(input("You are sexually attracted to certain non-human animals. True/False: "))
#print(like_zoo)
#
#like_obj = blcnvrt(input("You are sexually attracted to certain things. True/False: "))
#print(like_obj)
#
#if is_int and is_them and is_he or like_men and like_w and like_them and like_obj and like_zoo:
#    print("You are an intersex transgender omnisexual")
#    #when using or, the combination of all variables after are
#    # compared to the combination of all variables before
#elif is_int and is_them: # elif: else if

