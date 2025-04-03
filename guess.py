import random

def number_guessing_game(): print("Welcome to the Number Guessing Game!") lower_bound = 1 upper_bound = 100 secret_number = random.randint(lower_bound, upper_bound) attempts = 0

while True:
    try:
        guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")
        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < lower_bound or guess > upper_bound:
            print("Out of bounds! Try again.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except Exception as e:
        print(f"An error occurred: {e}")

if name == "main": number_guessing_game()

