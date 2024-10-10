############################# # Walking a directory tree and printing the names of the directories and files #########################################
############################################################################################################
############################################################################################################

# Let’s explore how the built-in Python function os.walk() can be used to do this. os.walk() is used to generate filename
# in a directory tree by walking the tree either top-down or bottom-up. For the purposes of this section,

# The following is an example that shows you how to list all files and directories in a directory tree using os.walk().
#
# os.walk() defaults to traversing directories in a top-down manner:

# import os
# for dirpath, dirnames, files in os.walk('.'):
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         print(file_name)