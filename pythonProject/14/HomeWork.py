# 1. До завдання, в якому ви реалізовували телефонну книгу, додати валідацію номера телефону за допомогою RegEx.
# Врахувати можливість декількох форматів: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX

# import json
# import re
# # Инициализируем словарь для телефонной книги
# phone_book_dict = {}
#
# # Загружаем данные из файла при старте программы
# try:
#     with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="r",
#               encoding="utf-8") as read_file:
#         phone_book_dict = json.load(read_file)
# except FileNotFoundError:
#     print("Файл не найден, создана новая книга.")
# except json.JSONDecodeError:
#     print("Ошибка чтения файла, создана пустая телефонная книга.")
#     phone_book_dict = {}
#
# while True:
#     try:
#         command_input = input('Введите вашу команду: ')
#         splited_input = command_input.split()
#         command = splited_input[0].lower()
#
#         # Проверяем наличие второго аргумента (например, имени)
#         if len(splited_input) > 1:
#             key = splited_input[1]
#         else:
#             key = None
#
#     except IndexError:
#         print("Ошибка: неверный ввод команды. Попробуйте еще раз.")
#         continue
#
#     if command == 'stats':  # stats: количество записей
#         print('Количество записей в словаре равно:', len(phone_book_dict))
#
#     elif command == 'add':  # add: добавить запись
#         if key is None:
#             print("Ошибка: не указано имя для добавления.")
#             continue
#
#         if key in phone_book_dict:
#             print(f"Контакт с именем {key} уже существует.")
#         else:
#             phone_number = input(f"Введите номер телефона для {key}: ")
#             # phone_validation = re.match(r'\+380[\d]+|380[\d]+|0[\d]+', phone_number)
#
#             if (len(phone_number) >= 9 and len(phone_number) <= 14):
#                 if re.match(r'\+380[\d]+|380[\d]+|0[\d]+', phone_number):
#                     phone_book_dict[key] = phone_number
#                     print(f"Контакт {key} с номером {phone_number} добавлен.")
#                     with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="w",
#                               encoding="utf-8") as write_file:
#                         json.dump(phone_book_dict, write_file, ensure_ascii=False, indent=4)
#                 else:
#                     print('Неверный формат номера, комманда "add" принимает следющие доступные форматы: "+380", "380", "0(код оператора)"')
#             else:
#                 print("Телефон должен содержать от 9 до 14 цифр")
#
#
#     elif command == 'delete':  # delete <name>: удалить запись
#         if key is None:
#             print("Ошибка: не указано имя для удаления.")
#             continue
#
#         if key in phone_book_dict:
#             del phone_book_dict[key]
#             print(f'Контакт по имени "{key}" был успешно удален')
#
#             # Сохраняем изменения в файл
#             with open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", mode="w",
#                       encoding="utf-8") as write_file:
#                 json.dump(phone_book_dict, write_file, ensure_ascii=False, indent=4)
#         else:
#             print(f'Ошибка: контакта с именем {key} не существует')
#             print('Список контактов:', list(phone_book_dict.keys()))
#
#     elif command == 'list':  # list: список всех имен в книге
#         print('Полный список имен в книге:', list(phone_book_dict.keys()))
#
#     elif command == 'show':  # show <name>: показать информацию по контакту
#         if key is None:
#             print("Ошибка: не указано имя для показа.")
#             continue
#
#         if key in phone_book_dict:
#             print(f'Детальная информация по пользователю "{key}" - {phone_book_dict[key]}')
#         else:
#             print(f'Ошибка: пользователя с именем {key} не существует')
#
#     else:
#         print(
#             f'Ошибка: команда "{command}" не распознана. Попробуйте ввести одну из следующих команд: (show, list, delete, add, stats)')



#####################################################Варианты реализации кода первого задания ##############################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################

############################################### ВАРИАНТ ПЕРВЫЙ ЗАПИСЬ ПАТТЕРНОВ В ПЕРМЕННЫЕ #####################################
# while True:
#     phone_number = input('Enter here: ')
#     pattern1 = r'^0\d{9}$'
#     pattern2 = r'^\+380\d{9}$'
#     pattern3 = r'^380\d{9}$'
#
#     if re.match(pattern1, phone_number) or re.match(pattern2, phone_number) or re.match(pattern3, phone_number):
#         print('Введен верный формат')
#     else:
#         print("Wrong number")
############################################### ВАРИАНТ ВТОРОЙ ЗАПИСЬ ПАТТЕРНОВ на прямую в условній опретор #####################################

