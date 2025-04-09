#  This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

# An example interaction can look like this:

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...

# And so on, until the player gets the word.

chosen_word = "EVAPORATE"
to_guess_lines = []
letters_guessed = []
loop = True

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

def check_winner(list_of_lists):
    global loop
    if list_of_lists[0] == list_of_lists[1]:
        print(" ".join(list_of_lists[0]))
        print("Congratulations! You win!")
        loop = False

    
    
print("Welcome to hangman!")
to_guess_lines = guess_lines(chosen_word)
#print(to_guess_lines)

while loop:
    display_game(to_guess_lines)
    check_guess(ask_for_guess())
    check_winner(to_guess_lines)
