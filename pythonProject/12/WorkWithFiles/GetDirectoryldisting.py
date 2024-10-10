############################# Python’s “with open(…) as …” Pattern #########################################
############################################################################################################
############################################################################################################
# open a text file and read its contents

# with open('data.txt', 'r') as f:
#     data = f.read() #  r opens the file in read only mode
# print(data)
#
#
# with open('data.txt', 'w') as f:
#     data = 'some data to be written to the file'
#     f.write(data)

########################### Getting a Directory Listing os.scandir() and pathlib.Path(). ###################################

############################ os.scandir ############################


# import os
# entries = os.scandir(r'C:\Users\Nikola\Robot_repo\pythonProject\4')
# print(entries)
#
# for entry in entries:
#     print(entry.name)


############################ from pathlib import Path ############################

# from pathlib import Path
#
# entries = Path(r'C:\Users\Nikola\Robot_repo\pythonProject\4')
# print(entries)
# for entry in entries.iterdir():
#     print(entry.name)

# In the example above, you call pathlib.Path() and pass a path argument to it.
# Next is the call to .iterdir() to get a list of all files and directories in my_directory.



############################# Listing All Files in a Directory #########################################
############################################################################################################
############################################################################################################


# This section will show you how to print out the names of files in a directory using os.listdir(), os.scandir(),
# and pathlib.Path(). To filter out directories and only list files from a directory listing produced by os.listdir(), use os.path:


########################### import os #########################################

# import os
# basepath = r'C:\Users\Nikola\Robot_repo\pythonProject\12'
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)


########################### from pathlib import Path #########################################


# from pathlib import Path
#
# basepath = Path(r'C:\Users\Nikola\Robot_repo\pythonProject\12')
# files_in_basepath = basepath.iterdir()
# for item in files_in_basepath:
#     if item.is_file():
#         print(item.name)



############################# Listing Subdirectories #######################################################
############################################################################################################
############################################################################################################

# To list subdirectories instead of files, use one of the methods below. Here’s how to use os.listdir() and os.path():

################################# # List all subdirectories using scandir() ################################

import os

# List all subdirectories using scandir()
# basepath = r'C:\Users\Nikola\Robot_repo\pythonProject\12'
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_dir():
#             print(entry.name)


################################# # List all subdirectory using pathlib ################################

# from pathlib import Path
#
#
# basepath = Path('my_directory/')
# for entry in basepath.iterdir():
#     if entry.is_dir():
#         print(entry.name)

