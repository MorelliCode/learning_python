import csv
import json

data = {}

with open("learning_apis/aviation/airport_raw.csv", "r") as raw_file:
    reader = csv.DictReader(raw_file)
    for row in reader:
        data[row["icao"]] = row["name"]

with open("learning_apis/aviation/airport_icao.json", "w") as json_file:
    json.dump(data, json_file, indent=4)