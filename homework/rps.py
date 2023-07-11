# rock, paper, scissors game
# import random
import random
# define the function
def rps():
    # welcome to the game opening messages
    print("Welcome to the game")
    # which characters the user should select
    print("Enter r for rock, p for paper and s for scissors")
    print("Enter q to quit")
    while True:
        # set a user input function
        user_input = input("Enter your choice: ")
        if user_input == "q":
            break
        # give the computer an input of random.choice to select from r, p, s
        comp_input = random.choice(["r", "p", "s"])
        # if/elif/else statements to show which move wins over the other
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
# call the function
rps()