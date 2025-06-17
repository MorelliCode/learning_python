list = [7,5,3,1,9,8,6,4,2]

def bubble_sort(list):
    while True:
        was_switched = False
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                switch = list[i]
                list[i] = list[i+1]
                list[i+1] = switch
                was_switched = True
        if was_switched == False:
            break

print(list)
bubble_sort(list)
print(list)