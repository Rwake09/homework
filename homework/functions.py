
# def is the key to define a function

def first_function():
    print('mr very first python function')
    print()
# call the function
first_function()

#  adding an argument/ parsing

def second_function(first_name):
    print("my name is " + first_name)

second_function("Robert")
second_function('Paul')

# error as no argument passed in
# second_function()

print()
print()

def third_function(first_name, last_name):
    print('my full name is ' + first_name + ' ' + last_name)

third_function('Robert', 'Wakefield')
# fails as only one out of two arguments passed in
# third_function('Rob')

# collection of arguments
def fourth_function(*params):
    print('the number of arguments is ' +str(len(params))+' the first item in our arugment list is ' +params[0])

fourth_function('test')
fourth_function('test 2', 'test')

def fifth_function(first_name, last_name):
    print('my full name is ' + first_name + ' ' + last_name)

# fifth_function(first_function='rob',last_name='wakefield')

# pass multiple arguments with unspecified param names using **
# def sixth_function(**params):
#     print('The first argument is '+ params+['name'])
#
# sixth_function(name='Rob')
#
# def sixth_function(**params):
#     print("The first argument is"+ params +["name"]+ " And the second is "+ params + ["lastname"])
#
# sixth_function(name='Rob',lastname='Wakefield')


def seventh_function(age=25):
    print('my age is '+str(age))

seventh_function(30)
seventh_function()

# functions accepting a list of objects as an argument
listOfCountries = ['UK', 'France', 'Germany', 'Spain']

def countries_function(countries):
    print('The number of countries is ' + str(len(countries))+ ' and their names are;')
    for x in countries:

        print(x)


countries_function(listOfCountries)

# functions using return keyword

def number(num):
    return num
print(number(5))
someNumber = number(5)
print(someNumber)


# function with empty body. use pass keyword to avoid compiler error
def someFunction():
    pass

# peython recursion - a function that calls itself
# factorial of a number-

def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num-1))
number = 6
print('the factorial of ' + str(number)+' is '+str(factorial(6)))




def area(length, width):
    area = length * width
    return area

print(area(10 ,7))

def odd_even(num):
    if num % 2 != 0:
        return 'odd'
    else:
        return 'even'

print(odd_even(3))

def count(word):
    count_word = 0
    for x in word:
        if x in word:
            count_word += 1
            return count_word
string = "Hello World Hello "
count = string.count("Hello")
print(count)

import re
def count_words(string):
    # searches for all the words in a sentance and strips any special characters
    words = re.findall(r'\w+', string)
    # creates a dictionary with key pairs to show the word in the sentance with the freq next to it
    countup={i:words.count(i) for i in words}

    for x, l in countup.items():
        print(x, ' is in the sentance ', l, ' times.')


count_words('the quick brown, fox jumps over the fence!')


print()
print()



def count_words(string):
    words = re.findall(r'\w+', string)
    countup = {}
    for word in words:
        if word in countup:
            countup[word] += 1
        else:
            countup[word] = 1

    for word, count in countup.items():
        print(f"{word} is in the sentence {count} times.")

count_words('the quick brown, fox jumps over the fence!')

# variable visibility in functions

result = 3
def scope_test1():
    result = 42
scope_test1()
print(result)

def scope_test2():
    global result
    result = 42

scope_test2()
print(result)


