# finds the folder containing python

#!/usr/bin/python
# Example Python script


# importing system module
import sys
# creating a variable which is the length of sys.argv
# argv is part of the sys module
# argument vector aka the list of parameters/inputs to the program
# argument = parameter/input

# argument_count is our variable
argument_count = len(sys.argv)
# if the variable is greater than 1 print x
# 'if' is a conditional expression
if argument_count > 1:
    print('Too many args')
#     else print the concatenation of  "Hello" + the 'where variable'
else:
    where = 'World'
    print("Hello", where)
# always prints as it is to the left
print('Goodby from ' + sys.argv[0])

print(sys.argv[0])

