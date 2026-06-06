import requests
import json
import os

# API URL
url = "https://official-joke-api.appspot.com/random_joke"

# Get joke from API
response = requests.get(url)

# Convert response to Python dictionary
data = response.json()

# Print setup
print("\n😂 Joke Time!")
print(data["setup"])

# Wait for user
input("\nPress Enter for the punchline...")

# Print punchline
print(data["punchline"])

# Save joke to jokes.json
filename = "jokes.json"

# Read existing jokes
if os.path.exists(filename):
    with open(filename, "r") as file:
        jokes = json.load(file)
else:
    jokes = []

# Add new joke
jokes.append(data)

# Write back to file
with open(filename, "w") as file:
    json.dump(jokes, file, indent=4)

print("\nJoke saved to jokes.json")