#  This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

# Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def check_winner(list_of_lists):
    winner = 0
    #check diagonals
    if list_of_lists[0][0] == list_of_lists[1][1] and list_of_lists[1][1] == list_of_lists[2][2]:
        winner = list_of_lists[0][0]
    elif list_of_lists[0][2] == list_of_lists[1][1] and list_of_lists[2][0]:
        winner = list_of_lists[0][2]
    #check horizontals
    elif list_of_lists[0][0] == list_of_lists[0][1] and list_of_lists[0][1] == list_of_lists[0][2]:
        winner = list_of_lists[0][0]
    elif list_of_lists[1][0] == list_of_lists[1][1] and list_of_lists[1][1] == list_of_lists[1][2]:
        winner = list_of_lists[1][0]
    elif list_of_lists[2][0] == list_of_lists[2][1] and list_of_lists[2][1] == list_of_lists[2][2]:
        winner = list_of_lists[2][0]
    #check verticals
    elif list_of_lists[0][0] == list_of_lists[1][0] and list_of_lists[1][0] == list_of_lists[2][0]:
        winner = list_of_lists[0][0]
    elif list_of_lists[0][1] == list_of_lists[1][1] and list_of_lists[1][1] == list_of_lists[2][1]:
        winner = list_of_lists[0][1]
    elif list_of_lists[0][2] == list_of_lists[1][2] and list_of_lists[1][2] == list_of_lists[2][2]:
        winner = list_of_lists[0][2]
    else:
        return
    
    if winner == 0:
        return
    
    return winner

def show_result(player_number):
    if player_number == None:
        print("No one wins, DRAW!")
    else:
        print("Player " + str(player_number) + " is the winner!")

show_result(check_winner(winner_is_1))
show_result(check_winner(winner_is_2))
show_result(check_winner(winner_is_also_1))
show_result(check_winner(no_winner))
show_result(check_winner(also_no_winner))
        