# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input("Give me a word or phrase and I'll tell you if it's a palindrome: \n")
reverse_word = ""

for character in word:
    reverse_word = character + reverse_word

if word == reverse_word:
    print("Yes! This is a palindrome!")
else:
    print("Nope, sorry. Better luck next time.")