# The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

# It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# For example, consider the following section of corrupted memory:

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

#we need regular expressions for this one
import re


def find_patterns(string_to_process):
    #Use regular expressions to extract a list of all "mul(X,Y)" values (where X and Y are 1 to 3 digits numbers)
    processed_list = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', string_to_process)
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
        patterns = find_patterns(text)
        for item in patterns:
            added_multiplications += execute_multiplication(item)
        print(added_multiplications)


part_one()