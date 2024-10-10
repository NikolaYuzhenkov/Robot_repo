############################# Making Directories ######################################################
############################################################################################################
############################################################################################################

# os.mkdir()	Creates a single subdirectory
# pathlib.Path.mkdir()	Creates single or multiple directories
# os.makedirs()	Creates multiple directories, including intermediate directories

################################### Creating a Single Directory ######################################

####### import os
# import os
# os.mkdir(r'C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles\NewDir')

###### from pathlib import Path

# from pathlib import Path
#
# p = Path('example_directory')
# try:
#     p.mkdir()
# except FileExistsError as exc:
#     print(exc)

# Alternatively, you can ignore the FileExistsError by passing the exist_ok=True argument to .mkdir():
# This will not raise an error if the directory already exists.

# from pathlib import Path
#
# p = Path('example_directory')
# p.mkdir(exist_ok=True)


############################# Creating Multiple Directories ######################################################
############################################################################################################
############################################################################################################

# os.makedirs() is similar to os.mkdir(). The difference between the two is that not only can os.makedirs()
# create individual directories, it can also be used to create directory trees. In other words, it can create any
# necessary intermediate folders in order to ensure a full path exists.
#
# os.makedirs() is similar to running mkdir -p in Bash. For example, to create a group of directories like 2018/10/05,
# all you have to do is the following:

# import os
#
# os.makedirs('2018/10/05')
#
# .makedirs() creates directories with default permissions. If you need to create directories with different
# permissions call .makedirs() and pass in the mode you would like the directories to be created in:



# import os
#
# os.makedirs('2018/10/05', mode=0o770) # iTS Like CHMOD in Linux

