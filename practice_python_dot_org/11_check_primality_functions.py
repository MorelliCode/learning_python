#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def get_number():
    return int(input("Give me a number, I'll check if it's a prime number:"))

def create_list_divisors(number):
    for x in range(2, number):
        if number % x == 0:
            divisors.append(x)

def check_prime():
    if len(divisors) == 0:
        return str(user_input) + " is a prime number."
    else:
        return str(user_input) + " is NOT a prime number. It is divisible by: " + str(divisors) + "."
        

user_input = get_number()
divisors = []

create_list_divisors(user_input)

print(check_prime())