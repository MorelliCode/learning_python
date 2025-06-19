import requests

def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"ERROR: {response.status_code}")

    print(f"The pokemon name is {data["name"]}")
    get_type(data)

def get_type(pokemon_dict):
    type_1 = pokemon_dict["types"][0]["type"]["name"]
    type_2 = None
    message = "It's a"
    vowels = ["a", "e", "i", "o", "u", ]

    if type_1[0] in vowels:
        message += "n"

    message += f" {type_1}"

    if len(pokemon_dict["types"]) > 1:
        type_2 = pokemon_dict["types"][1]["type"]["name"]
        message += f" and {type_2}"
    
    message += " type pokemon."
    print(message)
    

get_pokemon("mew")