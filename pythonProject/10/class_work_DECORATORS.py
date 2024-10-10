############### DECORATORS ###################

from time import sleep

# def my_deco(func): # PARANTS FUNCTION
#     print('parants functions (my_deco --> start)') # Спочатку викликається, а потім одрауз переходить до print('My deco end')
#     def wrap():
#         print('Start decoration')
#         func()
#         print('End of decoration')
#     print('My deco end') # відбувається одразу після (my_deco --> start)'
#     return wrap # функцію тут не виконуємо, оскільки яфкщо ми її виконаємо, то сама функція виконається одразу коли файл читається (тобто ми отримаємо резуольтат виконання
#     #а не виклик самої функціїї ) ЩЕ РАЗ, МИ ТУТ ВИКЛИКАЄМО САМУ ФУНКЦІЮ, А НЕ РЕЗУЛЬТАТ ФУНКЦІЇЇ
#
#
# @my_deco
# def my_func(): # wrap
#     print('My func')
#
# sleep(15)
# my_func()

################# SYNTAXIS WITHOUT @ ###########

# deco_func = my_deco(my_func)
# deco_func()

############################################ DECO WITH PARAMETERS #####################

# def my_deco_with_params(func):
#     def wrap():
#         func()
#     return wrap
#
# @my_deco_with_params
# def my_function(a, b, c):
#     print(a, b, c)
#
# my_function(1, 2, 3) # TypeError: my_deco_with_params.<locals>.wrap() takes 0 positional arguments but 3 were given

# def my_deco_with_params(func):
#     def wrap(wrap_a, wrap_b, wrap_c):
#         print('wrap', wrap_a, wrap_b, wrap_c)
#         func(wrap_a, wrap_b, wrap_c)
#     return wrap
#
# @my_deco_with_params
# def my_function(a, b, c):
#     print(a, b, c)
#
# my_function(1, 2, 3)

# def my_deco_with_params(func):
#     def wrap(*args, **kwargs):
#         print(f'Function {func} is called with parameters {args}')
#         func(*args, **kwargs)
#     return wrap
#
# @my_deco_with_params
# def my_function(a, b, c, name):
#     print(a, b, c, name)
#
# my_function(1, 2, 3, name='Nikola')


# def my_result_deco_func(func):
#     def wrap(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f'Deco result is {res}')
#         return res % 2 # Таким образом мы вощзвращаем рещльтат функции и модет продолжить работу над ним (Повертаємо результат цілочисельного ділення)
#     return wrap
#
# @my_result_deco_func
# def add_numbers(a, b):
#     return a + b
#
# print(add_numbers(1, 2))

#################### ВИДОЗМІН.ЄМО ВХІДНІ ПАРАМЕТРИ АБО ОБРОБЛЮЄМО ЇХ##########################
def my_result_deco_func(func):
    def wrap(*args, **kwargs):
        if 'name' in kwargs:
            print(f'Function {func} is called with name {kwargs.get("name")}')
        res = func(*args, **kwargs)
        print(f'Deco result is {res}')
        return res # Таким образом мы вощзвращаем рещльтат функции и модет продолжить работу над ним (Повертаємо результат цілочисельного ділення)
    return wrap

@my_result_deco_func
def add_numbers(a, b):
    return a + b

add_numbers(44, 45)
#
# @my_result_deco_func
# def other_function(name, phone):
#     print(name, phone)
#
#
# print(add_numbers(1, 2))
# print(other_function(name='Oleksii', phone=394930239))


############################ ПИШЕМО ДЕКОРАТОРИ ЯКІ ПРЙИМАЮТЬ САМІ ПАРАМЕТРИ #########################

# def my_decorator(name):
#     print(f'The name is {name}')
#     def wrapper(func):
#         def deco(*args, **kwargs):
#             print(args, kwargs)
#             return func(*args, **kwargs)
#         return deco
#     return wrapper
#
#
# @my_decorator(name='Oleksii')
# #ДЕТАЛЬНЕ ПОЯСНЕННЯ У НОУШЕН
# def my_func(a, b):
#     return a + b
#
# print(my_func(1, 2))
#
#
# from functools import wraps
#
# def my_wraps_decorator(name):
#     @wraps(func)
#     def deco(*args, **kwargs):
#         return func
#     return deco