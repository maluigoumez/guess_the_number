import random

# Generate the random number
random_number = random.randint(1, 100)

# Starting guesses for both user and computer
user_guess = None
computer_guess = None


while user_guess != random_number and computer_guess != random_number:

    #user's turn

    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue  

    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break  # Exit the loop if the user guesses correctly

# Computer's turn (random guess for now)
    computer_guess = random.randint(1, 100)
    print(f"The computer guesses: {computer_guess}")

    if computer_guess < random_number:
        print("Computer's guess is too low.")
    elif computer_guess > random_number:
        print("Computer's guess is too high.")
    else:
        print("The computer guessed the number!")
        break  # Exit the loop if the computer guesses correctly



    
# Add unit tests (optional, for code quality assurance)
# import unittest
# ... (unit test code here)