list = [7,5,3,1,9,8,6,4,2]

def insertion_sort(list):
    for i in range(len(list)):
        chosen = list[i]
        j = i - 1
        while j >= 0 and list[j] > chosen:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = chosen

print(list)
insertion_sort(list)
print(list)