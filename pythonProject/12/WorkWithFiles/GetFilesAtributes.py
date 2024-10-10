############################# Getting File Attributes ######################################################
############################################################################################################
############################################################################################################

# Python makes retrieving file attributes such as file size and modified times easy.
# This is done through os.stat(), os.scandir(), or pathlib.Path().

# The examples below show how to get the time the files in  were last modified. The output is in seconds:

################################ import os ##################################

# import os
# with os.scandir(r'C:\Users\Nikola\Robot_repo\pythonProject\12') as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)


################################ from pathlib import Path ##################################

# from pathlib import Path
# current_dir = Path(r'C:\Users\Nikola\Robot_repo\pythonProject\12')
# for path in current_dir.iterdir():
#     info = path.stat()
#     print(info.st_mtime)

# list. The st_mtime attribute returns a float
# value that represents seconds since the epoch.
# To convert the values returned by st_mtime for display purposes,
# you could write a helper function to convert the seconds into a datetime object:

# from datetime import datetime
# from os import scandir
#
# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date
#
# def get_files():
#     dir_entries = scandir(r'C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles')
#     for entry in dir_entries:
#         if entry.is_file():
#             info = entry.stat()
#             print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
#
# get_files()