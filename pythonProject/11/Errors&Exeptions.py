# it = iter([1, 2, 3])
# while True:
#     print(next(it)) # StopIteration ERROR

############################ SYNTAX ERROR ###############################

# fr in [1, 2]: # SyntaxError: invalid syntax
# print(a)


############################ NAME ERROR ################################

# print(a) # NameError: name 'a' is not defined

############################ Identation errorr ################################

# if True:
# print('This is true') IndentationError: expected an indented block after 'if' statement on line 17

############################ TYPE ERROR ################################

# print('text' / 1) TypeError: unsupported operand type(s) for /: 'str' and 'int'

############################ INDEX ERROR ################################

# lst = [1, 2]
# print(lst[2]) IndexError: list index out of range

############################ KEY ERROR ################################

# dct = {'test': 1}
# print(dct['some']) KeyError: 'some'

############################ KEYBOARD INTERRUPT ERRORR ################################

# while True:
#     print('1') # KeyboardInterrupt

############################ STOP ITERRATION ################################

# lst = iter([1, 2])
# while True:
#     print(next(lst)) #StopIteration


############################ VALUE ERROR ################################

# int('test') #ValueError: invalid literal for int() with base 10: 'test'


############################ ATTRIBUTE ERRORR ################################

# lst = [1, 2]
#
# lst.print() AttributeError: 'list' object has no attribute 'print'
#
#
#
#
#
#
#
#
###################################### ОБРОБКА ПОМИЛОК (try / except)##################################

# ПРИКЛАД БЕЗ ПОМИЛКИ
# try:
#     print('This is try')
# except Exception:
#     print('Exeption')
#
# # ПРИКЛАД З ПОМИЛКОЮ
#
# try:
#     zero = 1 / 0
#     print('This is try')
# except Exception:
#     print('Exeption')
#
# # ПРИКЛАД З КОДОМ, ЩО НЕ ОЧІКУЄ НА ПОМИЛКУ ЯКА ВИНИКЛА (КОД TRY... EXCEPT... ПРОСТО ПРОПУСКАЄТЬСЯ)
#
# try:
#     zero = 1 / 0 # ZeroDivisionError: division by zero
# except TypeError:
#     print('Wrong Type')
#
# # ПРИКЛАД З "EXEPTION"
#
# try:
#     zero = 1 / 0
# except Exception: # Exception - включає у себе усі можилві помилки
#     print('Some Exeption occured')

## ПРИКЛАД ОЧІКУВАННЯ І ОБРОБКА МОЖИЛВИХ ПОМИЛОК ВІДПОВІДНО ЛОГІКИ ПРОГРАМИ
# (ПЕРЕДБАЧАЄМО ВИНЕКНЕННЯ ЖЕКЯКИХ ПОМИЛОК І КАЄЕМО ПРОГРАМІ, ЩО ЗРОБИТИ У РАЗІ ЇХ ВИНИКНЕННЯ)

# my_dict = {'key1': 1, 'key2': 2}
# try:
#     key = 'key3'
#     print(my_dict[key])
# except KeyError: # ПЕРШИЙ БЛОК ДЛЯ ТИПІВ ПОМИЛОК KeyError (ЯКЩО ВИКОНОВСЯ ПЕРШИЙ КОД, ТО ДРУГИЙ ЕКСЕПТ ВЖЕ НЕ ВИКОНАЄТЬСЯ)
#     key = list(my_dict.keys())[0]
#     print(my_dict[key])
# except Exception: # ЖРУГИЙ БЛОК ДЛЯ ТИПІВ ПОМИЛОК (УСІХ ІНШИХ)
#     print('Some unknown exception occured')
#
#

################################ ОБРОБКА ПОМИЛОК FINALLY ТА ПОЛЕ ДЛЯ ЛОГІНУ #################################

# TRY.. EXCEPT.. ТАКОЖ МОЖЕ МІСТИТИ БЛОК FINALLY: ЦЕ УМОВА ЯКА БУДЕ ВИКОНАНА НЕЗАЛЕЖНО ВІД ТОГО
# ЧИ ВИНИКНЕ ПОМИЛКА ПІД БЛОКОМ TRY ЧИ НІ.

# pin = 1234
# max_tried = 3
# permission = False
#
# while permission is False and max_tried > 0:
#     try:
#         _pin = input('Enter a pin:')
#         if int(_pin) == pin:
#             print('Pin is correct')
#             permission = True
#     except ValueError:
#         print('Pin should contain only digits')
#     finally: # КОД ВИКОНАЄТЬСЯ ЗА БУДЬ-ЯКИХ УМОВ
#         max_tried -= 1
#         print(f'{max_tried} attampts left. Permission {"granted" if permission else "denied"}')


