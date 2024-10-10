#################### РЕЖИМИ РОБОТИ З ФАЙЛАМИ ######################

# Для відкриття файлу використовуємо функцію OPEN() функція має певні режими у якому цей файл необхідно відкрити.
#
# r - відкрити файл для читання (Використовується за замовчуванням)
# w - переписати файл
# x - створити новий файл і відкрити його для запису (відкиття вже існуючого викличе помилку)
# a - відкрити  файл для додвання запису в кінець
# b - бінарний режим
# t - режим тексту (використовується за замовчуванням)
# + - відкрити файл для читання тексту та запису
#
# Режими можна комбінувати

# Також функція прйимає й інщі параметри:
#
# --> buffering
# --> encoding
# --> errors
# --> newline
# --> closefd
# --> opener

# help(open)

# DEFAULT FILE READING

# file = open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json")
# print(file.read())
# file.close()

# file = open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", 'r')

# file = open(r"C:\Users\Nikola\Robot_repo\pythonProject\12\PhoneBookData.json", 'r+')
# file_content = file.read()
# file_content = "I love Python" + file_content
# file.write(file_content)


# FILE NOT FOUND