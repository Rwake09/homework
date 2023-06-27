# a variable is a place to stored data that can change
# python is a dynamically typed language a.k.a weakly typed
# java is a strongly typed language a.k.a statically typed

# python variable - we just give it a name
first_name = 'Robert'

print(first_name)

print(type(first_name))
print(len(first_name))


last_name = 'Wakefield'
print(last_name)
print(type(last_name))




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# this is not python - this is java

# String firstName = "Robert"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# concatenation

print(first_name)
print(last_name)

full_name = first_name + last_name
print(full_name)

full_name_with_space = first_name + ' ' + last_name
print(full_name_with_space)

chips = 2.50
fish = 4.50
total_cost = chips + fish
print(total_cost)

# operator overloading
# '+' either concatenation with string or addition with numbers
# operands is the data we feed in

dinner = 2.50
dinner = dinner + fish
# dinner = dinner + mushy_peas
# long hand syntax

print('price of dinner is ' + str(dinner))


#  shorthand syntax (augmented assignment) / compound operators

dinner += fish
print('price of dinner is ' + str(dinner))
dinner -= chips
print('price of dinner is ' + str(dinner))
