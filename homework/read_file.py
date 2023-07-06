
# safe recomended way to open files, while also return the file as a list

with open('pelican.txt', 'r') as infile:
    # lines = infile.readlines()
    line2 = infile.read()
    print(type(line2))
    # print(lines)


print()
print()
# print(type(lines))

print()
print()

with open('pelican.txt', 'r') as f:
    my_list = [word for line in f for word in line.strip().split()]
    for item in my_list:
        print(item)
    print(f'Total number of items: {len(my_list)}')


# for item in lines:
#     print(item.strip())
#     print(len(item.strip()))