################################## ОБРОБКА ПОМИЛОК TRY... ELSE.... ############################
# ЦЕМ МЕТОД ВВАЖАЄТЬСЯ КРАЩИМ НІЖ МИНУЛИЙ
#
# ЗАМІСТЬ ТОГО АБИ ПОМІЩАТИ ВЕСЬ НАШ КОД В БЛОК TRY МИ ПОМІЩАЄМО ТУДИ ЛИШЕ ЧАСТИНУ
# ЩО МОЖЕ ВИКЛИКАТИ ПОМИЛКУ, А ВСЮ ІНШУ ЛОГІКУ ПИШЕМО В ELSE:

# pin = 1234
# max_tried = 3
# permission = False
#
# while permission is False and max_tried > 0:
#     try: # ТОБТО У ЦЬОМУ БЛОЦІ ПИШЕМО ЛИШЕ КОД ЯКИЙ МОЖЕ ВИКЛИКАТИ ПОМИЛКУ
#         _pin = int(input('Enter a pin:'))
#     except ValueError:
#         print('Pin should contain only digits')
#     else: # БУДЕ ВИКОНУВАТИСЬ У ВИПАДКУ ЛИШЕ ЯКЩО НЕ ВИНЕКНЕ ЖОДНИХ ПОМИЛОК
#         if  _pin == pin:
#             print('Pin is correct')
#             permission = True
#     finally: # КОД ВИКОНАЄТЬСЯ ЗА БУДЬ-ЯКИХ УМОВ
#         max_tried -= 1
#         print(f'{max_tried} attampts left. Permission {"granted" if permission else "denied"}')


############################## ВИКОРИСТАННЯ ТЕКСТУ ПОМИЛОК ####################################

# try:
#     zero = 1 / 0
# except ZeroDivisionError as zde: # ЗАПИСАЛИ У ЗМІННУ ТЕКСТ ПОМИЛОК
#     print(f'Zero division: {zde}')
#
#
#
#
#
#
#
#
#
#
############################### КАСТОМНІ ВИНЯТКИ (ПОМИЛКИ) #######################################

# ЩОБ ЗРОБИТИ СВІЙ ВИНЯТОК ПОТРІБНО СТВОРИТИ КЛАСС ТА УНАСЛІДУВАТИ ЙОГО ВІД КЛАССУ Exception:

# class MyException(Exception):
#     pass

# ТЕПЕР ЦЕЙ ВИНЯТОК МОЖНА ВИКОРИСТОВУВАТИ В ПРОГРАММІ, ДЛЯ ЇЇ ВИКЛИКУ СЛІД ВИКОРИСТОВУВАТИ КЛЮЧОВЕ СЛОВО "RAISE":

# if True:
#     raise MyException()

# МОЖЕМО ДОДАТИ МЕСЕДЖ ДО ПОМИЛКИ

# if True:
#     raise MyException('This is my custom error')
#
#
#
#
#
#
#
#
################################  TRY EXCEPT LIVE CODING ################################

################################  TRY EXCEPT: KEY ERROR ################################

# dct = {'key': 1}
#
# try:
#     print(dct['other key'])
# except KeyError:
#     print('Key does not exist')

################################  TRY EXCEPT: ZERO DEVISION ################################

# try:
#     print(1 / 0)
# except ZeroDivisionError as zde:
#     print(zde)
#     print('На нуль ділити нізя')

# try:
#     print(1 / 0)
# except  Exception as e:
#     print(type(e), e)

################################  TRY EXCEPT FINALLY: PHONEBOOK RECORDS ################################

# phone_book = {'Nikola': 123456}
# counter = 5
#
# while True and counter:
#     name = input('Enter name: ')
#     try:
#         print(phone_book[name])
#     except KeyError:
#         print(f'Key {name} does not exist')
#     finally:
#         counter -= 1
#
# print('You reached the limit. Restart the programm')

################################  TRY EXCEPT ELSE FINALLY: PHONEBOOK RECORDS ################################

# phone_book = {'Nikola': 123456}
# counter = 5
#
# while True and counter:
#     name = input('Enter name: ')
#     try:
#         value = phone_book[name]
#     except KeyError:
#         print(f'Key {name} does not exist')
#     else:
#         print(value)
#     finally:
#         counter -= 1
#
# print('You reached the limit. Restart the programm')
#
#
#
#
#
#
#
#
#
#
############################### CUSTOM EXCEPTIONS ##################################

# class MyExeption(Exception):  # КЛАСИ ПРИЙНЯТО ПИСАТИ З ВЕЛИКОЇ БУКВИ
#     pass # ОЗНАЧАЄ НІЧОГО БІЛЬШЕ НЕ РОБИТИ
#
# raise MyExeption('Custom MSG for Error')

# raise ValueError('This is value error')

# try:
#     raise ValueError('Test err')
# except ValueError as ve:
#     print(ve)