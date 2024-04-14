# ====function, classes, loops and comditions identation ==== #

#def test(): # блок коду
#    print('hello')
#     while True:
#        print('Goodbye') # блок коду
#        if True:
#            print('True') # блок коду
#            if True:
#                print('True')


#class TestClass:
#    def test_class(self):
#        print('test')


# ========== comments ============ #

#def test(): # блок коду
'''
Таким чином надають олписання для функцій
'''
#    print('hello')
#     while True:
#        print('Goodbye') # блок коду
#        if True:
        # also we can use comment here!
#            print('True') # блок коду
#            if True:
#                print('True')
#TODO: add some logic here (пишемо плани на майбутнє))
# екранування  - "\" після символу - це екранування print('I'\m a developer too')


# ========= conditions ========== #
#---------------------------------------------------
# x = 1
# if x > 0:
#     print('X is greater then 0')
# else:
#     print('X is not greater than 0')
#---------------------------------------------------
# age = 42
#
# if age < 18: # умови викон.ться зверху до низу
#     print('You are not allowed to see this')
# elif age >= 60:
#     print('You are too old for that')
# elif age > 100: # умови які передують й покривають цей пункт перевірки як от "age > 60" - в цю умову входить й 100 й більше 100, тому для виконання умови, такі розділи можна пересунути до гори перед іншою умовою
#     print('wow')
# elif age == 42: # ця умова буде виконуватись й так
#     print('you know answers')
# else:
#     print('You are allowed to see that, you are from 18 to 59 years')
#---------------------------------------------------
# var = 1 # всегда true
# var1 = 0 # - это всегда false
# var2 =  'text' # якщо текст є - це true
# var3 = '' # якщол тексту немає - false
# print(bool(var))
# print(bool(var1))
#
# if var:
#     print('var is here')
# else:
#     print('There is no var')
#
#     if var1:
#         print('var is here')
#     else:
#         print('There is no var')
#--------------------------------------------------
# def func():
#     return True
# # функція повертає True
# if func():
#     print('Func is true')
# else:
#     print('Func si false')
#
# number = 5
# def is_even(number): # Визначається функція is_even, яка має один параметр number.
# # функція визначає це є парним числом чи не парним
#     return number % 2 == 0 # В тілі функції використовується оператор % для перевірки, чи є залишок від ділення number на 2 дорівнює 0. Це означає, що число парне, якщо залишок дорівнює 0, і непарне, якщо не дорівнює.
# if is_even(number): # Використовується умовний оператор if-else для визначення, чи є результат функції True (парне число) чи False (непарне число).
#     print(str(number) + ' is even')
# else:
#     print(str(number) + ' is odd')

# ================ build in function ================= #

# int() # натисеувши CTRL можна перейти до перегляду документації
# str()
# print() #def print(self, *args, sep=' ', end='\n', file=None): # known special case of print - taken from CTRL + click
# list()
# help() - Отримання допомоги, тобто довідник
# help(str)
# type()
# text = 'Text  '
# print(len(text)) # функція визначає кілкість симолів у контейнері
#
# # можна також записати результат функції у змінну й використовувати її при умововних конструкціях:
# len_of_text = len(text)
# if len_of_text > 5:
#     print('Test contains more than 5 symbols')
# else:
#     print('Text contains less than 5 symbols')
#-----------------------------------------------------
# Для перевірки кількості слів у тексті можемо використовувати:

# long_text = 'This is very large text'
# splitted_text = long_text.split(' ') # для перегляду можливих функцій ми пишемо нащу змінну й IDE автоматично демонструє доступні вбудовані функції.
# print(splitted_text) # за допомогою методу "split" ми порахували кількість пробілів у тексті й записали до змінної у вигляді списку - ['This', 'is', 'very', 'large', 'text']
# len_of_the_text = len(splitted_text) # за допомогою вбуд функції ми визначили довжину або кілкість обєктів у списку, у нашому випадку.
# print(len_of_the_text) # надрукували кількість слів

#------------------------------------------------------
# How to count number of words in text in one row

# long_text = 'This is very large text dfsg sdfsd sfsdfs d sfsdf'
# print(len(long_text.split(' ')))
#
# # ========================= string formating  =========================== #
# #Є декілька варіантів форматування тексту при роботі з print: 1) Конкатинація 2) f-string (форматні строки)
# x = "My name is"
# y = " Nikola"
# print(x + y) # конкатинація
#
# x1 = "My name is" #f-string (форматні строки)
# y2 = "Nikola"
# print(f'{x1} {y2}')
# # ------------------------------------------------------------------------------
# v = 1
# f_string = f'Th{v}is  is a text' #таким чином ми можемо імпллементувати змінні у текст
# print(f_string) # Result - "Th1is  is a text"
#
# # ======================= input ======================== #
# print('code before input')
#
# age = input('Enter your age:') # до моменту інпуту виконуваний код зупиняється до моменту введення (ПО дефолту - тип данних після введення - числовий)
#
# if age.isdigit(): #вбудована функція, яка повертає True, якщо введенний тип даних - це числовий тип
#     age = int(age) # якщо умова виконається, то age перетвориться на int, а якщо ні, то age так і залишиться текстом
#
# print(f'Your age is: {age}')
#
# print('code after input')
#
# print(type(age))


# ====================== print ============================== #

print('1', '2', '3', '4', '5') # надрукуються через пробіл
print('1', '2', '3', sep='~') # через "sep" визначає яким чином будуть розділятися
print('1', '2', '3', sep='\n') # у такому випадку кожен текст буде починатся із нової строки
print('1', '2', '3', end=' The end\n') # перенос строки на новий рядок