number = int(input("Give me a number: \n"))
check = int(input("Give me a number to divide the last number by: \n"))

if number % 4 == 0:
    print("This number is divisible by 4 and, therefore, even.")
elif number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")

if number % check == 0:
    print(str(number) + " is divided evenly by ", str(check))
else:
    print(str(number) + " is NOT divided evenly by " + str(check))