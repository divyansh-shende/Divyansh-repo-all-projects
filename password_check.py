password = "sarthak"

attempts = 0

while attempts < 3:
    guess = input("Enter password: ")

    if guess == password:
        print("Correct")
        break
    else:
        attempts = attempts + 1
        print("Wrong password")

if attempts == 3:
    print("Locked out")