# import os
# # open file in read mode
# infile = open('mynewfile.txt','r')
# infile.close()
# # print(infile.read())
#
# print()
# print()
#
# # Readline
# infile2 = open('mynewfile.txt','r')
# line = infile2.readlines()
# infile2.close()
# # print(line)
#
# # reads the whole file
# lines = open('mynewfile.txt').read()
# print(lines)
#
# lines = open('mynewfile.txt').read().splitlines()
# print(lines)
#
# # safe recomended way to open files
# with open('mynewfile.txt', 'r') as infile:
#     for line in infile:
#         print(line, end='')
#
#
# infile = open('mynewfile.txt').read()
# print(infile)
#
# # writing to a file
#
# output = open('mynewfile.txt', 'w')
#
# # add to next line
# output.write('7\n')
# output.close()
#
# # append a file
# output2 = open('mynewfile.txt', 'a')
# output2.write('7\n')
#
# # write a list to a file using a line terminator to move to separate lines
#
# fruits = ['oranges\n', 'mangoes\n']
# output2.writelines(fruits)
#
# # for x in fruits:
# #     output2.write(x)
# #     output2.write('\n')
#
# # varFruit = 'banana'
#
# output2.write('pineapple, banana')
# output2
# os.remove('mynewfile.txt')


infile = open('countries.txt', 'w')

output = open('countries.txt', 'a')
countries = ['France', 'Germany', 'Belgium', 'England', 'Croatia']
for x in countries:
    output.write(x)
    output.write('\n')
output.write(str(countries))
