#  This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

# Happy coding!

bdate_dictionary = {
    "Leonardo da Vinci": "15/04/1452",
    "Galileo Galilei": "15/02/1564",
    "Isaac Newton": "25/12/1642",
    "Maria Sibylla Merian": "02/04/1647",
    "Charles Darwin": "12/02/1809",
    "Ada Lovelace": "10/12/1815",
    "Marie Curie": "07/11/1867"
}

def welcome_message():
    print("Welcome to the birth date dictionary. We know the birth dates of:")
    for key in bdate_dictionary:
        print(key)

def return_bdate():
    while True:
        name = input("Whose birth date do you want to look up?\n")
        if name in bdate_dictionary:
            print(name + "'s birth date is " + bdate_dictionary[name] + ".")
        else:
            print("That name is not in the list. Are you sure you typed it correctly?")

welcome_message()
return_bdate()