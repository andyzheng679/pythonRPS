import random


# Lets user pick rock paper or scissors, if not in the option, will print, "Not a valid choice"
user_choice = input("Enter a choice: (rock, paper, scissors): ")        

rps_choices = ["rock", "paper", "scissors"]

if user_choice not in rps_choices:
        print("Not a valid choice")


# randomly picks out of the three
comp_choices = ["rock", "paper", "scissors"]

comp_action = random.choice(comp_choices)

print(comp_action)

# determining winners 
if user_choice == comp_action:
    print(f"Both pick {user_choice}, it is a tie.")
elif user_choice == "rock":
    if comp_action == "scissors":
        print("rock beats scissors, you win.")
    else:
        print("paper beats rock, you lose.")
elif user_choice == "paper":
    if comp_action == "rock":
        print("paper beats rock, you win.")
    else:
        print("scissors beats paper, you lose.")
elif user_choice == "scissors":
    if comp_action == "paper":
        print("scissors beats paper, you win.")
    else:
        print("rock beats scissors, you lose.")
        

        



