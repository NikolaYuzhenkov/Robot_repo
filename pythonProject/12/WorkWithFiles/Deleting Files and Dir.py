################################### Deleting Files in Python ###############################################
############################################################################################################
############################################################################################################

# To delete a single file, use pathlib.Path.unlink(), os.remove(). or os.unlink().
#
# os.remove() and os.unlink() are semantically identical. To delete a file using os.remove(), do the following:


################################### os.remove ###############################################
# import os
#
# data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
# os.remove(data_file)

################################### os.unlink(data_file) ###############################################

# import os
#
# data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
# os.unlink(data_file)

################################### Deleting Directories ###############################################
############################################################################################################
############################################################################################################

# The standard library offers the following functions for deleting directories:
#
# os.rmdir()
# pathlib.Path.rmdir()
# shutil.rmtree()


########################################### os.rmdir(trash_dir) ####################################
# import os
#
# trash_dir = 'my_documents/bad_dir'
#
# try:
#     os.rmdir(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')
#

########################################### from pathlib import Path ####################################

# from pathlib import Path
#
# trash_dir = Path('my_documents/bad_dir')
#
# try:
#     trash_dir.rmdir()
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')


################################### Deleting Entire Directory Trees ###############################################
############################################################################################################
############################################################################################################

# To delete non-empty directories and entire directory trees, Python offers shutil.rmtree():

# import shutil
#
# trash_dir = 'my_documents/bad_dir'
#
# try:
#     shutil.rmtree(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')

# import os
#
# for dirpath, dirnames, files in os.walk('.', topdown=False):
#     try:
#         os.rmdir(dirpath)
#     except OSError as ex:
#         pass



# Function
# os.remove() --	Deletes a file and does not delete directories
#
# os.unlink()	-- Is identical to os.remove() and deletes a single file
#
# pathlib.Path.unlink()	-- Deletes a file and cannot delete directories
#
# os.rmdir()	-- Deletes an empty directory
#
# pathlib.Path.rmdir()	-- Deletes an empty directory
#
# shutil.rmtree()	-- Deletes entire directory tree and can be used to delete non-empty directories