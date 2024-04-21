# 1. Створити програму, яка буде очікувати від користувача введення тексту і виведе інформацію по кожному надрукованому символу:
#
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”

# text = input('Enter your text: ')
#
# for symbol in text:
#     if symbol.isdigit():
#         symbol = int(symbol)
#         if symbol % 2 == 0:
#             print(f'Це число: "{symbol}" та це число є парним;')
#         else:
#             print(f'Це число: "{symbol}" та це число не є парним;')
#     elif symbol.isupper():
#         print(f'Це буква: "{symbol}" та ця буква є великою;')
#     elif symbol.islower():
#         print(f'Це буква: "{symbol}" та ця буква є маленькою;')
#     else:
#         print(f'Це символ: "{symbol}"')


# text = input('Enter your text: ')
#
# for symbol in text:
#     if symbol.isdigit():  # Перевірка, чи символ є цифрою
#         symbol = int(symbol)  # Конвертація символу в ціле число
#         if symbol % 2 == 0:
#             print(f'Це число: "{symbol}" та це число є парним')
#         else:
#             print(f'Це число: "{symbol}" та це число не є парним')
#     elif symbol.isupper():  # Перевірка, чи символ є великою літерою
#         print(f'Це буква: "{symbol}" та ця буква є великою')
#     elif symbol.islower():  # Перевірка, чи символ є малою літерою
#         print(f'Це буква: "{symbol}" та ця буква є маленькою')
#     else:
#         print(f'Це символ: "{symbol}"')  # Якщо символ не є цифрою або літерою, він вважається символом

# 2. Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди, поки її виконання не буде перервано вручну.
#
# Підказка: для того, щоб програма могла зупинитися на вказаний час, можна використати бібліотеку time (import time), а саме функцію sleep().
# (time.sleep(second), де second, це кількість секунд, які програма має чекати).

# import time
#
# i = 'I love Python'
# while True:
#     print(i)
#     time.sleep(4.2)
#     print('Прошло 4.2 секунды')

