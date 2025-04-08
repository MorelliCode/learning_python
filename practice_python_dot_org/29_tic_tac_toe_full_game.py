#  This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

#     Draw the Tic Tac Toe game board
#     Checking whether a game board has a winner
#     Handle a player move from user input

# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

#     You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
#     If there are no more moves left, don’t ask for the next player’s move!

# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
loop = True
player_turn = 1
gameboard = [['.', '.', '.'], 
             ['.', '.', '.'], 
             ['.', '.', '.']]

def draw_board(list_of_lists):
    print(" --- --- --- ")
    print("| " + list_of_lists[0][0] + " | " + list_of_lists[0][1] + " | " + list_of_lists[0][2] + " |")
    print(" --- --- --- ")
    print("| " + list_of_lists[1][0] + " | " + list_of_lists[1][1] + " | " + list_of_lists[1][2] + " |")
    print(" --- --- --- ")
    print("| " + list_of_lists[2][0] + " | " + list_of_lists[2][1] + " | " + list_of_lists[2][2] + " |")
    print(" --- --- --- ")

def player_play(player_number):
    global gameboard
    while True:
        player_input_row = int(input("Player " + str(player_number) + " please input your row number: ")) - 1
        player_input_column = int(input("Player " + str(player_number) + " please input your column number: ")) - 1
        #error catcher
        if player_input_column > 2 or player_input_column < 0:
            print("There was an error...")
            continue
        elif player_input_row > 2 or player_input_row < 0:
            print("There was an error...")
            continue
        elif gameboard[player_input_row][player_input_column] != '.':
            print("That square is already taken. Try again.")
            continue
        #inputs play depending on player
        if player_turn == 1:
            gameboard[player_input_row][player_input_column] = "X"
        else:
            gameboard[player_input_row][player_input_column] = "O"
        break        

def check_winner(list_of_lists):
    global loop
    #checks if there are available squares to play, if now end program in a draw
    if '.' not in list_of_lists[0] and '.' not in list_of_lists[1] and '.' not in list_of_lists[2]:
        draw_board(list_of_lists)
        print("No one wins, it's a DRAW!")
        loop = False
    #main win logic
    #check diagonals
    if list_of_lists[0][0] == list_of_lists[1][1] == list_of_lists[2][2]:
        winner = list_of_lists[0][0]
    elif list_of_lists[0][2] == list_of_lists[1][1] == list_of_lists[2][0]:
        winner = list_of_lists[0][2]
    #check horizontals
    elif list_of_lists[0][0] == list_of_lists[0][1] == list_of_lists[0][2]:
        winner = list_of_lists[0][0]
    elif list_of_lists[1][0] == list_of_lists[1][1] == list_of_lists[1][2]:
        winner = list_of_lists[1][0]
    elif list_of_lists[2][0] == list_of_lists[2][1] == list_of_lists[2][2]:
        winner = list_of_lists[2][0]
    #check verticals
    elif list_of_lists[0][0] == list_of_lists[1][0] == list_of_lists[2][0]:
        winner = list_of_lists[0][0]
    elif list_of_lists[0][1] == list_of_lists[1][1] == list_of_lists[2][1]:
        winner = list_of_lists[0][1]
    elif list_of_lists[0][2] == list_of_lists[1][2] == list_of_lists[2][2]:
        winner = list_of_lists[0][2]
    else:
        return
    
    if winner == '.':
        return
    
    show_winner(winner)

def show_winner(player_symbol):
    draw_board(gameboard)
    if player_symbol == "X":
        player_number = 1
    else:
        player_number = 2
    print("Congratulations, Player " + str(player_number) + "! You are the winner!")
    global loop
    loop = False


def pass_turn():
    global player_turn
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1

while loop:
    draw_board(gameboard)
    player_play(player_turn)
    check_winner(gameboard)
    pass_turn()