import random

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess > secret_number:
        print("too high")

    elif guess < secret_number:
        print("too low")

    else:
        print("correct")
        print("Total attempts:", attempts)
        break