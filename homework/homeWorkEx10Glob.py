import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# * is to select all files, a letter berfore will selec the files beginning with that charecter, and if at the end of the * will select files ending with that letter
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
print(glob.glob(pattern))
print()
print()


# TODO: use os.path.getsize to find each file's size
list = glob.glob(pattern)
for x in list:
    print(x, os.path.getsize(x))
print()
print()



# TODO: Add a test to only display files that are not zero length
list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(x, os.path.getsize(x))
print()
print()



# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
list = glob.glob(pattern)
for x in list:
    if os.path.getsize(x) > 0:
        print(os.path.basename(x), os.path.getsize(x))