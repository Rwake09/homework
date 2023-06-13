person1 = 'Melissa'
person2 = 'Rob'
person3 = 'Serene'
person4 = 'Callum'

# tuple , this is immutable

person_tuple = 'Melissa', 'Rob', 'Serene', 'Callum'
print(type(person_tuple))
print(person_tuple)
print(person_tuple[0])
print(person_tuple[1])
print(person_tuple[2])
print(person_tuple[-1])

# this tuple has round brackets
second_tuple = ('Jordan', 'Lou')

print(type(second_tuple))
print(second_tuple)
print(second_tuple[0])

# [] list items these are mutable
lucky_numbers = [5, 8, 13]
print(lucky_numbers)
print(type(lucky_numbers))

marmite_lover = True, True, False
print(type(marmite_lover))

# [] makes a list, items seperated by ,
names_list = ['Stephen', 'Mark', 'Nav', 'Nik', 'Lewis']
print(names_list)
print(type(names_list))

names_list.append('Melissa')
print(names_list)

print(names_list[0])

# dictionaries {}
# key value pairs
numbers_dictionary = {'Mark': 5, 'Lewis': 8, 'Rob': 2}
print(numbers_dictionary)
print(type(numbers_dictionary))

# sets
# a unique collection
# no duplicates

names_set = {'Lewis', 'Nik','Serene', 'Nav', 'Lewis', 'Stephen'}
print(names_set)
print(type(names_set))


