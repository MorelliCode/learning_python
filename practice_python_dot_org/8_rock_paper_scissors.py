# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

play_another = "yes"
player1_input = 0
player2_input = 0

while play_another == "yes":
    print("Let's play rock, paper, scissors!")
    player1_input = int(input("Player 1, enter a number: \n 1-rock \n 2-paper \n 3-scissors \n"))
    player2_input = int(input("Player 2, enter a number: \n 1-rock \n 2-paper \n 3-scissors \n"))

    if player1_input == 1 and player2_input == 3:
        print("Rock beats scissors. Player 1 Wins")
    elif player1_input == 3 and player2_input == 1:
        print("Rock beats scissors. Player 2 Wins")
    elif player1_input == 2 and player2_input == 1:
        print("Paper beats rock. Player 1 Wins")
    elif player1_input == 1 and player2_input == 2:
        print("Paper beats rock. Player 2 Wins")
    elif player1_input == 3 and player2_input == 2:
        print("Scissors beat paper. Player 1 Wins")
    elif player1_input == 2 and player2_input == 3:
        print("Scissors beat paper. Player 2 Wins")
    elif player2_input == player2_input:
        print("It's a tie!")
    else:
        print("Something went wrong. Try again.")
    
    play_another = input("Would you like to play another game? yes/no: ")