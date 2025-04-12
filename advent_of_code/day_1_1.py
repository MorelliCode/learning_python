# There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

# For example:

# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

# In the example list above, the pairs and distances would be as follows:

#     The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
#     The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
#     The third-smallest number in both lists is 3, so the distance between them is 0.
#     The next numbers to pair up are 3 and 4, a distance of 1.
#     The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
#     Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.

# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

# Your actual left and right lists contain many location IDs. What is the total distance between your lists?

left_list = []
right_list = []
total_sum = 0

with open("day_1_1.txt", "r") as f:
    line = f.readline().strip().split()
    while line:
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))
        line = f.readline().strip().split()

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    if left_list[i] - right_list[i] > 0:
        total_sum += left_list[i] - right_list[i]
    else:
        total_sum += right_list[i] - left_list[i]

print(total_sum)