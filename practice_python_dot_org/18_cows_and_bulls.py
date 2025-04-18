# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...

# Until the user guesses the number.

import random

number = random.choices(range(0, 10), k=4)
tries = 0
loop = True

#gets input from player
def get_input():
    player_guess = input("Guess a four-digit number: ")
    player_list = [x for x in player_guess]
    return player_list

#check if input is only numbers and 4 digits, then creates a list with integers, then calls the main game function with the list
def check_input(player_list):
    numbers = [str(i) for i in range(0, 10)]
    
    for item in player_list:
        if item not in numbers:
            print("I said a four-digit NUMBER. Try again.")
            return
    
    if len(player_list) > 4 or len(player_list) < 4:
        print("I said a FOUR-digit number. Try again.")
        return
    
    new_player_list = [int(x) for x in player_list]

    cows_bulls(new_player_list)    

#main game function, prints results of guess, calls win function if needed
def cows_bulls(player_list):
    global tries
    tries += 1
    new_numbers = []
    cows = 0
    bulls = 0
    player_list2 = player_list.copy()

    for item in range(len(player_list)):
        if player_list[item] == number[item]:
            cows += 1
            player_list2.remove(player_list[item])
        else:
            new_numbers.append(number[item])

    while len(new_numbers) != 0:
        if new_numbers[0] in player_list2:
            bulls += 1
        del new_numbers[0]

    print_result(cows, bulls)

    if cows == 4:
        win()

def print_result(cows, bulls):
    if cows == 1:
        print("1 Cow")
    else:
        print(str(cows) + " Cows")
    if bulls == 1:
        print("1 Bull")
    else:
        print(str(bulls) + " Bulls")

def win():
    if tries == 1:
        print("You win! It only took you 1 try! Are you a wizard?")    
    else:
        print("You win! It only took you " + str(tries) + " tries!")
    global loop
    loop = False
#Uncomment the following line to help with debugging
#print(number)

while loop:
    check_input(get_input())
