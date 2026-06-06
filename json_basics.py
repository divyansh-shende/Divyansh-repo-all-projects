import json

# Create a dictionary
data = {
    "name": "Divyansh",
    "age": 17,
    "skills": ["Python", "Git", "VS Code"],
    "address": {
        "city": "Mumbai",
        "country": "India"
    }
}

# Convert dictionary to JSON string
json_string = json.dumps(data, indent=2)

print("JSON String:")
print(json_string)

# Save JSON to a file
with open("me.json", "w") as file:
    json.dump(data, file, indent=2)

print("\nData saved to me.json")

# Read JSON from file
with open("me.json", "r") as file:
    loaded_data = json.load(file)

# Print specific values
print("\nName:", loaded_data["name"])
print("City:", loaded_data["address"]["city"])