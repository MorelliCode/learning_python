# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra:

#     Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.


with open('22_1.txt', 'r') as open_file:
    line = open_file.readline()
    count = {}
    while line:
        new_line = line.rstrip("\n")
        if new_line not in count:
            count[new_line] = 0
        else:
            count[new_line] += 1
        line = open_file.readline()
    print(count)

with open("22_2.txt", "r") as open_file:
    line = open_file.readline()
    count = {}
    while line:
        new_line = 