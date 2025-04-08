#  This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.

import random
word_list = []

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

word_list = import_list("30.txt")
print(pick_word(word_list))
