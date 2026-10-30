import random

print("This is a guessing game!")

while True:
    choice = input("What would you like to do? Type 'play' or 'quit': ").strip().lower()

    if choice == "quit":
        print("Goodbye!")
        break

    if choice != "play":
        print("Please type 'play' or 'quit'.")
        continue

    secret_number = random.randint(1, 20)

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 20:
            print("Your guess must be between 1 and 20.")
        elif guess == secret_number:
            print("Correct!")
            break
        else:
            print("Wrong—please try again.")
