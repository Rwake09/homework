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