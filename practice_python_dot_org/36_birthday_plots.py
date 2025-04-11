#  This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

from bokeh.plotting import figure, show, output_file
from collections import Counter
import json

output_file("plot.html")
bdate_dictionary = {}
month_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
json_file = "34.json"
month_count_dictionary = {}


def read_from_file(file):
    with open(file, "r") as f:
        return json.load(f)
    
def decode_months(date_dictionary):
    months_list = []
    for date in date_dictionary.values():
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
    return months_list

def count_months(months_list):
    c = Counter(months_list)
    return dict(c)


bdate_dictionary = read_from_file(json_file)

month_count_dictionary = count_months(decode_months(bdate_dictionary))

p = figure(x_range = month_name)
x = list(month_count_dictionary.keys())
y = list(month_count_dictionary.values())

p.vbar( x=x, top=y, width=.75)
show(p)