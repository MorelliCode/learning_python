# One area of confusion for new coders is the concept of functions (which have been addressed on this blog in exercise 11 for example). So in this exercise, we will be stretching our functions muscle by refactoring an existing code snippet into using functions.

# Here is the code snippet to refactor (taken from a correct but very repeated solution to exercise 24 on this website):

# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")
# print("|   |   |   |")
# print(" --- --- ---")

# Hint: Think about a way to refactor this using functions where generating an 8x8 or a 19x19 grid is a single change to a function call!

hor = " ---"
vert = "|   "

def draw_board(grid_number):
    counter = grid_number
    for i in range(counter):
        print(hor * counter)
        print(vert * (counter + 1))
    print(hor * counter)

draw_board(int(input("Draw a grid that is X by X squares, where X is (type a number): ")))