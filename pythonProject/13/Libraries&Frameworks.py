import os
import random
import shutil
import time
from itertools import count, cycle, repeat

import argparse as argparse

############################################### IMPORT OS (Work with OS systems) #################################################

import os

# GETCWD (ПОКАЗАТИ ТЕПЕРЕШНЮ ДЕРИКТОРІЮ)

# print("Current dir:", os.getcwd())

# CHDIR (ЗМІНА ДЕРИКТОРІЇ)

# os.chdir(r"C:\Users\Nikola\Robot_repo\pythonProject\13")
# print("Current dir:", os.getcwd())

# GETENV (ПОКАЗУЄ РОБОЧЕ СЕРИДОВИЩЕ)

# print(os.getenv('PATH'))

# CHMOD (ЗМІНИТИ ПРАВА ДОСТУП ДО ФАЙЛУ)

# os.chmod(r"C:\Users\Nikola\Robot_repo\pythonProject\3\ClassWork.3.py", mode=777)

# CHOWN (ЗМІНИТИ ФЛАСНИКА ФАЙЛУ)

# os.chown(r"C:\Users\Nikola\Robot_repo\pythonProject\3\ClassWork.3.py", 1)

# LISTDIR (ПОКАЗУЄ СПИСОК ДЕР ТА ФАЙЛІВ)

# print(os.listdir(r"C:\Users\Nikola\Robot_repo\pythonProject"))

# dir_list = os.scandir(r"C:\Users\Nikola\Robot_repo\pythonProject")
#
# for i in dir_list:
#     print(i)

# # MKDIR
#
# os.mkdir('test_dir')

# RENAME

# os.rename('test_dir', 'super_dir')

# RMDIR
# try:
#     os.rmdir("super_dir")
# except FileNotFoundError as Dos:
#     print("Файл не был найен")

# help(os)


############################################### SHUTIL (ТАКОЖ ДЛЯ РОБОТИ З ФАЙЛАМИ СИСТЕМИ)#################################################

# COPY

# shutil.copy('test_file1', 'new_copied_file')

# COPYTREE (Копією усю директорію рекурсивно)

# shutil.copytree(r"C:\Users\Nikola\Robot_repo\pythonProject\3", 'copy_of_3')

# RMTREE
# os.chmod(r"C:\Users\Nikola\Robot_repo\pythonProject\13\copy_of_3", 0o777)
# shutil.rmtree(r"C:\Users\Nikola\Robot_repo\pythonProject\13\copy_of_3", )

# MOVE
# shutil.move('test', r"C:\Users\Nikola\Robot_repo\pythonProject\13\New_Test_With_Tes_Inside") # MOVE FILE

# shutil.move(r'C:\Users\Nikola\Robot_repo\pythonProject\13\New_Test_With_Tes_Inside\test', r"C:\Users\Nikola\Robot_repo\pythonProject\13\New_Test_With_Tes_Inside\test_renamed") #RENAME FILE

# CHOWN

# shutil.chown()


###############################################  ITERTOOLS (СТОВРЕННЯ ІТЕРАТОРІВ ТА РОБОТА З ІТЕРАТОРАМИ)#################################################

from itertools import count, cycle, repeat, accumulate, chain, permutations

# COUNT

# for i in count(1): #ЛІЧИЛЬНИК
#     print(i)


# CYCLE (потворює значення ітератора в нескінченному циклі)

# for i in cycle([1, 2, 3, 4, 5]): # ПОЧЕРЗІ ОТРИМАЄМО КОЖЕН ЕЛЕМЕНТ ЛІСТА
#     print(i)

# REPEAT

# for i in repeat(1, 4): # Вказується скільки разі потрібно друкувати той чи інший обєкт
#     print(i)

# accumulate, chain, permutations

# ACCUMULATE

# for n in accumulate([1, 2, 3, 4, 5]) # АККУМУЛЯЦІЯ - ПОВЕРТАЄ значення у вигляді ітератора які аккумулють в процесі тіерації, обчислює суми накопичуваних значень


# CHAIN

# for i in chain([1, 2, 3], [1, 3, 5, 6,]): # ОБЄДНУЄ ІТЕРАТОРИ У ЛАНЦЮЖОК
#     print(i)

