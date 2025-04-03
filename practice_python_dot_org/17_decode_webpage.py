# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup 

url = "http://www.nytimes.com"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
wrapper_headline = soup.find_all(class_="story-wrapper")

for section in wrapper_headline:
    for p in section.find_all("p", class_="indicate-hover"):
        print(p.get_text())

