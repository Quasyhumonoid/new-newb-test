
def translate(phrase):
    #for each vowel in the input, change it to a g
    translation = ""
    for letter in phrase:
        if letter.lower in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("enter phrase to translate. ")))