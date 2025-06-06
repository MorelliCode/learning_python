import requests

def get_currency_to_brl(currency_code):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency_code}.json"
    response = requests.get(url)

    if response.status_code == 200:
        value = round(response.json()[currency_code]["brl"], 2)
        return value
    else:
        return f"Error: {response.status_code}"
    
print("The current exchange rate for the Brazilian Real is:")
print(f"{get_currency_to_brl("eur")} Reais to 1 Euro")
print(f"{get_currency_to_brl("usd")} Reais to 1 Dollar")