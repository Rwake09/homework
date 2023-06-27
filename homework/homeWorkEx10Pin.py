# import getpass
#
# import getpass
#
# correct_pin = '3457'
# max_attempts = 3
# attemps = 0
# while attemps < max_attempts:
#     supplied_pin = getpass.getpass('Enter your pin:')
#
#     if supplied_pin == correct_pin:
#         print('pin correct')
#         break
#     else:
#         attemps += 1
#         print('pin incorrect')
# if attemps == max_attempts:
#     print("Max attempts reached, card chewed and destroyed")

# import getpass
import pwinput

correct_pin = '3457'
max_attempts = 3
attemps = 0
while attemps < max_attempts:
    supplied_pin = pwinput.pwinput(prompt="pin ")
    if supplied_pin == correct_pin:
        print('pin correct')
        break
    else:
        attemps += 1
        print('pin incorrect', attemps, 'times')
if attemps == max_attempts:
    print("Max attempts reached, card chewed")
