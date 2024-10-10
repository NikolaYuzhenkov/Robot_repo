# the methods and functions available to you:
#
# endswith() and startswith() string methods
# fnmatch.fnmatch()
# glob.glob()
# pathlib.Path.glob()

############################# Using String Methods #########################################
############################################################################################################
############################################################################################################

# Python has several built-in methods for modifying and manipulating strings.
# Two of these methods, .startswith() and .endswith(), are useful when you’re searching for patterns in filenames.
#     To do this, first get a directory listing and then iterate over it:

# import os
#
# # Get .txt files
# for f_name in os.listdir(r'C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles'):
#     if f_name.endswith('.txt'):
#         print(f_name)

############################# Simple Filename Pattern Matching Using fnmatch #########################################
############################################################################################################
############################################################################################################

# String methods are limited in their matching abilities.
# fnmatch has more advanced functions and methods for pattern matching.
# We will consider fnmatch.fnmatch(), a function that supports the use of wildcards such as * and ?
# to match filenames. For example, in order to find all .txt files in a directory using fnmatch, you would do the following:

# import os
# import fnmatch
#
# for file_name in os.listdir(r'C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles'):
#     if fnmatch.fnmatch(file_name, '*.txt'):
#         print(file_name)

############################# More Advanced Pattern Matching #########################################
############################################################################################################
############################################################################################################

# import os
# import fnmatch
#
# for filename in os.listdir(r'C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles'):
#     if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
#         print(filename)


############################# Filename Pattern Matching Using glob #########################################
############################################################################################################
############################################################################################################

# .glob() in the glob module works just like fnmatch.fnmatch(),
# but unlike fnmatch.fnmatch(), it treats files beginning with a period (.) as special.

# UNIX and related systems translate name patterns with wildcards like ? and * into a list of files. This is called globbing.
#
# For example, typing mv *.py python_files/ in a UNIX shell moves (mv) all files with the .py extension from the current directory to
# the directory python_files. The * character is a wildcard that means “any number of characters,” and *.py is the glob pattern.
# This shell capability is not available in the Windows Operating System.
# The glob module adds this capability in Python, which enables Windows programs to use this feature.
#
# Here’s an example of how to use glob to search for all Python (.py) source files in the current directory:

# import glob
# glob.glob('*.py')

# glob.glob('*.py') searches for all files that have the
# .py extension in the current directory and returns them as a list. glob also supports shell-style wildcards to match patterns:

# import glob
# for name in glob.glob('*[0-9]*.txt'): # This finds all text (.txt) files that contain digits in the filename
#     print(name)
#
# import glob
# for file in glob.iglob('**/*.py', recursive=True):
#     print(file)

# To recap, here is a table of the functions we have covered in this section:
#
# Function	Description
#
# startswith()	Tests if a string starts with a specified pattern and returns True or False
#
# endswith()	Tests if a string ends with a specified pattern and returns True or False
#
# fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the pattern and returns True or False
#
# glob.glob()	Returns a list of filenames that match a pattern
#
# pathlib.Path.glob()	Finds patterns in path names and returns a generator object