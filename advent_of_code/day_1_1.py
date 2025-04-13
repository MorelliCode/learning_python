
left_list = []
right_list = []
total_sum = 0

with open("day_1.txt", "r") as f:
    line = f.readline().strip().split()
    while line:
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))
        line = f.readline().strip().split()

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    total_sum += abs(left_list[i] - right_list[i])

print(total_sum)