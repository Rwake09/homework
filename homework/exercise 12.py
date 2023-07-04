
# question 1
print('question 1, cheese')
cheese = ['cheddar', 'stilton', 'cornish yarg']
# use the .append function to add one item to a list
# cheese.append('oke')
# use the extend function to add two items to a list
cheese.extend(['oke', 'camembert'])

print(cheese)

print()
print()

# question 2
print('question 2, tuples')
# this is showing as len = 5 because it is counting the length of the only item
tup = 'hello'
print(len(tup))
# this is showing len = 1 as there is a comma, so it is counting how many items there are
tup = 'hello',
print(len(tup))

print()
print()

print('question 3, lotto_app.py')
# question 3 lotto  app
# using a defined function
import random

def generate_lottery_numbers():
    # Generate 6 unique main numbers
    main_numbers = sorted(random.sample(range(1, 50), 6))

    # Generate a single bonus number
    bonus_number = sorted(random.sample(range(1, 9), 2))


    return main_numbers, bonus_number

# Generate and print lottery numbers
main_nums, bonus_num = generate_lottery_numbers()
print("Main Numbers:", main_nums)
print("Bonus Number:", bonus_num)

print()
print()
# using a oneline style

import random

lotto_number = random.sample(range(1, 50), 6)
bonus_ball = random.sample(range(1, 9), 2)
sorted_lotto_numbers = sorted(lotto_number) + sorted(bonus_ball)
print(sorted_lotto_numbers)