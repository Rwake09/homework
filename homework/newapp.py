# create a variable for the answer
answer = 9
# creat a loop so that if the answer is not True the app is re-run
while True:
# create a variable that takes the users input
    guess = input('guess a number between 1 an 10: ')
# make guess an integer
    guess = int(guess)
# conditional for a True answer
    if guess == answer:
        # print statement for true answer
        print('you win!')
        break
    # conditional for a numer higher than 10
    elif guess > 10 or guess < 1:
        print('Guess should be between 1 and 10.')
    # conditional statement for an incorrect answer
    else:
        print('guess again!')

# create a variable for the answer
answer2 = 3.14
# creat a loop so that if the answer is not True the app is re-run
while True:
    # create a variable that takes the users input
    guess2 = input('What is pi to 2 decimal places? ')
    # guess2 is a float(decimal number)
    guess2 = float(guess2)
    # used round to round pi to 3.14
    if round(guess2, 2) == answer2:
        print('Well done!!')
        break
    else:
        print('Try again!')

print('Hope you had fun!!')
