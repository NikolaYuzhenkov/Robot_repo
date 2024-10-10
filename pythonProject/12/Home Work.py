# 1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.
#
# Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
# При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
# Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл) і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.
#
# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.
#
# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.


#
# with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="w", encoding="utf-8") as write_file:
#     json.dump(file_name, write_file)

import json

# Инициализируем словарь для телефонной книги
phone_book_dict = {}

# Загружаем данные из файла при старте программы
try:
    with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="r",
              encoding="utf-8") as read_file:
        phone_book_dict = json.load(read_file)
except FileNotFoundError:
    print("Файл не найден, создана новая книга.")
except json.JSONDecodeError:
    print("Ошибка чтения файла, создана пустая телефонная книга.")
    phone_book_dict = {}

while True:
    try:
        command_input = input('Введите вашу команду: ')
        splited_input = command_input.split()
        command = splited_input[0].lower()

        # Проверяем наличие второго аргумента (например, имени)
        if len(splited_input) > 1:
            key = splited_input[1]
        else:
            key = None

    except IndexError:
        print("Ошибка: неверный ввод команды. Попробуйте еще раз.")
        continue

    if command == 'stats':  # stats: количество записей
        print('Количество записей в словаре равно:', len(phone_book_dict))

    elif command == 'add':  # add: добавить запись
        if key is None:
            print("Ошибка: не указано имя для добавления.")
            continue

        if key in phone_book_dict:
            print(f"Контакт с именем {key} уже существует.")
        else:
            phone_number = input(f"Введите номер для {key}: ")
            if phone_number.isdigit():
                phone_book_dict[key] = phone_number
                print(f"Контакт {key} с номером {phone_number} добавлен.")

                # Сохраняем обновления в файл
                with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="w",
                          encoding="utf-8") as write_file:
                    json.dump(phone_book_dict, write_file, ensure_ascii=False, indent=4)
            else:
                print('Номер может содержать только числа')

    elif command == 'delete':  # delete <name>: удалить запись
        if key is None:
            print("Ошибка: не указано имя для удаления.")
            continue

        if key in phone_book_dict:
            del phone_book_dict[key]
            print(f'Контакт по имени "{key}" был успешно удален')

            # Сохраняем изменения в файл
            with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="w",
                      encoding="utf-8") as write_file:
                json.dump(phone_book_dict, write_file, ensure_ascii=False, indent=4)
        else:
            print(f'Ошибка: контакта с именем {key} не существует')
            print('Список контактов:', list(phone_book_dict.keys()))

    elif command == 'list':  # list: список всех имен в книге
        print('Полный список имен в книге:', list(phone_book_dict.keys()))

    elif command == 'show':  # show <name>: показать информацию по контакту
        if key is None:
            print("Ошибка: не указано имя для показа.")
            continue

        if key in phone_book_dict:
            print(f'Детальная информация по пользователю "{key}" - {phone_book_dict[key]}')
        else:
            print(f'Ошибка: пользователя с именем {key} не существует')

    else:
        print(
            f'Ошибка: команда "{command}" не распознана. Попробуйте ввести одну из следующих команд: (show, list, delete, add, stats)')


####################### 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику. ##############################
#################################################################################################################################################################
#################################################################################################################################################################


import json
# from datetime import datetime
#
# # Определение декоратора
# def my_decorator(func):
#     def deco_func(*args, **kwargs):
#         func_result = func(*args, **kwargs)  # Выполняем функцию и сохраняем результат
#         print(f'Это название вызванной функции: "{func.__name__}", '
#               f'дата и время вызова: {datetime.now()}, '
#               f'результат: {func_result}')
#         # name = func.__name__
#         # date = datetime.now()
#         # result = func_result
#         with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles\FuncLogs.txt", 'a', encoding='utf-8-sig') as write_file:
#             write_file.write(f"Название функции: {func.__name__}, Дата и время: {datetime.now()}, Результат: {func_result}\n")
#         return func_result  # Возвращаем результат функции, если требуется
#     return deco_func
#
# # Применение декоратора
# @my_decorator
# def my_func():
#     return 2 * 23
#
# # Вызов функции
# my_func()


#############################  В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл. #################################

# class MyCustomException(Exception):  # Классы принято писать с большой буквы
#     pass  # Используем pass, чтобы не делать лишнего
#
# try:
#     raise MyCustomException('Custom exception is occured')
# except MyCustomException as MyError:
#     # Открываем файл и записываем в него информацию об ошибке
#     with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles\ErrorLogs.txt", 'a', encoding='utf-8-sig') as write_file:
#         write_file.write(str(MyError) + '\n')  # Исправлено, добавляем символ новой строки
#
#     print(MyError)  # Печатаем ошибку на консоль


with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\WorkWithFiles\ErrorLogs.txt", 'r', encoding='utf-8-sig') as read_file:
         readed_file = read_file.read()