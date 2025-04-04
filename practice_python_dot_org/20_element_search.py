# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

#     Use binary search.

a = [1, 3, 5, 30, 42, 43, 500]

def check_list(number_to_find):
    if number_to_find in a:
        return True 
    else:
        return False

def binary_search(number_to_find):
    start_index = 0
    end_index = len(a) - 1
    while True:
        middle_index = (start_index + end_index) // 2
        middle_value = a[middle_index]

        if start_index > end_index or end_index < start_index:
            return False

        if middle_value == number_to_find:
            return True
        elif middle_value < number_to_find:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1 
            




print(a)
print(check_list(int(input("Give me a number to check if it's on the list: "))))
print(binary_search(int(input("(Binary) Give me a number to check if it's on the list: "))))