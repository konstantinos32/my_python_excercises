import sys
import random

if len(sys.argv)<2:
    print("You need to choose between rock, paper and scissors")
    sys.exit()

user_choice = sys.argv[1].lower()

valid_choices=["rock", "paper", "scissors"]

if user_choice not in valid_choices:
    print("Invalid choice. You need to choose between rock, paper and scissors")
    sys.exit()

computer_choice = random.choice(valid_choices)

if user_choice == computer_choice:
    game_result = "tie"
    print(f"You both chose {user_choice}. It's a tie! Try again.")

elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    game_result = "win"
   

else:
    game_result = "lose"


print(f"You chose {user_choice} and the computer chose {computer_choice}. You {game_result}!")
