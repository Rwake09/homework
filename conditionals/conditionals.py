a = 2
b = 2


# if statements

# logical operators not equal !=
if a == b:
    print('a is equal to b')

lang = ['Perl', 'python', 'PHP', 'Ruby']
if 'python' in lang:
    print('Python is found')

if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('some other unexpected condition')

#     chained conditionals
number = 5
distance = 42
if 0 < number < 42 < distance:
    print('num and dist are within range')
else:
    print('num and dist are out of range')
#  logical AND operator
if 0 < number and number < 42 and 42 < distance:
    print('num and dist are within range')

else:
    print('What?')

# if list is empty print nothing, if not empty print not empty
myList = [1, 2, 3, 5, 7, 9]
if myList:
    print('this list is not empty')
#  if all items in the list are not true print the statement
myList2 = [True, False]
if not all(myList2):
    print('not all are true')

# Object types

num = 42
txt = '3'
# convert a string to an integer
if int(txt) < num:
    print('txt is less than num')

# while line is not equal to 'done' print type "done" to complete

# line = None
# while line != 'done':
#     line = input('Type "done" to complete:')
#     print('<', line, '>')

# if no i+=1 this would return an endless loop
i = 1
while i < 6:
    if i == 4:
        print('the value of i is 4')
    i += 1

# using a break to stop the script

i = 1
while i < 8:
    print(i)
    if i == 4:
        break
    i += 1
print()
print()
# while with continue

i = 1
while i < 8:
    i += 1
    if i == 4:
        continue
    print(i)

# while with else

i = 1
while i < 8:
    i += 1
    print(i)
else:
    print('i is no longer less than 8')

# For loops

fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)

#     for loop with break
fruits = ['apple', 'banana', 'orange', 'grape']
for x in fruits:
    print(x)
    if x == 'orange':
        break

# pause

favouriteFoods = ['pizza', 'chinese', 'lasagna', 'madras', 'steak']
for x in favouriteFoods:
    print(x)