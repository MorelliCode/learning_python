# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []
result2 = set()

for element in a:
    if element in b and element not in result:
        result.append(element)

print(result)

def overlap_set(numbers1, numbers2):
    a_set = set(numbers1)
    b_set = set(numbers2)
    for item in a_set:
        if item in b_set:
            result2.add(item)
    return result2

print(overlap_set(a, b))