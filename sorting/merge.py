list = [7,5,3,1,9,8,6,4,2]

def merge_sort(list, left, right):
    if left < right:
        middle = int((left + right) / 2)
        merge_sort(list, left, middle)
        merge_sort(list, middle + 1, right)
        merge(list, left, middle, right)

def merge(list, left, middle, right):
    v = [None] * (right - left + 1)
    i = left
    j = middle + 1
    k = 0

    while i <= middle and j <= right:
        if list[i] < list[j]:
            v[k] = list[i]
            i = i + 1
        else:
            v[k] = list[j]
            j = j + 1
        
        k = k + 1

    while i <= middle:
        v[k] = list[i]
        i = i + 1
        k = k + 1
    
    while j <= right:
        v[k] = list[j]
        j = j + 1
        k = k + 1

    for i in range(k):
        list[left + i] = v[i]

print(list)
merge_sort(list, 0, len(list) - 1)
print(list)