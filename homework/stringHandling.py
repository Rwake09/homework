# Basic string

someString = "Some String"
# multiline string
someString1 = """
First Line
Some multiline string
Third Line
"""


print(someString)
print(someString1)

# string character sequence position
# print character 0 to 4
print(type(someString[0:4]))
print(someString[0])
print(someString[1])

# string length
# returns the length of a string
print(len(someString))

if len(someString) < 10:
    print("string not long enough")
else:
    print("way to go")


# loop over a string, does not need to be a variable you can add a string after the 'in'
for x in (["sky", "today"]):
    if x == 4:
        print(x)
    else:
        print('')

# some string methods

number = 3
string = '3'

# convert a string to int
print(number + int(string))

# String to upper or lower case

print(someString.upper())
print(someString.lower())

# type your full names seperated by commas into a string and print the upper case and lower case instances
# print out the length of your names combined

first_name = 'Robert'
last_name = 'Wakefield'
full_name = first_name + ', ' + last_name
print(full_name.upper())
print(full_name.lower())
print(len(full_name))

# string replace

names = "Robert, Wakefield"
print(names.replace('Robert', 'Rob'))
print(names)

# # search a string
# print(names.find('Wakefield'))
# print('Wakefield' in names)
#
# #  slicing - substring -- startindex - endindex -1
#
# print(names[0:4])
#
# # slice from start to a position
#
# print(names[:6])
#
# # slice from a position to the end
# print(names[8:])
#
# # strip or remove whitespace from a string  strip, rstrip removes from the right, lstrip removes from the left
#
#
# names2 = '  Robert, Wakefield   '
# print(names2)
# print(names2.strip())
#
# # remove white space after a string
#
# print(names2.rstrip())
#
# #  remove whitespace before the string
#
# print(names2.lstrip())
#
# # concatenate strings
#
# first_name = 'Robert'
# last_name = 'Wakefield'
# full_name = first_name + ', ' + last_name
# print(full_name)
# print(full_name + ' test')
#
# age = 20
# message = 'i am ' +str(age) + ' years old'
# print(message)
#
# # format insert {} as a placeholder and use the format function to point to the braces where the variable should go
#
# message1 = 'I am {} years old'
# print(message1.format(age))
#
# message2 = 'I am {} years old, and i like {}'
# print(message2.format(age, 'Python'))
#
# # endswith/startswith
#
# message3 = 'Welcome to Python'
# print(message3.startswith('Welcome'))
# print(message3.endswith('Python'))
#
# message3 = 'Welcome to Python'
# print(message3.startswith('w'))
# print(message3.endswith('e'))
#
# # split a string into a list
#
# message4 = "Welcome to Python's coolness"
# print(message4.split())
#
# message4 = "Welcome to Python's coolness"
# splitList = message4.split()
# for x in splitList:
#     print(x)
# print(message4.split())
# # print(splitList[2])
# #
# # #  iterate over the new list
# #
# # for x in splitList:
# #     print(x)
# #
# # # Escape Characters
# #
# # message5 = " Hello world, it is \"sunny\" today"
# # print(message5)
# #
# # message6 = " Hello world, it is \nsunny today"
# #
# # print(message6)
# #
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# print('')
# # challenge
#
#
# vowels = "aAeEiIoOuU"
# count = 0
# input_string = input("enter string ")
# for char in input_string:
#     if char in vowels:
#         count +=1
#
# print('number of vowels:', + count)
#
# hello_world = input('comment here ')
# print(hello_world[::-1])
#
# string = input('string here ')
# split_string = string.split()
# print(len(string.split(',')))
#
