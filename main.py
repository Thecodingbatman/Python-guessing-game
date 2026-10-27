import random
random_number = random.randint(1, 20)
print("This is a guessing game")
while True:
    initial_User_Input = input("What do you want to do?\n quit or play.\n")
    if initial_User_Input == "quit":
        break
    while initial_User_Input != "quit":
        user_guess = int(input("Please enter a number between 1 and 20:\n"))
        if user_guess == random_number:
            print("Correct")
            break 
        else:
            print("Wrong please try again")