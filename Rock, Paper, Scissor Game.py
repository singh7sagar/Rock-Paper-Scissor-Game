# Rock, Paper, Scissor Game

while True:
    import random

    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    user = None

    while user not in choices:
        user = input("Choose your Weapon from (Rock, Paper, Scissor):  ").lower()

    print("You choose:  " + user.upper())
    print("Computer choose:  " + computer.upper())


    if user == computer:
        print("Tie!!")

    elif user == "rock":
        if computer == "paper":
            print("You lose!!")

        if computer == "scissor":
            print("You win!!")

    elif user == "paper":
        if computer == "rock":
            print("You win!!")
        if computer == "scissor":
            print("You lose!!")

    elif user == "scissor":
     if computer == "rock":
        print("You lose!!")
     if computer == "paper":
         print("You win!!")

    play_again = input("You wanna play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Ok Bye!!")

