# text-based-game.
A Python text-based game.
import time

def start_game():
    print("\nWelcome to the Treasure Hunt Game!")
    time.sleep(1)
    print("You are in a dark forest looking for treasure.")
    time.sleep(1)

    choice1 = input("\nYou see two paths: Left (L) or Right (R). Which way do you go? ").strip().lower()

    if choice1 == "l":
        print("\nYou walk into a trap! Game Over.")
    elif choice1 == "r":
        print("\nYou find a river.")
        choice2 = input("Do you swim across (S) or walk around (W)? ").strip().lower()

        if choice2 == "s":
            print("\nThe river is too deep, and you drown! Game Over.")
        elif choice2 == "w":
            print("\nYou find a hidden cave with treasure! You Win!")
        else:
            print("\nInvalid choice. Game Over.")
    else:
        print("\nInvalid choice. Game Over.")

if __name__ == "__main__":
    start_game()