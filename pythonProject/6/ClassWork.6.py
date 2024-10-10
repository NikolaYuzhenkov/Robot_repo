# ========================= VARIABLES IN FUNC ========================== #

# a = 10
#
# print(f'Before function {a}')
# def add(a, b):
#     print(f'Inside function: {a} та {b}') # в середині функції свторується своя область видимості.
#     return a + b
#
#
# result = add(100, 200) # виконали функцію та записали до змінної result
# print(f'Result is {result}')
#
# print(f'After a function {a}')

# ========================= VARIABLES IN FUNC 2 EX  ============================== #

# a = 10
# c = 42
#
# print(f'Before function {a} та {c}')
# def add(a, b):
#     print(f'Inside function: {a} {b} {c}') # в середині функції свторується своя область видимості.
#     return a + b + c # тепер у середені функції ми викликаємо змінну не з діпазону функціїї, а саме змінна С - вона стає автоматично частиною функції
#
#
# result = add(100, 200) # виконали функцію та записали до змінної result
# print(f'Result is {result}')
#
# print(f'After a function {a} {c}')

# ============================== FUNCTIONS =================================== #
def test(): # функция, которая что-то возвращает (назначаем функцию)
    return 880

def second (): # функция которая печатает (назначаем функцию)
    print('second test')

def pass_function(): # пустая функция (назначаем функцию)
    pass

# ============================== RETURN FROM A FUNCTIONS =================================== #

# test_variable = test() # передаємо функцію у змінну
# print(test_variable) # передаємо функцію у функцію print
# print(test())

# second_test_variable = second()
# third_test_variable = pass_function()
# print(second_test_variable, third_test_variable)

# ============================== CALL A FUNCTION =================================== #

# def is_even(number):
#     return number % 2 == 0
#
# if is_even(4):
#     print('This is even number')
# else:
#     print('This is not even num')

# def get_string():
#     return 'This is the string'
#
# for c in get_string():
#     print(c)

# ============================== FUNCTION ARGUMENTS: POSITIONAL, NAMED, DEFAULT, *args, **kwarks ========================== #

# def func_with_args(first, second, third=1): # ПЕРВЫЙ И ВТОРОЙ (POSITIONAL) АРГУМЕНТ ЯВЛЯЕТСЯ ОБЯЗАТЕЛЬНЫМ
#     print(f'Arguments: {first}, {second}, {third} ')
#     return 1
#
# #func_with_args(10, 20, ) # ПЕРЕДАЕМ ПАРАМЕТРЫ В ОБЯЗАТЕЛЬНЫЕ АРГУМЕНТЫ
#
# func_with_args(second=45, first=33) # можемо надвати значення змінним використовуючи їх імена. Для запобігання порядку визначеному.

# def super_func(*args, **kwargs): #args та kwargs повинні бути саме у такому порядку й врони не обовязово повинні мати такі назви
#     print(args, kwargs) # звернення без зірочок
#     for a in args:
#         print(a)
#
#     if kwargs.get('dir'):
#         print(f'dir is passed, Value is {kwargs.get("dir")}')
#     else:
#         print('dir is not passed, try again')
#
# number = 42
#
# super_func(1, number, 'Text', position='Absolute', dir='Flex')
#
# def another_func(*sup, **ksup): # вот у нас тот же кваргс и аргс, только с другим названием
#     print(sup, ksup)
#
#
# def anothe3r_func(*sup): # можем использовать аргументы аргс и кваргс отдельно друг от друга
#     print(sup)


# def super_super_func(first, second, third=3, *args, **kwargs): #(first, second = позиционные аргументы, third=3 = именнованые аргументы, args = неограниченное кол в виде масива, kwargs = неогр кол. в виде словаря )
#     print(first)
#     print(second)
#     print(third)
#     print(args)
#     print(kwargs)
#
#
# super_super_func(22, 34, 33, 22, 33, 1, kwargs=4, sdaf=3)# нельзя передавать несколько занчений для одного аргумента, как позиционный а потом к поз дать значение
#
# b = 3
# b = b * b
# b = b + b * b
# print(b)

# ---------------------------------LAMBDA-----------------------------------------

x = lambda a: a + 10
print(x(5))

# 1. **`x = lambda a: a + 10`**:
#    - `lambda a: a + 10` — это анонимная функция (или функция `lambda`), которая принимает один аргумент `a` и возвращает результат выражения `a + 10`.
#    - Эта функция присваивается переменной `x`.
#
# 2. **`print(x(5))`**:
#    - `x(5)` вызывает анонимную функцию, передавая ей аргумент `5`.
#    - Функция `lambda` выполняет вычисление `5 + 10`, что равно `15`.
#    - `print(15)` выводит `15` на экран.
#
# Итак, переменная `x` содержит анонимную функцию, которая добавляет 10 к переданному числу, а `print(x(5))` показывает результат этого вычисления.