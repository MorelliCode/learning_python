
is_valid = False
des_asc = []
number_safe = 0

with open("day_2.txt", "r") as f:
    line = f.readline().strip().split()
    while line:
        for i in range(len(line)):
            line[i] = int(line[i])
        is_valid = False
        des_asc = []
        for i in range(len(line)):
            if i == len(line) - 1:
                break
            if abs(line[i] - line[i+1]) > 3:
                is_valid = False
                break
            else:
                is_valid = True
                if line[i] > line[i+1]:
                    des_asc.append(-1)
                elif line[i] < line[i+1]:
                    des_asc.append(1)
                else:
                    is_valid = False
                    break

        if is_valid == True:
            if -1 in des_asc and 1 in des_asc:
                line = f.readline().strip().split()
                continue
            else:
                number_safe +=1
        line = f.readline().strip().split()

print(number_safe)