n = 94
guess = 9
rule = "Guess the number within 9 tries"
print(rule.upper())
print("NOTE:= the number is between 1 to 50")
while (True):
    user = int(input("Enter the number\n"))
    if user > n:
        guess = guess - 1
        print("Greater number make it lower")
        print(guess, "guesses left\n")
        continue
    elif user == n:
        print("Congratulation you won by", 10 - guess, "guesses")
        break
    elif guess == 1:
        print("Game over out of tries")
        break
    else:
        guess = guess - 1
        print("Lower number make it Greater")
        print(guess, "guesses left\n")
        continue
