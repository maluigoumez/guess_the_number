import random

# Generate the secret number
secret_number = random.randint(1, 100)

# Player's turn
player_guess = None
while player_guess != secret_number:
    try:
        player_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue  # Move to the next iteration of the loop

    if player_guess < secret_number:
        print("Too low! Try again.")
    elif player_guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break  # Exit the loop if the player guesses correctly

# Computer's turn (random guess for now)
computer_guess = random.randint(1, 100)

# Check if the computer guessed correctly
if computer_guess == secret_number:
    print("The computer guessed the number!")
else:
    # You can add more logic here for additional computer turns or further game play
    print("The computer didn't guess the number.")

# Add unit tests (optional, for code quality assurance)
# import unittest
# ... (unit test code here)
