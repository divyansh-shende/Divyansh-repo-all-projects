while True:
    print("\n1. Add Expense")
    print("2. View Total Expenses")
    print("3. View Expenses By Category")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = input("Enter amount: ")

        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{amount}\n")

        print("Expense added!")

    elif choice == "2":
        total = 0

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    date, category, amount = line.strip().split(",")
                    total += float(amount)

            print("Total Expenses =", total)

        except FileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == "3":
        search_category = input("Which category? ")

        try:
            with open("expenses.txt", "r") as file:
                found = False

                for line in file:
                    date, category, amount = line.strip().split(",")

                    if category.lower() == search_category.lower():
                        print(date, category, amount)
                        found = True

                if not found:
                    print("No expenses found in that category.")

        except FileNotFoundError:
            print("No expenses recorded yet.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")