# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele

# Then I would see the string:

#   Michele is name My

# shown back to me.

def get_string():
    return input("Give me a sentence to reverse:\n")

def separate_string(text):
    new_text = text.split()
    return new_text

def invert_list(list):
    new_list = []
    for item in list:
        new_list.insert(0, item)
    return new_list

def create_new_string(new_list):
    new_string = " ".join(new_list)
    return new_string

print(create_new_string(invert_list(separate_string(get_string()))))