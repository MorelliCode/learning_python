
import re


def find_patterns_part_one(string_to_process):
    #Use regular expressions to extract a list of all "mul(X,Y)" values (where X and Y are 1 to 3 digits numbers)
    processed_list = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', string_to_process)
    return processed_list

def find_patterns_part_two(string_to_process):
    #Use regular expressions to extract a list of all "mul(X,Y)" values (where X and Y are 1 to 3 digits numbers)
    processed_list = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)", string_to_process)
    return processed_list

def execute_multiplication(pattern):
    #Uses eval to execute the string given as a function
    result = eval(pattern)
    return result

#function to multiply the numbers
def mul(num1, num2):
    result = num1 * num2
    return result

def part_one():
    with open("day_3.txt", "r") as f:
        added_multiplications = 0
        text = f.readlines()
        text = "".join(text)
        patterns = find_patterns_part_one(text)
        for item in patterns:
            added_multiplications += execute_multiplication(item)
        print(added_multiplications)


def part_two():
    with open("day_3.txt", "r") as f:
        added_multiplications = 0
        text = f.readlines()
        text = "".join(text)
        patterns = find_patterns_part_two(text)
        do_or_not = True
        for item in patterns:
            if item == "do()":
                do_or_not = True
                continue
            elif item == "don't()":
                do_or_not = False
                continue
            if do_or_not == False:
                continue
            else:
                added_multiplications += execute_multiplication(item)
        print(added_multiplications)

part_one()

part_two()