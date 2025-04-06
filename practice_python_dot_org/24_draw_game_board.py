#  This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

# Remember that in Python 3, printing to the screen is accomplished by

#   print("Thing to show on screen")

# Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.

grid_size = int(input("What grid size would you like? "))
vertical = "|   "
horizontal = " ---"


def print_horizontal(grid_size):
    print(horizontal * grid_size)

def print_vertical(grid_size):
    print((vertical * grid_size) + vertical)

def draw_board(grid_size):
    i = grid_size
    print_horizontal(grid_size)
    while i != 0:
        print_vertical(grid_size)
        print_horizontal(grid_size)
        i -= 1

draw_board(grid_size)