# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old), except use f-strings instead of the + operator to print the resulting output message.

name = input("What's your name? \n")
age = input("What's your age? \n")

def calc_centennial(age):
    current_year = 2025
    centennial_year = 100 - int(age) + current_year
    return centennial_year

print(f"{name}, you will turn 100 years old on the year {calc_centennial(age)}.")