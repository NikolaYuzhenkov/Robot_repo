#1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
variable = 42 * "I love Python"
print(variable)
print("I love Python" * 42)
#2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.

age_in_month = 24 * 12
print(age_in_month)

#3. Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
#Підказка: використовуючи арифметичні оператори та/або приведення типів).

age_in_years = age_in_month // 12
print (str(age_in_years))
print (type(age_in_years))
#4. Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”, де на замість пропусків буде підставлятись ваші імʼя та вік. Значення віку слід брати зі змінної age_in_years.

my_age = 'My name is Nikola Im ' + str(age_in_years) + ' years old'
print(my_age)

#5. Створити змінну зі значенням 1. Використовуючи оператори порівняння, порівняти її із будь-якими іншими значеннями (мінімум 5 порівнянь) і перевірити вивід в інтерпретаторі.

x = 1
print(x == 1)   # Проверяем, равно ли значение переменной 1
print(x != 2)   # Проверяем, не равно ли значение переменной 2
print(x > 0)    # Проверяем, больше ли значение переменной 0
print(x < 5)    # Проверяем, меньше ли значение переменной 5
print(x >= -1)  # Проверяем, больше или равно ли значение переменной -1

#6. Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d, значення якої має бути “256”

a = 2
b = 5
c = 6
d = str(a) + str(b) + str(c)
print (d)

a1 = '2'
b2 = '5'
c3 = '6'
d4 = a1 + b2 + c3
print (d4)


#Формат здачі: прикріпити посилання на файли/папку у своєму репозиторії GitHub із виконаним домашнім завданням в LMS до даного уроку.