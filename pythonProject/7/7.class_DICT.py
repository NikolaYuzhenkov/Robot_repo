# { } - для свторення словнику
# вбудована функція dict - для стоврення словнику
# > dct = {}
# > new_dct = dict()
# > dct_with_data = {'data1':'This is sime data1', 'data2':'another data'} - ОБМЕЖЕННЯ - значенням для ключів можуть бути лише
#immutable(незмінні) дані, це - str, int, tuple
# Впорядковані дані. Кожен елемент має свій ключ і значення.
# Змінювані дані. Dictionary можна змінити: додати або видалити певні елементи.
# Унікальні дані. Не може бути 2 однакових ключів, проте значення для різних ключів можуть повторюватися.

########## ДОСТУП ДО ЕЛЕМЕНТІВ DICT  #########

# → Для доступу до елементів використовується назва ключа в квадратних дужках, або метод get().
# Безпечніше використовувати саме метод get(), оскільки, якщо ключа не існує, при використанні синтаксису із квадратними дужками виникне помилка:
# > spends = {'food': 500, 'car': 200, 'education': 100}
# > spends['food'] # 500
# > spends.get('food') #500
# > spends['travel'] # error
# > spends.get('travel') # None
# Щоб додати елемент, достатньо записати назву ключа в квадратних дужках і присвоїти йому значення:
# > spends['travel'] = 0
# > spends.get('travel') # 0


# Важливо розуміти, що доступ за ключем і доступ через get має відмінності.
# Крім вже зазначеної, основна відмінність полягає в тому, що через get ми можемо отримати дані тільки для читання,
# тоді як при доступі за ключем ми можемо змінити значення:
# > spends['travel'] = 100
# > spends.get('travel') # 100
# > spends['travel'] += 100
# > spends.get('travel') # 200
# Якщо присвоїти існуючому елементу нове значення, то воно перезапишеться, оскільки ключі не дублюються:
# > spends.get('travel') # 200
# > spends['travel'] = 0
# > spends.get('travel') # 0

############## CREATE A DICT ###############

# my_dict = {}
# my_dict2 = dict()

# my_spends = { #бажано словник записувати саме атким чином
#     'travel': 0,
#     'food': 0,
#     'transport': 0,
# }

# print(my_spends.get('travel'))
# print(my_spends['travel'])
#
# if my_spends.get('subscription') is None:
#     print('There is no such key')

# key = input('Enter a key: ')

# if my_spends.get(key) is None:
#      print(f'There is no {key} key')

# while True:
#     user_input = input('Enter a command: ') #format "command amount category" commands: add, remove
#     splited_input = user_input.split()
#
#     command = splited_input[0]
#     amount = int(splited_input[1])
#     category = splited_input[2]
#
#     if my_spends.get(category) is None:
#         my_spends[category] = 0
#
#     if command == 'add':
#         my_spends[category] += amount
#     elif command == 'remove':
#         my_spends[category] -= amount
#     elif command == 'get':
#         print(my_spends.get(category))




################## CREATE DICT FROM LIST OF LISTS ##################3

# users_lists = [
#     ['1234532', 'John'],
#     ['234235', 'Sara'],
#     ['2342353', 'Clark']
# ]
#
# print(dict(users_lists)) # Елемент у списку з індексом нуль стає ключем

################ get element by key: get() and [] #####################
# my_dict={'first': 1, 'second': 2, 'third': 3}
# print(my_dict['first'])
# print(my_dict.get('first'))  ### ЦЕЙ СПОСІБ БАЖАНИЙ ОСКІЛЬКИ ВІН НЕ ВИКЛИКАЄ ПОМИЛКИ

#################### update element by key: update and [] ###################3333
#my_dict = {'first': 1, 'second': 2, 'third': 3}
#my_dict['first'] = 10
#my_dict['fourth'] = 4
#print(my_dict)

########### BUILD METHODS --> KEYS(), VALUES(), ITEMS() ###############

############ KEYS() ############## - БЕРЕ ВИБІРКУ З КЛЮЧІВ СЛОВНИКА І ПЕРЕТВОРЮЄ ЇХ В ЛІСТ

# my_dict = {'first': 1, 'second': 2, 'third': 3}
#
# print(list(my_dict.keys())) # - перетворює в ліст саме ключі, цей метод взагалі робе вибірку ключів

################### VALUES() #################### - РОБЕ ВИБІРКУ ЗІ ЗНАЧЕНЬ СЛОВНИКА

# my_dict = {'first': 1, 'second': 2, 'third': 3}
#
# print(list(my_dict.values()))

################ ITEMS() #####################33

# my_dict = {'first': 1, 'second': 2, 'third': 3}
#
# print(my_dict.items()) # МИ ОТРИМАЄМО ЛІСТ З ЕЛЕМЕНТАМИ ЗА ТИПОМ TUPLE
#
# for key, value in my_dict.items(): # ТАКИМ ЧИНОМ ЕЛЕМЕНТИ РОЗПАКУЮТЬСЯ І ЇХ МОЖНА ЗАПИСАТУ КОЖНУ У РІЗНУ ЗМІННУ
#     print(key, value)

#####################  UPDATE() ############################

# dct = {'1': 1}
# dct.update({'1': 2})
# print(dct)
#
# dct.update({'one': 3, 'second': 4}) # - Якщо елементу нема то він просто зявиться
# print(dct)

#################### DEL delete item from dicts #################

# del dct['one'] # ВИДАЛЯЄ ЗНАЧЕННЯ ЗА КЛЮЧЕМ
# print(dct)