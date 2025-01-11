import csv
import re

def format_phone_numbers(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            rows = [row for row in reader]

        formatted_numbers = []
        for row in rows:
            for number in row:
                # Удаляем пробелы, скобки, дефисы и преобразуем номер в нужный формат
                cleaned_number = re.sub(r'[\s\-()]+', '', number)
                formatted_number = cleaned_number.replace('+', '')
                if formatted_number.startswith('38'):
                    formatted_numbers.append(formatted_number)

        # Соединяем номера знаком |
        result = '|'.join(formatted_numbers)

        # Записываем результат обратно в файл
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(result)

        print(f"Форматированные номера успешно записаны в файл: {output_file}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
input_csv = 'C:\\Users\\Nikola\\Robot_repo\\pythonProject\\WorkProjects (OS, FILES, DIR, ETC)\\Внутрянка - Лист1.csv'
output_csv = 'C:\\Users\\Nikola\\Robot_repo\\pythonProject\\WorkProjects (OS, FILES, DIR, ETC)\\Внутрянка - formated.csv'

format_phone_numbers(input_csv, output_csv)

import csv
import re

# def format_phone_numbers(input_file, output_file):
#     try:
#         with open(input_file, 'r', encoding='utf-8') as infile:
#             reader = csv.reader(infile)
#             rows = [row for row in reader]
#
#         original_numbers = []
#         formatted_numbers = []
#         for row in rows:
#             for number in row:
#                 original_numbers.append(number)  # Добавляем номер из исходного файла
#                 # Удаляем пробелы, скобки, дефисы и преобразуем номер в нужный формат
#                 cleaned_number = re.sub(r'[\s\-()]+', '', number)
#                 formatted_number = cleaned_number.replace('+', '')
#                 if formatted_number.startswith('38'):
#                     formatted_numbers.append(formatted_number)
#
#         # Соединяем номера знаком |
#         result = '|'.join(formatted_numbers)
#
#         # Записываем результат обратно в файл
#         with open(output_file, 'w', encoding='utf-8') as outfile:
#             outfile.write(result)
#
#         print(f"Форматированные номера успешно записаны в файл: {output_file}")
#
#         # Считаем количество номеров в исходном файле
#         original_count_file = input_file.replace('.csv', '_original_count.txt')
#         with open(original_count_file, 'w', encoding='utf-8') as original_countfile:
#             original_countfile.write(f"Количество номеров в файлах: {len(original_numbers)}")
#
#         print(f"Количество номеров в исходном файле записано в файл: {original_count_file}")
#
#         # Считаем количество номеров в отформатированном файле
#         count_file = output_file.replace('.csv', '_count.txt')
#         with open(count_file, 'w', encoding='utf-8') as countfile:
#             countfile.write(f"Количество номеров в файлах: {len(formatted_numbers)}")
#
#         print(f"Количество номеров в отформатированном файле записано в файл: {count_file}")
#
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#
# # Пример использования
# input_csv = 'C:\\Users\\Nikola\\Robot_repo\\pythonProject\\WorkProjects (OS, FILES, DIR, ETC)\\Внутрянка - Лист1.csv'  # Имя входного файла
# output_csv = 'C:\\Users\\Nikola\\Robot_repo\\pythonProject\\WorkProjects (OS, FILES, DIR, ETC)\\New-Version'  # Имя выходного файла
# format_phone_numbers(input_csv, output_csv)

# import csv
# import re
#
# def format_and_count_phone_numbers(input_file, output_file):
#     try:
#         # Считываем номера из исходного файла
#         with open(input_file, 'r', encoding='utf-8') as infile:
#             raw_numbers = infile.readlines()
#
#         # Форматируем номера
#         formatted_numbers = []
#         for number in raw_numbers:
#             cleaned_number = re.sub(r'[\s\-()]+', '', number.strip())
#             formatted_number = cleaned_number.replace('+', '')
#             if formatted_number.startswith('38'):
#                 formatted_numbers.append(formatted_number)
#
#         # Подсчитываем количество номеров в исходном файле
#         original_count = len(raw_numbers)
#
#         # Подсчитываем количество отформатированных номеров
#         formatted_count = len(formatted_numbers)
#
#         # Записываем отформатированные номера в файл
#         with open(output_file, 'w', encoding='utf-8') as outfile:
#             outfile.write('|'.join(formatted_numbers))
#
#         # Записываем количество номеров в отдельные файлы
#         with open(output_file.replace('.csv', '_original_count.txt'), 'w', encoding='utf-8') as original_count_file:
#             original_count_file.write(f"Количество номеров в исходном файле: {original_count}\n")
#
#         with open(output_file.replace('.csv', '_formatted_count.txt'), 'w', encoding='utf-8') as formatted_count_file:
#             formatted_count_file.write(f"Количество отформатированных номеров: {formatted_count}\n")
#
#         print(f"Номера обработаны успешно.")
#         print(f"Форматированные номера записаны в файл: {output_file}")
#         print(f"Количество исходных номеров: {original_count}")
#         print(f"Количество отформатированных номеров: {formatted_count}")
#
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#
# # Пример использования
# input_csv = 'C:\\Users\\Nikola\\Robot_repo\\pythonProject\\WorkProjects (OS, FILES, DIR, ETC)\\Внутрянка - Лист1.csv'  # Имя входного файла
# output_csv = 'C:\\Users\\Nikola\\Robot_repo\\pythonProject\\WorkProjects (OS, FILES, DIR, ETC)\\New-Version'  # Имя выходного файла
# format_and_count_phone_numbers(input_csv, output_csv)