# while True:
#     phone_number = input('Enter here: ')
#
#     if re.match(r'^0\d{9}$', phone_number) or re.match(r'^\+380\d{9}$', phone_number) or re.match(r'^380\d{9}$', phone_number):
#         print('Введен верный формат')
#     else:
#         print("Wrong number")

############################################## ВАРИАНТ ТРЕТИЙ УСПОЛЬЗУЯ УСЛОВИЯ С ОДНОЙ СТРОКОЙ РЕГ ВЫРАЖЕНИЙ #################################################################3

# while True:
#     phone_number = input('Enter here: ')
#
#     if re.match(r'^(0\d{9}|\+380\d{9}|380\d{9})$', phone_number):
#         print('Введен верный формат')
#     else:
#         print("Wrong number")

############################################## ВАРИАНТ ЧЕТВЕРТЫЙ УСПОЛЬЗУЯ РЕГ ВЫРАЖЕНИЯ БЕЗ ВАЛИДАЦИИ ДЛИНЫ СТРОКИ  ###########################################

#     if (len(phone_number) >= 9 and len(phone_number) <= 14):
#         if re.match(r'\+380[\d]+|380[\d]+|0[\d]+', phone_number):

#####################################################################################################################################

########################################################################################################################################

# 2. (необов'язкове виконання) Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на *@*.

import os
import re

# def symb_replacement(file_name):
#     with open(file_name, 'r') as readed_file:
#         file_contents = readed_file.read()
#         email_pattern = r' (.+@.+)'
#         replaced_text = re.sub(email_pattern, '*@*', file_name)

# symb_replacement(r"C:\Users\Nikola\Robot_repo\pythonProject\14\Emails.file.txt")

import re

# def symb_replacement(file_name):
#     # Открываем файл и считываем его содержимое
#     with open(file_name, 'r', encoding='utf-8') as readed_file:
#         file_contents = readed_file.read()
#
#     # Регулярное выражение для поиска email-адресов
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' #r' (.+@.+)'
#
#     # Заменяем найденные email-адреса на *@*
#     replaced_text = re.sub(email_pattern, '*@*', file_contents)
#
#     # Выводим результат
#     print(replaced_text)
#
# # Вызов функции с указанием пути к файлу
# symb_replacement(r"C:\Users\Nikola\Robot_repo\pythonProject\14\Emails.file.txt")





# 3. (необов'язкове виконання) Написати програму, яка буде:
# зчитувати текст із файлу, назва якого вводиться користувачем (program argument або input)
# знаходити всі email в тексті і змінювати їх на X***@****X, де замість Х мають бути перша і остання літери справжньої адреси,
# а весь інший текст має бути замінений на *. Кількість * необовʼязково має відповідати кількості замінених символів

import re


def mask_email(email):
    """Функція для заміни email на X***@****X"""
    name, domain = email.split('@')

    # Залишаємо першу та останню літери в локальній частині, решту замінюємо на ***
    if len(name) > 2:
        masked_name = name[0] + '***' + name[-1]
    else:
        masked_name = name  # Якщо менше 3 символів, залишаємо як є

    # Залишаємо першу та останню літери в доменній частині, решту замінюємо на ****
    domain_parts = domain.split('.')
    masked_domain_name = domain_parts[0]
    if len(masked_domain_name) > 2:
        masked_domain_name = masked_domain_name[0] + '****' + masked_domain_name[-1]
    else:
        masked_domain_name = masked_domain_name  # Якщо менше 3 символів, залишаємо як є

    masked_domain = masked_domain_name + '.' + domain_parts[1]

    return f"{masked_name}@{masked_domain}"


def process_text(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

            # Регулярний вираз для пошуку email
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

            # Знаходимо всі email у тексті
            emails = re.findall(email_pattern, text)

            # Замінюємо всі знайдені email на форматовані
            for email in emails:
                masked_email = mask_email(email)
                text = text.replace(email, masked_email)

            # Виводимо або зберігаємо змінений текст
            print("Processed Text:\n")
            print(text)

    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    # Запитуємо у користувача назву файлу
    file_name = input("Введіть назву файлу: ")
    process_text(file_name)

# def mask_email(email):
#     """Функція для заміни email на X***@****X"""
#
#
# mask_email("yuzhenkovsan@gmail.com")