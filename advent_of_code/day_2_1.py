# The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# This example data contains six reports each containing five levels.

# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.

# In the example above, the reports can be found safe or unsafe by checking those rules:

#     7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
#     1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
#     9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
#     1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
#     8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
#     1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

# So, in this example, 2 reports are safe.

# Analyze the unusual data from the engineers. How many reports are safe?

is_valid = False
des_asc = []
number_safe = 0

with open("day_2.txt", "r") as f:
    line = f.readline().strip().split()
    while line:
        for i in range(len(line)):
            line[i] = int(line[i])
        is_valid = False
        des_asc = []
        for i in range(len(line)):
            if i == len(line) - 1:
                break
            if abs(line[i] - line[i+1]) > 3:
                is_valid = False
                break
            else:
                is_valid = True
                if line[i] > line[i+1]:
                    des_asc.append(-1)
                elif line[i] < line[i+1]:
                    des_asc.append(1)
                else:
                    is_valid = False
                    break

        if is_valid == True:
            if -1 in des_asc and 1 in des_asc:
                line = f.readline().strip().split()
                continue
            else:
                number_safe +=1
        line = f.readline().strip().split()

print(number_safe)