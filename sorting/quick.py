list = [7,5,3,1,9,8,6,4,2]

def quick_sort(list, low, high):
    if low < high:
        pivot_index = split(list, low, high)
        quick_sort(list, low, pivot_index - 1)
        quick_sort(list, pivot_index + 1, high)

def split(list, low, high):
    pivot = list[high]
    i = low

    for j in range(low, high):
        if list[j] <= pivot:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i = i + 1
    
    temp = list[i]
    list[i] = pivot
    
    list[high] = temp
    
    return i 

print(list)
quick_sort(list, 0, len(list) - 1)
print(list)