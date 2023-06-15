import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
print(glob.glob(pattern))
print()
print()


# TODO: use os.path.getsize to find each file's size
list = glob.glob(pattern)
for x in list:
    print(x, os.path.getsize(x))
print()
print()



# TODO: Add a test to only display files that are not zero length
list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))
print()
print()



# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(os.path.basename(x), os.path.getsize(x))

import getpass

correct_pin = '3457'
max_attempts = 3
attemps = 0
while attemps < max_attempts:
    supplied_pin = getpass.getpass('Enter your pin:')

    if supplied_pin == correct_pin:
        print('pin correct')
        break
    else:
        attemps += 1
        print('pin incorrect')
if attemps == max_attempts:
    print("Max attempts reached, card chewed and destroyed")

