
left_list = []
right_list = []
total_similarity_score = 0

with open("day_1_1.txt", "r") as f:
    line = f.readline().strip().split()
    while line:
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))
        line = f.readline().strip().split()

for i in range(len(left_list)):
    x = right_list.count(left_list[i])
    total_similarity_score += left_list[i] * x

print(total_similarity_score)