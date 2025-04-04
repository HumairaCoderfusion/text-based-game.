import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    
    # Define choices
    choices = ["rock", "paper", "scissors"]
    
    while True:
        # Get player's choice
        player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if player_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

# Start the game
rock_paper_scissors()
