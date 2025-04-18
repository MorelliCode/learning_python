# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old), except don’t explicitly write out the year. Use the built-in Python datetime library to make the code you write work during every year, not just the one we are currently in.
import datetime

name = input("What's your name? \n")
age = input("What's your age? \n")

def calc_centennial(age):
    centennial_year = 100 - int(age) + datetime.datetime.now().year
    return centennial_year

print(f"{name}, you will turn 100 years old on the year {calc_centennial(age)}.")