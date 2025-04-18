# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]
a_list = []
a_set = set()


def dedupe_list(numbers):
    for item in numbers:
        if item not in a_list:
            a_list.append(item)
    return a_list

def dedupe_set(numbers):
    a_set = set(numbers)
    return a_set


print(dedupe_list(a))

print(dedupe_set(a))