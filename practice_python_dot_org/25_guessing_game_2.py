# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)


#number_range = [x for x in range(int(input("What's the range of guesses?")) + 1)]

def start_game():
    print("Let's play a guessing game.")
    number_range = [x for x in range(int(input("You think of a number between 0 and (input a number now): ")) + 1)]
    return number_range

def main_loop(number_range):
    loop = True
    tries = 0
    start_index = 0 
    end_index = len(number_range) - 1
    while loop:
        tries += 1
        middle_index = (start_index + end_index) // 2
        middle_value = number_range[middle_index]
        
        if start_index > end_index or end_index < start_index:
            return "There has been a problem. Did you lie to me?"
        
        print("Is your number " + str(middle_value) + " ?")
        user_response = int(input("Was my guess:\n[1] Too high\n[2] Too low\n[3] Right on the spot? "))

        if user_response == 1:
            end_index = middle_index - 1 
        elif user_response == 2:
            start_index = middle_index + 1
        else:
            return "HA! I knew it! It only took " + str(tries) + " tries!"
        
print(main_loop(start_game()))