#Program created using the People-in-Space API
#more information at http://open-notify.org/Open-Notify-API/People-In-Space/

import requests

def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()["people"]
        print(f"At the moment, there are {len(data)} people in space.")
        print("They are:")
        
        data = sorted(data, key=lambda x:x["name"])

        for person in data:
            print(f"- {person["name"]}, from the craft {person["craft"]}")

get_astronauts()