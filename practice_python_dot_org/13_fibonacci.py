#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def get_input():
    return int(input("How many fibonacci numbers do you want?\n"))

def create_fibonacci(number):
    for x in range(0,number):
        if len(a) == 0:
            a.append(1)
            continue
        elif len(a) == 1:
            a.append(1)
            continue
        else:
            a.append((a[x - 2] + a[x - 1]))

user_input = get_input()
a = []

create_fibonacci(user_input)

print(a)