# PERMUTATIONS  ВИДАЄ КОМБІНАЦІЇ ІТЕРОВАНИХ ОБЄЕКТІВ, В ТІЙ КІЛЬКОСТІ ЯКІЙ МИ ВКАЖЕМО або в усіх можливих варіаціях


# for n in permutations('ABCD', 2):
#     print(n)

# for n in permutations('123'):
#     print(n)



###############################################  ARGPARSE ( ДЛЯ РОБОТИ З АРГУМЕНТАМИ З КОНСОЛІ)#################################################

# import argparse
#
# parser = argparse.ArgumentParser() # ІНІЦІАЛІЗУВАЛИ ОБЄКТ КЛАСУ ArgumentParser()
# parser.add_argument('command')
# parser.add_argument('first_name')
# parser.add_argument('last_name')
#
# args = parser.parse_args()
# print(args)
# print(args.command)
# print(args.first_name)
# print(args.last_name)

# ВЫЗВАТЬ ЭТУ ХРЕНЬ НУЖНО ЧЕРЕЗ ТЕРМИНАЛ ИСПОЛЬЗУЯ ПУТЬ И ТАКОЙ ФОРМАТ  - python "C:\Users\Nikola\Robot_repo\pythonProject\13\Libraries&Frameworks.py" greet John Doe
# Таким образом собздается вот такой обьект - Namespace(command='add', first_name='Nikola', last_name='Yuzhenkov')
# Це потрібно тоді коли ви працюєте з програмиами з якими ви працюєте в консолі й передаються певні аргументи й після цьбого їх можна прйимати та потім парсити



###############################################  TIME #################################################

# TIME(), SLEEP

# print(time.time()) # ЗАПИС В СЕКУНДАХ ХЗ З ЯКОГО ЧАСУ
# print('start')
# time.sleep(3)
# print('end')

###############################################  DATETIME #################################################
from datetime import datetime

# now(), isoformat(), strftime, strptime

# NOW

# print(datetime.now().isoformat()) # - Return the time formatted according tt(datetime.now()) # 2024-10-09 22:04:19.537490
# #
# # prino ISO.

# STRFTIME

# now = datetime.now()
# print(now.strftime("%Y-%m/%d, %H:%M")) # Format using strftime(). Example: "%d/%m/%Y, %H:%M:%S" ВСЕ ОКРІМ ШАБЛОНУ ДАТИ ЬУДЕ ПРИЙНЯТО ЯК ТЕКСТ

# STRPTIME

# my_date = "2023-01-16"
# new_date = datetime.strptime(my_date, "%Y-%m-%d")
# print(new_date)
# print(type(new_date))

# 2023-01-16 00:00:00
# <class 'datetime.datetime'>

# my_date = datetime(day=1, year=2020, month=4) # СТВОРЕННЯ ВЛАСНОЇ ДАТИ ФОРМАТУ # <class 'datetime.datetime'>

###############################################  RANDOM  #################################################

import random

# RANDINT

# print(random.randint(0, 1999)) # ДІАПАЗОН РАНДОМУ З A TO B

# CHOICE

# print(random.choice([1, 2, 3, 4, 5, 6])) # РАНДОМНО ПОВЕРТАЄ ЕЛІМЕНТ ЛИСТА

# CHOICES

print(random.choices([1, 2, 3], [0.1, 0.1, 0.8], k=3)) # РАНДОМНО ПОВЕРТАЄ ЕЛІМЕНТ ЛИСТА
# ПЕРШИЙ - ЦЕ ДІАПАЗОН, СПИСОК, 2 - WEIGHTS,(WEIGHTS ОЗНАЧАЄ, ШАНС ВИПАДІННЯ У НАШОМУ ВИПАДКУ 3 БУДЕ НА 80 ВІДСОТКІВ БІЛЬШЕ ЧАСТІШЕ ВИПАДАТИ),
# K = 2 ОЗНАЧАЄ, ЩО СКІВЛЬКО ОБЄКТІВ ЗІ СПИСКУ ПОТРІБНО ВЗЯТИ

# SHUFFLE



###############################################  TYPING  ??? #################################################

# from typing import List, Set, Dict, Tuple
#
# def print_list(lst: List) -> None:
#     print(lst)
#
# print_list([1, 2, 3, 4])
# print_list(2)
# print_list("asfasf")

###############################################  SYS ???????? #################################################

import sys

###############################################  TKINTER ????????? #################################################


