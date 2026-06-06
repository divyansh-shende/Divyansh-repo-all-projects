while True:
    print("\n1. Add Note")
    print("2. Search Notes")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note added!")

    elif choice == "2":
        keyword = input("Enter keyword to search: ").lower()

        try:
            with open("notes.txt", "r") as file:
                found = False

                for line in file:
                    if keyword in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("No matching notes found.")

        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")