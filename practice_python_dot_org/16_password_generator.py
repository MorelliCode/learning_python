# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random

letters_lower = [chr(i) for i in range(97, 123)] #loop through lower-case alphabet
letters_upper = [chr(i) for i in range(65, 91)] #loop through upper-case alphabet
numbers = [str(i) for i in range(0, 10)] #loop through numbers 0-9
symbols = [chr(i) for i in range(33, 48)] #loop through symbols !"#$%&'()*+,-./
loop = True

def get_input():
    user_choice = int(input("Choose password strength:\n[1] weak\n[2] medium\n[3] strong\n"))
    return user_choice

def sort_input(choice):
    if choice == 1:
        create_weak_password()
    elif choice == 2:
        create_medium_password()
    elif choice == 3:
        create_strong_password()
    else: 
        print("There has been an error")
    

def create_weak_password():
    weak_password = random.choices(letters_lower, k=4) + random.choices(letters_upper, k=4)
    random.shuffle(weak_password)
    weak_password = "".join(weak_password)
    print(weak_password)

def create_medium_password():
    medium_password = random.choices(letters_lower, k=4) + random.choices(letters_upper, k=4) + random.choices(numbers, k=4)
    random.shuffle(medium_password)
    medium_password = "".join(medium_password)
    print(medium_password)

def create_strong_password():
    strong_password = random.choices(letters_lower, k=4) + random.choices(letters_upper, k=4) + random.choices(numbers, k=4) + random.choices(symbols, k=4)
    random.shuffle(strong_password)
    strong_password = "".join(strong_password)
    print(strong_password)

def repeat():
    while True:
        again = input("Would you like another password? yes/no\n")
        if again == "no":
            global loop
            loop = False
            return
        if again == "yes":
            return
        else:
            print("You need to type 'yes' or 'no'")

while loop == True:
    sort_input(get_input())
    repeat()