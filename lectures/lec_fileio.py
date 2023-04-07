'''4.6 reading and writing files'''
# The following will open the qan_stk_prc.csv for reading as text (str objects).
# fobj = open('qan_stk_prc.csv', mode='rt')
# Interpret the parameter mode='rt' as an instruction as to how we will communicate with the file.
# The value rt is a combination of two instructions:
#
# r means "open this file for reading".
# This means you will not be able to modify the contents of qan_stk_prc.csv.
#
# t means "open this file in text mode".
# When you open a file in text mode, the contents will be automatically converted from bytes to text (str)
# access mode parameter: 'a': Opening a file for writing, appending content to the end of the file if it exists.
# access mode parameter: 'w': Opening a file for writing, erasing any previous content if any.
# data mode parameter: 'b': Work with binary data.
'''IN-CLASS Exercise 1'''
'''open a file for reading as strings? rt
open a file for writing as bytes? wb
open a file for appending as strings? at or a, t is a default one'''


# 1.1 Reading text files in python
"""" lec_fileio.py
Companion codes for the lecture on reading and writing files
"""
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')  # destination file


# ----------------------------------------------------------------------------
#   Opening the `SRCFILE` and reading its contents with the read method
# ----------------------------------------------------------------------------
# This will open the file located at `SRCFILE` and return a handler (file
# object):
fobj  = open(SRCFILE, mode='r')

# We can get the entire content of the file by calling the method `.read()`,
# without parameters:
cnts  = fobj.read()

# The variable `cnts` will be a string containing the full contents of the
# file. This will print the first 20 characters:
#print(cnts[:20])

# Check if the file is closed
#print(fobj.closed)  #-->False

# Close the file
#fobj.close()
#print(fobj.closed)

# ----------------------------------------------------------------------------
#   Comparing different approaches to get the contents
# ----------------------------------------------------------------------------
# Remember that we previously closed the file so we need to open it again
fobj = open(SRCFILE, mode='r')
# Contents using `.read`
#cnts = fobj.read()
#cnts = fobj.read()
print(f"First 20 characters in cnts: '{cnts[:20]}'")  # First 20 characters in cnts: 'Date,Open,High,Low,C'

# Start with an empty string
cnts_copy = ''
# Iterate over each line of fobj # <comment>
for line in fobj:
    # Add this line to the string `cnts_copy` # <comment>
    cnts_copy += line

# Print the result
print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")  # First 20 characters in cnts_copy: ''
# it is reading line by line

# close the file
fobj.close()


# ----------------------------------------------------------------------------
#   Reading one line at a time
# ----------------------------------------------------------------------------
#fobj = open(SRCFILE, mode='r')

# Read the first line
#first_line = next(fobj)

# After that, the fobj iterator now points to the second line in the file

#for line in fobj:
#    print(f"fobj now point to : '{line}'")
#    break
#

# close the file
#fobj.close()


# ----------------------------------------------------------------------------
#   Using context managers
# ----------------------------------------------------------------------------
# Instead of fobj = open(SRCFILE, mode='r'), use a context manager:

with open(SRCFILE, mode='r') as fobj:
    cnts = fobj.read()
    # Check if the object is closed inside the manager --> False
    print(f'Is the fobj closed inside the manager? {fobj.closed}')
#

# Notice that we did not close the object when using a context manager
# But after exiting the context manager, the file will automatically close
print(f'Is the fobj closed after we exit the manager? {fobj.closed}')  # -->Is the fobj closed after we exit the manager? True


# ----------------------------------------------------------------------------
#   Writing content to a file
# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")


#  This will create the file located at `DSTFILE` and write some content to it

with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line')
#

# Exiting the context manager will close the file
# We can then print its contents
print_lines(DSTFILE)  # line 0: This is a line


# If you open the same file again in writing mode, the line we wrote above
# will be erased:

with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is another line')
#
print_lines(DSTFILE)  # line 0: This is another line
# why? since we write it again, they will wipe out all the content. Then add the new message.


# ----------------------------------------------------------------------------
#   The write method does not add terminate the line.
# ----------------------------------------------------------------------------

with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line')
    fobj.write('This is a another line')
print_lines(DSTFILE)  # line 0: This is a lineThis is a another line
#

# ----------------------------------------------------------------------------
#   Notice that the write method does not add a newline character (\n). You
#   must add it yourself:
# ----------------------------------------------------------------------------

with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is a another line')
print_lines(DSTFILE)  # line 1: This is a another line
#


# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
# ----------------------------------------------------------------------------
def print_lines_rstrip(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: '{line.rstrip()}'")

#
with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is a another line')
print_lines_rstrip(DSTFILE)
# line 0: 'This is a line'
# line 1: 'This is a another line'
'''1.1 line endings when reading and writing next files
we can remove the newlines using the str.rstrip() method
this remove any newlines and spaces at the end of the string'''
# 两种方法
 with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: '{line.rstrip()}'")  # NEW

with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is a another line')
print_lines_rstrip(DSTFILE)  #

# ----------------------------------------------------------------------------
#   Quiz: Create the save_open function here
# ----------------------------------------------------------------------------
def safe_open(pth, mode):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.
    Will not open a file in writing mode if the file already exists and has
    some content.
    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
    """
    pass
###
'''IN-CLASS-EXERCISE2: create a function to find the most common word and its frequency in a text file?'''
# 4 data structure in the python standard library:
#
'''HINT
open()  # read file use open()function
split()  # split lines using split()function
get()   # count words use, returns the value of the item withe the specified way
syntax: dictionary.get(keyname, value)
keyname(required)-the key name of the item you want to return the value from
value(optional)- a value to return if the specified key does not exist. Default value None
'''
'''def freqword(filepath):
    with open(filepath) as file:
        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1
        maxcount = None
        maxword = None
        for word, count in counts.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count
    return(f"The most frquent word is: {maxword}, and the number of times appeared is: {maxcount}")
### call the function
freqword('iso.txt')
'''
# 2.0 introducing pandas- overview
# two primary data structures in pandas:
# Series(1-dimensional) and DataFrame(2-dimensional)
## using pandas in our project
import pandas as pd
# then open lec_pd_series