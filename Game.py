
secret_word = "giglioplex"
guess = ""
guess_count = 0
guess_out = False
guess_limit = 8

while secret_word != guess and not(guess_out):
    guess = input("Enter your guess: ")
    guess_count += 1
    if secret_word == guess:
        print("Good Job!")
    elif secret_word != guess and guess_limit - guess_count == 1:
        print("Guess again :/ You have " + str(guess_limit - guess_count) + " more guess.")
        length = len(secret_word)
        Correct = 0
        while length >= 0:
            try:
                if secret_word[length - 1] == guess[length - 1]:
                    Correct += 1
            except:
                pass
            length -= 1
        if Correct == 1:
            print("You have 1 Character in the correct position.")
        else:
            print("You have " + str(Correct) + " Characters in the correct positions.")
    elif secret_word != guess and guess_count < guess_limit:
        print("Guess again :/ You have " + str(guess_limit - guess_count) + " more guesses.")
        length = len(secret_word)
        Correct = 0
        while length >= 0:
            try:
                if secret_word[length - 1] == guess[length - 1]:
                    Correct += 1
            except:
                pass
            length -= 1
        if Correct == 1:
            print("You have 1 Character in the correct position.")
        else:
            print("You have " + str(Correct) + " Characters in the correct positions.")
    else:
        guess_out = True

if not(guess_out):
    print("You win!")
elif guess_out:
    print("You Lose :(")
if guess_count == 1:
    print("You knew it all along!")
else:
    print("You took " + str(guess_count) + " guesses.")