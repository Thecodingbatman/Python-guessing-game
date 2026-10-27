import random
random_number = random.randint(1, 20)
print("This is a guessing game")
initial_User_Input = input("What do you want to do?\n quit or play.\n")
print(random_number)
while (initial_User_Input == "play" ):
    user_guess = int(input("Please enter a number between 1 and 20:\n"))
    if user_guess == random_number:
        print("Correct")
        break
    else:
        print("Wrong please try again")