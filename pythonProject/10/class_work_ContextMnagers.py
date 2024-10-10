# Викликати функцію як менеджер контексту:
#
# Ключове слово with <ctx> as <var> de:
#     ctx - виклик функції яка є менеджером контексту
#     var - це результат який поверта. функція

########## EXAMPLE ################

# with open('text.txt', 'r+') as my_file:
#     print(my_file.read())
#
# ---> В цьому прикладі менеджер контексту це функція open.
# ---> Результат виконанная записанний в змінну my_file


############### EXAMPLE WITHOUT МЕНЕДЖЕРУ КОНТЕКСТУ ################

# my_file = open('text.txt', 'r+')
# print(my_file.read())
#
# my_file.close() - ТОБТО ЗАВЖИ НЕОБХІДНО БУДЛЕМ ПОТІМ ЗАКРИВАТИ ФАЙЛ В РУЧНУ

######################## СТВОРЕННЯ ВЛАСНОГО МЕНЕДЖЕРУ КОНТЕКСУТ #######################

# Для створення потрібно реалізувати два методи - _enter_ та _exit_ усе це свторенно у класі - class.

########################## LIVE CODING #####################

# my_file = open('file_text.txt', 'r+') - БЕЗ МЕНЕДЖЕРА КОНТЕКСТУ
# print(my_file.read())
# my_file.close()

# with open('file_text.txt', 'r+') as my_file: # - З МЕНЕДЖЕРОМ КОНТЕКСТУ
#     print(my_file.read())

###################### НАПИСАННЯ ВЛАСНОГО МЕНЕДЖЕРА КОНТЕКСТУ ###################

# class MyManager:
#     def __enter__(self):
#         print('Enter method')
#         return 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exit method')
#         return 1
#
#
# with MyManager():
#     print('Something inside my context manager')
#
# print('End of program')

################### ПАРАМЕТРИ МЕТОДІВ enter та exit #####################3

# class MyManager:
#     def __enter__(self):
#         print('Enter method')
#         return 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exit method')
#         return 1
#
# #ЗАГАЛОМ ПРИ ВИКОРИСТАННІ МЕНЕДЖЕРУ У НАС МОЖЕ ВИНИКНУТИ ПЕВНА ПОМИЛКА, ПРИ ВИНИКНЕННІ ПОМИЛКИ БУДЕ ЗАСТОСОВУВАТИСЬ МЕТОД EXIT
# # У САМОГО МЕТОДУ EXIT Є ДЕКІЛЬКА ПАРМАЕТРІВ - def __exit__(self, exc_type, exc_val, exc_tb):
# # ПРИ ВИНИКННІ ПОМИЛКИ МИ МОЖЕМО ХАДАТИ ПАРАМЕТРИ ДЛЯ ОБРОБКИ ПОМИЛКИ
# # exc_type - визначитит тип помилки
# # exc_val - отримати значення аке викликало помилку
# # exc_tb - отримати інформрацію, що і яка помлідовність дій призвела до помилки
#
# with MyManager():
#     print('Something inside my context manager')
#
# print('End of program')

######### НАПИШЕМО МЕНЕДЖЕР КОНТЕКСТУ ЯКИЙ БУДЕ ОБРОБЛЮВАТИ КЕЙС КОЛИ МИ ЗВЕРТАЄМОСЬ ДО КЛЮЧА ЯКИЙ НЕ ІСНУЄ В СЛОВНИКУ #############

class MyDictContextManger:
    def __enter__(self):
        print('Start method "Enter"')
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == KeyError:
            print('Start method "Exit"')
            print(f'Key {exc_val} does not exist')
        return True # потрібно для того аби наша программа не звершилась
        #print(exc_type, exc_val) # Дивимось ща записанно у відповідних змінних стосвно помилки


my_dict = {}

with MyDictContextManger():
    print(my_dict['test'])

print('end')