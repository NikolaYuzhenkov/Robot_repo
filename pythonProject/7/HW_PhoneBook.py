# 1. Створити телефонну книгу, яка матиме наступні команди:
#
# stats: кількість записів
#
# add: додати запис
#
# delete <name>: видалити запис за іменем (ключем)
#
# list: список всіх імен в книзі
#
# show <name>: детальна інформація по імені
#
# Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново.

# phone_books = {
#     'Alex': '+380671791741',
#     'Shmaks': '+380966364384',
#     'Beseda': '+1823474832'
# }
#
# while True:
#     user_input = input('Enter your command: ')
#     splited_input = user_input.split() # Перетворюємо у список
#
#     command = splited_input[0] # Визначаємо індекси для команд
#     key = splited_input[1]
#

phone_book_dict = {
    'Nikola': +3806717234,
    'Alex': +3806717234,
    'Sexa': +3806717234,
}

while True:
    try:
        command_input = input('Введите вашу команду: ')
        splited_input = command_input.split()
        command = splited_input[0]

        # Проверяем наличие второго аргумента (например, имени)
        if len(splited_input) > 1:
            key = splited_input[1]
        else:
            key = None

    except IndexError:
        print("Ошибка: неверный ввод команды. Попробуйте еще раз.")
        continue


    if command.lower() == 'stats': # stats: количество записей
        print('Количество записей в словаре равно:', len(phone_book_dict))


    elif command.lower() == 'add': # add: добавить запись
        if key is None:
            print("Ошибка: не указано имя для добавления.")
            continue
        elif key in phone_book_dict:
            print(f"Контакт с именем {key} уже существует.")
        else:
            try:
                phone_number = input(f"Введите номер для {key}: ")
                if phone_number.isdigit():
                    phone_book_dict[key] = phone_number
                    print(f"Контакт {key} с номером {phone_number} добавлен.")
                else:
                    print('Номер можеть содержать только числа')
            except ValueError:
                print("Ошибка: неверный формат номера.")

    elif command.lower() == 'delete': # delete <name>: видалити запис за іменем (ключем)
         try:
            if key is None:
                print("Ошибка: не указано имя для удаления.")
                continue
            del phone_book_dict[key]
            print(f'Контакт по имени "{key}" был успешно удален')
         except KeyError:
             print(f'Ошибка: контакта с именем {key} не существует')
             print('Выберете имя из представленого списка', phone_book_dict)

    elif command.lower() == 'list': # list: список всіх імен в книзі
        print('Полный список имен в книге:', list(phone_book_dict))

    elif command.lower() == 'show':
            if key is None:
                print("Ошибка: не указано имя для удаления.")
                continue
            elif phone_book_dict.get(key) == None:
                print(f'Ошибка: пользователя с именем {key} не существует')
            else:
                print(f'Детальная инфомрация по пользователю "{key}" - {phone_book_dict.get(key)}')

    else:
        print(f'Ошибка: комманда "{command}" не расспознана, попробуйте ввести одну из слдующих комманд: (show, list, delete, add, stats) ')










