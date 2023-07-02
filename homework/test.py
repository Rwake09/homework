PIN = '2023'
max_attempts = 3
Count = 0

# prompt to enter the PIN
# correct PIN statement 'access granted' appears
while Count < max_attempts:
    enter_pin = input('enter your PIN')
    if enter_pin == PIN:
        print('correct PIN')
        print('access granted')
        break
    # if incorrect_PIN 'Wrong pin entered' appears
    # Prompts to try again up the max number of attempts allowed
    # print('incorrect PIN please try again')
    else:
        Count += 1
        print("Wrong pin entered", Count, "times")


if Count == max_attempts:
    print("Wrong pin entered 3 times, account locked")


def multiply(a, b):
    return a * b

a = 2
b = 1
print(multiply(a, b))