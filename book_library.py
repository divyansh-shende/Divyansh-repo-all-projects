import json

data = '''
{
  "library": "City Central",
  "books": [
    {"title": "Atomic Habits", "author": "Clear", "available": true},
    {"title": "Deep Work", "author": "Newport", "available": false},
    {"title": "Sapiens", "author": "Harari", "available": true}
  ]
}
'''

# Convert JSON string to Python dictionary
library_data = json.loads(data)

# Print library name
print("Library Name:", library_data["library"])

# Print available books
print("\nAvailable Books:")
for book in library_data["books"]:
    if book["available"]:
        print(book["title"])

# Print authors as comma-separated string
authors = []

for book in library_data["books"]:
    authors.append(book["author"])

print("\nAuthors:", ", ".join(authors))