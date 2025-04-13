
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



