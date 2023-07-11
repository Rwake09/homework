# rock, paper, scissors game
import random

def rps():
    print("Welcome to the game")
    print("Enter r for rock, p for paper and s for scissors")
    print("Enter q to quit")
    while True:
        user_input = input("Enter your choice: ")
        if user_input == "q":
            break
        comp_input = random.choice(["r", "p", "s"])
        if user_input == comp_input:
            print("Tie")
        elif user_input == "r" and comp_input == "s":
            print("You win")
        elif user_input == "p" and comp_input == "r":
            print("You win")
        elif user_input == "s" and comp_input == "p":
            print("You win")
        else:
            print("You lose")

