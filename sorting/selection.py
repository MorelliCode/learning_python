list = [7,5,3,1,9,8,6,4,2]

def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        if list[i] != list[min]:
            switch = list[i]
            list[i] = list[min]
            list[min] = switch

print(list)
selection_sort(list)
print(list)