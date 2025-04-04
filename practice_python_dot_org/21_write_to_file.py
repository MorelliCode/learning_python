# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:

#     Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup 

url = "http://www.nytimes.com"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
wrapper_headline = soup.find_all(class_="story-wrapper")

print("You're about to save all headlines of the NY times in to a file")
file_name = input("What should the file be called? ") + ".txt"

with open((file_name), "w") as open_file:
    for section in wrapper_headline:
        for p in section.find_all("p", class_="indicate-hover"):
            open_file.write(p.get_text() + "\n")



