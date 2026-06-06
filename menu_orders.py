menu = {
    "burger": 250,
    "pizza": 400,
    "pasta": 300,
    "coke": 80,
    "hell": 100,
}

# Display Menu
print("\n===== MENU =====")
for item, price in menu.items():
    print(f"{item.capitalize()} - ₹{price}")
print("================\n")

orders = []
total_bill = 0

while True:
    item = input("What would you like to order? (or 'done'): ").lower()

    if item == "done":
        break

    if item in menu:
        orders.append(item)
        total_bill += menu[item]
        print(item, "added to your order.")
    else:
        print("Not available")

print("\n===== YOUR ORDER =====")
for item in orders:
    print(f"{item.capitalize()} - ₹{menu[item]}")

print("----------------------")
print("Total Bill = ₹", total_bill)