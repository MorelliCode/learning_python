# Given this solution to Exercise 9, modify it to have one level of user feedback: if the user does not enter a number between 1 and 9, tell them. Don’t count this guess against the user when counting the number of guesses they used.

# import random

# number = random.randint(1, 9)
# number_of_guesses = 0
# while True:
# 	guess = int(input("Guess a number between 1 and 9: "))
# 	number_of_guesses += 1
# 	if guess == number:
# 		break
# print(f"You needed {number_of_guesses} guesses to guess the number {number}")

import random

number = random.randint(1, 9)
number_of_guesses = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess > 9 or guess < 1:
            print("Not a valid number. Try again.")
            continue
        else:
            number_of_guesses += 1
        if guess == number:
            break
    except ValueError:
        print("Oops, that's not a number. Try again.")
        
print(f"You needed {number_of_guesses} guesses to guess the number {number}")