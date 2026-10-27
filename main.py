import random
random_number = random.randint(1, 20)
print("This is a guessing game")
print(random_number)
user_proof = 1
while True:
    try:
            initial_User_Input = str(input("What do you want to do?\n quit or play.\n").strip()).lower()
    except ValueError:
        print("make sure you typed correctly")
        initial_User_Input
    if initial_User_Input == "quit":
        break
    while initial_User_Input == "play":
        try:
            user_guess = int(input("Please enter a number between 1 and 20:\n"))
        except ValueError:
            print("please enter a whole number")
            continue
        if user_guess == random_number:
            print("Correct")
            break
        else:
            print("Wrong please try again")