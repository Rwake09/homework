# create a new .txt file in write format
infile = open('pelican.txt', 'w')
infile.close
# open the file in write format to add lines to it
write_lines = open('pelican.txt', 'w')
# write lines using .writelines
write_lines.writelines('A wonderful bird is the pelican. ')
# add more to the previous line
write_lines.writelines('His bill holds more than his belican. ')
# new list
lines = ['He can take his beak, \n', 'Enough food for a week, \n', "But I'm damned if I can see how the helican.\n"]
# append that lis to the previous lines, use \n to move to a new line
write_lines.writelines(lines)
