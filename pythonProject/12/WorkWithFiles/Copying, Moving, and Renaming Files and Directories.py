################################### Copying Files in Python ###############################################
############################################################################################################
############################################################################################################



################################################ shutil.copy(src, dst) #################################################
# import shutil
#
# src = 'path/to/file.txt'
# dst = 'path/to/dest_dir'
# shutil.copy(src, dst)
#
# shutil.copy() is comparable to the cp command in UNIX based systems.
# shutil.copy(src, dst) will copy the file src to the location specified in dst.


################################### Copying Directories ###############################################
############################################################################################################
############################################################################################################

# >>> import shutil
# >>> shutil.copytree('data_1', 'data1_backup')
# 'data1_backup'

# In this example, .copytree() copies the contents of data_1 to a new location data1_backup and returns
# the destination directory. The destination directory must not already exist. It will be created as well as
# missing parent directories. shutil.copytree() is a good way to back up your files.

################################### Moving Files and Directories ###############################################
############################################################################################################
############################################################################################################

# import shutil
# shutil.move('dir_1/', 'backup/')
#
# shutil.move('dir_1/', 'backup/') moves dir_1/ into backup/ if backup/ exists.
# If backup/ does not exist, dir_1/ will be renamed to backup.

################################### Renaming Files and Directories ###############################################
############################################################################################################
############################################################################################################

# Python includes os.rename(src, dst) for renaming files and directories:
#
# os.rename('first.zip', 'first_01.zip')