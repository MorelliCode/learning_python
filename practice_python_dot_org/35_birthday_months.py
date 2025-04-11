#  This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

import json
from collections import Counter

json_file = "34.json"
bdate_dictionary = {}
date_list = []
months_list = []
result_dictionary = {}


def read_from_file(file):
    with open(file, "r") as f:
        return json.load(f)
    
def count_months(months):
    c = Counter(months_list)
    return c


bdate_dictionary = read_from_file(json_file)

for date in bdate_dictionary.values():
    split_list = date.split("/")
    if split_list[1] == "01":
        months_list.append("January")
    elif split_list[1] == "02":
        months_list.append("February")
    elif split_list[1] == "03":
        months_list.append("March")
    elif split_list[1] == "04":
        months_list.append("April")
    elif split_list[1] == "05":
        months_list.append("May")
    elif split_list[1] == "06":
        months_list.append("June")
    elif split_list[1] == "07":
        months_list.append("July")
    elif split_list[1] == "08":
        months_list.append("August")
    elif split_list[1] == "09":
        months_list.append("September")
    elif split_list[1] == "10":
        months_list.append("October")
    elif split_list[1] == "11":
        months_list.append("November")
    else:
        months_list.append("December")

#print(months_list)

result_dictionary = dict(count_months(months_list))

print(result_dictionary)






