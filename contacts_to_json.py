import json
import os

# Load contacts from file if it exists
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
else:
    contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        # Save updated contacts list
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=2)

        print("Contact saved!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")