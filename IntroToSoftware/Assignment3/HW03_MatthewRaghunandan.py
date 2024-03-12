# Rock paper scissors - Assignment 3 

from random import choice

# use a dictionary to find who wins
moves = {
    ("r", "r"): -1,
    ("r", "p"): 1,
    ("r", "s"): 0,
    ("p", "r"): 0,
    ("p", "p"): -1,
    ("p", "s"): 1,
    ("s", "r"): 1,
    ("s", "p"): 0,
    ("s", "s"): -1
} # basically we will index the dictionary in the following format (user_choice, computer_choice) and it will return -1 if it's a tie, 0 if the user wins, and 1 if the computer wins

# function to play the game
def play_game(): # recursive function. Will keep calling itself until the user decides to quit
    user_choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit: ")
    if user_choice == 'q':
        print("Goodbye!")
        return
    elif user_choice != 'r' and user_choice != 'p' and user_choice != 's':
        print("Invalid choice. Please try again.")
        play_game()
    else:
        computer_choice = choice(["r", "p", "s"])
        print(f"Computer chose {computer_choice == 'r' and 'rock' or computer_choice == 'p' and 'paper' or 'scissors'}")
        result = moves[(user_choice, computer_choice)]
        if result == -1:
            print("It's a tie!")
        elif result == 0:
            print("You win!")
        else:
            print("Computer wins!")
        play_game()

play_game()


