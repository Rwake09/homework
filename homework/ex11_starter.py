#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print('')
print('')
# define a function to call upon in the print function later, pass in string to the argument so it returns a string
def replace_length_with_dash(string):
    # define a variable for the length of characters in the variable for Belgium
    length = len(Belgium)
    #  define a variable for the dashes to replace total characters
    replaced_string = '-' * length
    return replaced_string
# orginal variable

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# variable for the result with our defined function as the callable with the original Belgium varible passed as the argument to replace
result = replace_length_with_dash(Belgium)
print(result)

print('')
print('')
# create a
Belgium_split = Belgium.split(',')
Belgium_replace_commas = Belgium.replace(',', ':')
Belgium_pop = Belgium_split[1]
Brussels_pop = Belgium_split[3]
Total_pop = int(Belgium_pop) + int(Brussels_pop)

print('')
print('')


print(Belgium_replace_commas)

print('')
print('')

print(Total_pop)
