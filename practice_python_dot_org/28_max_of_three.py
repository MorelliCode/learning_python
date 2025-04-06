# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

print("Give me three numbers, and I'll tell you the highest one of them!")
input_1 = int(input("Give me a number: "))
input_2 = int(input("Give me a second number: "))
input_3 = int(input("Give me a third number: "))
highest = 0

if input_1 > input_2:
    highest = input_1
else:
    highest = input_2

if input_3 > highest:
    highest = input_3

print("The highest number is " + str(highest) + ".")

