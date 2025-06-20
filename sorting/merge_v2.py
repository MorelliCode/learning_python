list = [7,5,3,1,9,8,6,4,2]

def merge_sort(list):
    if len(list) > 1:
        left_list = list[:len(list) // 2]
        right_list = list[len(list) // 2:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = 0 # left_list index
        j = 0 # right_list index
        k = 0 # new list index

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

print(list)
merge_sort(list)
print(list)