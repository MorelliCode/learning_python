print ("10>1", 10 > 1) # TRUE 10 is bigger than 1

#print(1 > "1") # tye error. Trying to compare and int to a str

print("int == str", 1 == "1") # FALSE an int is not a str. Even if it's the same character

print("b>a", "b" > "a") # TRUE "b" is after, therefore bigger, than "a"

print("a>aa", "a" > "aa") # FALSE one letter is less than two letters

print("b>a AND a>aa", "b" > "a" and "a" > "aa") # FALSE one of the comparisons is false, which invalidates the AND operator

print("25>50 OR 1 !=2", 25 > 50 or 1 != 2) # TRUE only one of the comparisons is true, so it fulfills the OR operator

print("NOT 42 == Answer", not 42 == "Answer") # TRUE the NOT operator inverts the logic result
