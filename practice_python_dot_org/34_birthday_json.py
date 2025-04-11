#  This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json
json_file = "34.json"
bdate_dictionary = {}
loop_read = False
loop_write = False

def read_from_file(file):
    with open(file, "r") as f:
        return json.load(f)
    
def write_to_file(file):
    with open(file, "w") as f:
        json.dump(bdate_dictionary, f)

def welcome_message():
    global loop_read
    global loop_write
    print("Welcome to the birth date dictionary.")
    print("If you'd like to know a specific birthdate, type 'read'")
    print("If you'd like to add a name and birth date to the list, type 'write'")
    print("If you'd like to exit, type 'exit'")
    while True:
        choice = input()
        if choice == "read":
            loop_read = True
            loop_write = False
            break
        elif choice == "write":
            loop_read = False
            loop_write = True
            break
        elif choice == "exit":
            print("Goodbye!")
            exit()
        else:
            print("Please type 'read', 'write, or 'exit'.")

def display_read_message(dictionary):
    print("We know the birth date of the following people:")
    for key in dictionary:
        print(key)

def return_bdate(dictionary):
    while True:
        name = input("Whose birth date do you want to look up?\n")
        if name in dictionary:
            print(name + "'s birth date is " + dictionary[name] + ".")
            break
        else:
            print("That name is not in the list. Are you sure you typed it correctly?")

def another_read():
    global loop_read
    while True:
        choice = input("Would you like to know another person's birth date? yes/no: ")
        if choice == "yes":
            break
        elif choice == "no":
            loop_read = False
            break
        else:
            print("You need to type 'yes' or 'no'.")

def display_write_message():
    print("Let's add a name and a birth date to the list.")

def write_bdate():
    global bdate_dictionary
    name = input("What is the name of the person? ")
    bdate = input("What is the birthdate of the person (day/month/year)? ")
    bdate_dictionary[name] = bdate
       
def another_write():
    global loop_write
    while True:
        choice = input("Would you like add another person's birth date? yes/no: ")
        if choice == "yes":
            break
        elif choice == "no":
            loop_write = False
            break
        else:
            print("You need to type 'yes' or 'no'.") 

while True:
    bdate_dictionary = read_from_file(json_file)
    welcome_message()

    while loop_read == True:
        display_read_message(bdate_dictionary)
        return_bdate(bdate_dictionary)
        another_read()
    
    while loop_write == True:
        display_write_message()
        write_bdate()
        write_to_file(json_file)
        another_write()