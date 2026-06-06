import requests

country = input("Enter country name: ")

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

if response.status_code != 200:
    print("country not found")
else:
    data = response.json()[0]

    official_name = data["name"]["official"]

    capital = data.get("capital", ["N/A"])[0]

    region = data.get("region", "N/A")

    population = data.get("population", "N/A")

    currencies = data.get("currencies", {})
    currency_names = [curr["name"] for curr in currencies.values()]

    print("\nCountry Information")
    print("-------------------")
    print("Official Name:", official_name)
    print("Capital:", capital)
    print("Region:", region)
    print("Population:", population)
    print("Currencies:", ", ".join(currency_names))