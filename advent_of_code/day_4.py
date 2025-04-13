# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....

# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX

# Take a look at the little Elf's word search. How many times does XMAS appear?


def count_string_pattern_horizontal(pattern, string):
    count = string.count(pattern)
    return count

def replace_string_pattern_horizontal(pattern, string):
    new_string = string.replace(pattern, "____")
    return new_string

def count_list_vertical(pattern, list_of_lists):
    count = 0
    for i in range(len(list_of_lists) - 3):
        for j in range(len(list_of_lists[i])):
            if list_of_lists[i][j] == pattern[0]:
                if list_of_lists[i+1][j] == pattern[1]:
                    if list_of_lists[i+2][j] == pattern[2]:
                        if list_of_lists[i+3][j] == pattern[3]:
                            count += 1
    return count

def replace_vertical_list_pattern(pattern, list_of_lists):
    new_list_of_lists = list_of_lists.copy()
    for i in range(len(new_list_of_lists) - 3):
        for j in range(len(new_list_of_lists[i])):
            if new_list_of_lists[i][j] == pattern[0]:
                if new_list_of_lists[i+1][j] == pattern[1]:
                    if new_list_of_lists[i+2][j] == pattern[2]:
                        if new_list_of_lists[i+3][j] == pattern[3]:
                            new_list_of_lists[i][j] = "_"
                            new_list_of_lists[i+1][j] = "_"
                            new_list_of_lists[i+2][j] = "_"
                            new_list_of_lists[i+3][j] = "_"
    return new_list_of_lists

def count_list_diagonal_forward(pattern, list_of_lists):
    count = 0
    for i in range(len(list_of_lists) - 3):
        for j in range(len(list_of_lists[i]) - 3):
            if list_of_lists[i][j] == pattern[0]:
                if list_of_lists[i+1][j+1] == pattern[1]:
                    if list_of_lists[i+2][j+2] == pattern[2]:
                        if list_of_lists[i+3][j+3] == pattern[3]:
                            count += 1
    return count

def replace_list_diagonal_forward(pattern, list_of_lists):
    new_list_of_lists = list_of_lists.copy()
    for i in range(len(list_of_lists) - 3):
        for j in range(len(list_of_lists[i]) - 3):
            if new_list_of_lists[i][j] == pattern[0]:
                if new_list_of_lists[i+1][j+1] == pattern[1]:
                    if new_list_of_lists[i+2][j+2] == pattern[2]:
                        if new_list_of_lists[i+3][j+3] == pattern[3]:
                            new_list_of_lists[i][j] = "_"
                            new_list_of_lists[i+1][j+1] = "_"
                            new_list_of_lists[i+2][j+2] = "_"
                            new_list_of_lists[i+3][j+3] = "_"
    return new_list_of_lists

def count_list_diagonal_backward(pattern, list_of_lists):
    count = 0
    for i in range(len(list_of_lists) - 3):
        for j in range(len(list_of_lists[i]) + 3):
            if list_of_lists[i][j] == pattern[0]:
                if list_of_lists[i+1][j-1] == pattern[1]:
                    if list_of_lists[i+2][j-2] == pattern[2]:
                        if list_of_lists[i+3][j-3] == pattern[3]:
                            count += 1
    return count

def replace_list_diagonal_backward(pattern, list_of_lists):
    new_list_of_lists = list_of_lists.copy()
    for i in range(len(list_of_lists) - 3):
        for j in range(len(list_of_lists[i]) - 3):
            if new_list_of_lists[i][j] == pattern[0]:
                if new_list_of_lists[i+1][j-1] == pattern[1]:
                    if new_list_of_lists[i+2][j-2] == pattern[2]:
                        if new_list_of_lists[i+3][j-4] == pattern[3]:
                            new_list_of_lists[i][j] = "_"
                            new_list_of_lists[i+1][j-1] = "_"
                            new_list_of_lists[i+2][j-2] = "_"
                            new_list_of_lists[i+3][j-4] = "_"
    return new_list_of_lists

def count_list_spaced(pattern, list_of_lists):
    count = 0
    word = []
    for i in range(len(list_of_lists)):
        for letter in list_of_lists[i]:
            if len(word) == 0 and letter == pattern[0]:
                word.append(letter)
            elif len(word) == 1 and letter == pattern[1]:
                word.append(letter)
            elif len(word) == 2 and letter == pattern[2]:
                word.append(letter)
            elif len(word) == 3 and letter == pattern[3]:
                word.append(letter)
            elif len(word) == 4:
                count += 1
                word = []
    return count




def part_one():
    list_of_lists = []
    total_count = 0
    with open("day_4.txt", "r") as f:
        line = f.readline().strip()
        while line:
            total_count += count_string_pattern_horizontal("XMAS", line)
            line = replace_string_pattern_horizontal("XMAS", line)
            total_count += count_string_pattern_horizontal("SAMX", line)
            line = replace_string_pattern_horizontal("SAMX", line)
            list_of_lists.append(list(line))
            line = f.readline().strip()
    total_count += count_list_vertical("XMAS", list_of_lists)
    list_of_lists = replace_vertical_list_pattern("XMAS", list_of_lists)
    total_count += count_list_vertical("SAMX", list_of_lists)
    list_of_lists = replace_vertical_list_pattern("SAMX", list_of_lists)
    total_count += count_list_diagonal_forward("XMAS", list_of_lists)
    list_of_lists = replace_list_diagonal_forward("XMAS", list_of_lists)
    total_count += count_list_diagonal_forward("SAMX", list_of_lists)
    list_of_lists = replace_list_diagonal_forward("SAMX", list_of_lists)
    total_count += count_list_spaced("XMAS", list_of_lists)
    total_count += count_list_spaced("SAMX", list_of_lists)

    print(total_count)


part_one()