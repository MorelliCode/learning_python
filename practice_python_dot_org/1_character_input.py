# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Extras:

#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("What's your name? \n")

print("Thanks!")

age = input("What's your age? \n")

def calc_centennial(age):
    current_year = 2025
    centennial_year = 100 - int(age) + current_year
    return centennial_year

message = "You will turn 100 years old on the year " + str(calc_centennial(age))

print(message)

repeat = input("How may times would you like to hear this message again? \n")

print((message + "\n") * int(repeat))