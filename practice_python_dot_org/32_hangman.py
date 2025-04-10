#  This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

#     Only let the user guess 6 times, and tell the user how many guesses they have left.
#     Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

# Optional additions:

#     When the player wins or loses, let them start a new game.
#     Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

# Your solution will be a lot cleaner if you make use of functions to help you!

import random
word_list = []
chosen_word = ""
to_guess_lines = []
letters_guessed = []
number_of_tries = 6
loop = True

def import_list(file):
    #start by opening the file, reading each line while stripping it of newline and possible white spaces
    #Then return the list
    with open(file, "r") as file_list:
        line = file_list.readline().strip()
        lines = []
        while line:
            lines.append(line)
            line = file_list.readline().strip()
        return lines

def pick_word(word_list):
    chosen_word = random.choice(word_list)
    return chosen_word

def guess_lines(word):
    to_guess = [[],[]]
    for letter in word:
        to_guess[0].append("_")
        to_guess[1].append(letter)
    return  to_guess

def display_game(list_of_lists):
    print(" ".join(list_of_lists[0]))
    if len(letters_guessed) > 0:
        print("You've already guessed: " + " ".join(letters_guessed)) 

def display_drawing(number_missed_guesses):
    line_hor = "____"
    line_vert = "|"
    line_2 = "  O"
    line_3_1 = "  |"
    line_3_2 = " /|"
    line_3_3 = " /|\\"
    line_4_1 = " /"
    line_4_2 = " / \\"
    print(line_hor)
    if number_missed_guesses == 0:
        print(line_vert)
        print(line_vert)
        print(line_vert)
    elif number_missed_guesses == 1:
        print(line_vert + line_2)
        print(line_vert)
        print(line_vert)
    elif number_missed_guesses == 2:
        print(line_vert + line_2)
        print(line_vert + line_3_1)
        print(line_vert)
    elif number_missed_guesses == 3:
        print(line_vert + line_2)
        print(line_vert + line_3_2)
        print(line_vert)
    elif number_missed_guesses == 4:
        print(line_vert + line_2)
        print(line_vert + line_3_3)
        print(line_vert)
    elif number_missed_guesses == 5:
        print(line_vert + line_2)
        print(line_vert + line_3_3)
        print(line_vert + line_4_1)
    elif number_missed_guesses == 6:
        print(line_vert + line_2)
        print(line_vert + line_3_3)
        print(line_vert + line_4_2)
    else:
        print("ERROR")
    print(line_vert)
    
def ask_for_guess():
    lower_letters = [chr(x) for x in range(97, 123)]
    upper_letters = [chr(x) for x in range(65, 91)]
    while True:
        letter_guess = input("Guess a letter: ")
        letter_guess = letter_guess.upper()
        if len(letter_guess) > 1:
            print("I said, guess A (1) letter. Try again.")
            continue
        if letter_guess not in upper_letters and letter_guess not in lower_letters:
            print("I said, guess a LETTER. Try again.")
            continue
        elif letter_guess in letters_guessed or letter_guess in to_guess_lines[0]:
            print("You've already guessed that letter. Try again.")

        return letter_guess

def check_guess(letter):
    global to_guess_lines
    global letters_guessed
    for i in range(len(to_guess_lines[1])):
        if letter == to_guess_lines[1][i]:
            to_guess_lines[0][i] = letter
    if letter not in to_guess_lines[1] and letter not in letters_guessed:
        letters_guessed.append(letter)
        letters_guessed = sorted(letters_guessed)
        print("Incorrect!")

def check_result(list_of_lists):
    global loop
    if list_of_lists[0] == list_of_lists[1]:
        print(" ".join(list_of_lists[0]))
        print("Congratulations! You win!")
        loop = False
        play_again()
    elif len(letters_guessed) == number_of_tries:
        display_drawing(len(letters_guessed))
        print("You've exhausted your tries. You lose.")
        loop = False
        play_again()
    else:
        print("You still have " + str(number_of_tries - len(letters_guessed)) + " incorrect guesses left.")

def play_again():
    while True:
        play_again_input = input("Would you like to play another game? yes/no\n")
        if play_again_input == "yes":
            return
        elif play_again_input == "no":
            exit()
        else:
            print("You have to type 'yes' or 'no'. Try again.")

while True:
    print("Let's play hangman!")
    print("You have a total of " + str(number_of_tries) + " possible incorrect guesses.")
    print("If you exhaust your number of guesses, you lose.")
    word_list = import_list("30.txt")
    chosen_word = pick_word(word_list)
    to_guess_lines = guess_lines(chosen_word)
    loop = True
    letters_guessed = []
    #uncomment the following line for debug purposes
    #print(to_guess_lines)

    while loop:
        display_drawing(len(letters_guessed))
        display_game(to_guess_lines)
        check_guess(ask_for_guess())
        check_result(to_guess_lines)
