# The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

# More of the above example's reports are now safe:

#     7 6 4 2 1: Safe without removing any level.
#     1 2 7 8 9: Unsafe regardless of which level is removed.
#     9 7 6 2 1: Unsafe regardless of which level is removed.
#     1 3 2 4 5: Safe by removing the second level, 3.
#     8 6 4 4 1: Safe by removing the third level, 4.
#     1 3 6 7 9: Safe without removing any level.

# Thanks to the Problem Dampener, 4 reports are actually safe!

# Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

safe_reports = 0

def string_to_int(list_of_str):
    list_to_change = list_of_str.copy()
    for i in range(len(list_to_change)):
        list_to_change[i] = int(list_to_change[i])
    return list_to_change

def is_report_valid(list_of_int):
    is_ascending = check_ascending(list_of_int)
    is_descending = check_descending(list_of_int)

    if not is_ascending and not is_descending:
        return False
    
    for i in range(len(list_of_int) - 1):
        diff = abs(list_of_int[i] - list_of_int[i+1])
        if diff < 1 or diff > 3:
            return False
    
    return True

def valid_with_dampener(list_of_int):
    if is_report_valid(list_of_int):
        return True
    
    valid_with_dampener = False

    for i in range(len(list_of_int)):
        modified_report = list_of_int.copy()
        del modified_report[i]
        if is_report_valid(modified_report):
            valid_with_dampener = True
            break
    if valid_with_dampener:
        return True
    else:
        return False


def check_ascending(list_of_int):
    for i in range(len(list_of_int) -1):
        if list_of_int[i] > list_of_int[i+1]:
            return False    
    return True

def check_descending(list_of_int):
    for i in range(len(list_of_int) -1):
        if list_of_int[i] < list_of_int[i+1]:
            return False    
    return True




with open("day_2.txt", "r") as f:
    line = f.readline().strip().split()
    while line:
        line = string_to_int(line)
        if is_report_valid(line):
            safe_reports += 1
        elif valid_with_dampener(line):
            safe_reports += 1
        line = f.readline().strip().split()
    print(safe_reports)



