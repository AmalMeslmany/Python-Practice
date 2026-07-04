import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Choose rock, paper or scissors: ").lower()

if user not in choices:
    print("Invalid choice! Please choose rock, paper or scissors.")

else:

    if user == computer:
        print("Draw")

    elif user == "rock" and computer == "scissors":
        print("You Win!")

    elif user == "paper" and computer == "rock":
        print("You Win!")

    elif user == "scissors" and computer == "paper":
        print("You Win!")

    else:
        print("Computer Wins!")

    print("Computer chose:", computer)