# collection with an item/vaslue
someString = 'Norweigen Blue', "Mr. Khans bike"
# collection - list with items
fruitList = ['banana', 'apples', 'guava', 'oranges']

numberList = [3,5,7,9,1]


# arithmetic operations on lists
print('min',min(numberList))
print('max',max(numberList))
print('sum',sum(numberList))

print()
print()

# access individual items using their indexs
print(numberList[0])
print(numberList[2])

print()
print()

# length of list
print('length of the list is ',len(numberList))

print()
print()

# return a range of items from a list-start index inclusive[1:2] end index exclusive
print(numberList[1:3])

print()
print()

# get items from begining of list to a position
print(numberList[:3])
print(numberList[3:])

print()
print()

# change items
numberList[0] = 90
numberList[3] = [50,50]
print(numberList)

print()
print()

# add items to a list

fruitList += ['mangoes', 'pineapple']
print(fruitList)

print()
print()

#  remove items from a list

# fruitList.remove('mangoes')
print(fruitList)

print()
print()


# iterate or loop over a list
for fruit in fruitList:
    print(fruit)


count = fruitList.count('mangoes')
print('mangoes occur ',count, 'of time(s)')

print()
print()

# find the index of an item
fruitList.index('pineapple')

# find the index of a non-existing item
# fruitList.index('cars')

print()
print()

# sort list items

fruitList.sort()
print(fruitList)
fruitList.sort(reverse=True)
print(fruitList)

print()
print()

# dictionaries
mydict = {'Australia':'canberra', 'Eire':'Dublin', 'France':'Paris'}
print(mydict['Australia'])

country = 'Iceland'
mydict[country] = 'Reykjavik'
print(mydict)

print()
print()

# dictionary sorting an object of type list
mydict2 = {'UK':['London', 'Wigan', 'Manchester'], 'US':['Miami', 'New York', 'Boston']}
print(mydict2['UK'][2])

print()
print()

mydict2['FR']=['Paris', 'Lyon', 'Bordeaux']
print(mydict2['FR'][2])

for item in mydict2:
    print(len(mydict2[item]))


print()
print()
# creat a list of favourite fruits
myFavFruits = ['mango', 'banana', 'pear', 'watermelon']
# sort the list using key and len
myFavFruits.sort(key=len)
# print the myfavfruits variable at index 3 or -1
print(myFavFruits[3])
# print the length of myFavFruits at index 3 or -1
print(len(myFavFruits[3]))


print()
print()












