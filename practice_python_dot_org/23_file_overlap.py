# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

with open("23_1.txt", "r") as file_prime, open("23_2.txt", "r") as file_happy:
    line_prime = file_prime.readline()
    line_happy = file_happy.readline()
    list_prime = []
    list_happy = []
    while line_prime:
        new_line_prime = int(line_prime.rstrip("\n"))
        list_prime.append(new_line_prime)
        line_prime = file_prime.readline()
    while line_happy:
        new_line_happy = int(line_happy.rstrip("\n"))
        list_happy.append(new_line_happy)
        line_happy = file_happy.readline()

    list_overlap = [item for item in list_prime if item in list_happy]
    
    print(list_overlap)
        