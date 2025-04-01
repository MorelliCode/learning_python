# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

random_number = random.randint(1, 50)
play_another = "yes"


while play_another == "yes":
    user_guess = int(input("Guess a number:\n"))
    if user_guess == random_number:
        print("Right on the spot. Congratulations, you've guessed the number!")
        play_another = input("Would you like to play again? yes/no: ")
    elif user_guess > random_number:
        print("Too high, try again.")
    elif user_guess < random_number:
        print("Too low, try again.")
    else:
        print("Something went wrong... Try again")
