# Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана. Декоратор має працювати для різних функцій однаково.
#
# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
#
# Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
#
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.
#
# Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту із попереднього завдання.



################ Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана. Декоратор має працювати для різних функцій однаково. #################


# from datetime import datetime
# def my_decorator(func):
#     def deco_func(*args, **kwargs):
#         print(f'Это название вызванной функции: "{func.__name__}"')
#         print(f'Это дата и время вызванной функции: {datetime.now()}')
#         func(*args, **kwargs)
#     return deco_func
#
# @my_decorator
# def my_func():
#     print('This is my_func')
#
# @my_decorator
# def my_sec_func(number):
#     print(f'Результатом функции будет данное число:', number * number)
#
# my_func()
# my_sec_func(5)


############ Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured". #############

# class MyCustomException(Exception):  # КЛАСИ ПРИЙНЯТО ПИСАТИ З ВЕЛИКОЇ БУКВИ
#     True
#     #print('Custom exception is occured') # ОЗНАЧАЄ НІЧОГО БІЛЬШЕ НЕ РОБИТИ
#
# try:
#     raise MyCustomException('Custom exception is occured')
# except MyCustomException as e:
#     print(e)


# class MyCustomException(Exception):
#     def __init__(self, message="Custom exception is occured"):
#         self.message = message
#         super().__init__(self.message)
#
#
# try:
#     raise MyCustomException()
# except MyCustomException as e:
#     print(e)


# Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.
#
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.


# def my_func():
#     print('this is My super code')
#
# class CtxManager:
#     def __enter__(self):
#         print('=' * 10)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('=' * 10)
#
#
#
#
# with CtxManager(my_func()) as some_value:

# def fibo(a):
#     f1 = f2 = 1
#     #a = int(input())
#     for _ in range(a - 1):
#         next_sum = f1 + f2
#         f1 = f2
#         f2 = next_sum
#         print(f2)
#
# fibo(5)
# class MyContextManager:
#     def __enter__(self):
#         # Виконується перед виконанням коду в контексті
#         print("=" * 10)
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         # Виконується після виконання коду або при виникненні винятку
#         if exc_type is not None:
#             print(f"Error occurred: {exc_value}")
#         print("=" * 10)
#         # Повертаємо True, щоб придушити виняток і не завершити програму
#         return True
#
# # Приклад використання
# with MyContextManager():
#     print("Це код, який виконується в контексті.")
#     print(fibo(10))
#     # Спровокуємо виняток
#     #1 / 0
#
# print("Програма продовжує працювати після контекстного менеджера.")



# Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту із попереднього завдання.

# try:
#     # Частина коду, яка відповідає методу __enter__
#     print("=" * 10)
#
#     # Основний код
#     print("Це код, який виконується в try блоці.")
#     print(fibo(10))  # Викликаємо функцію, яка не існує і викликає помилку
#
# except Exception as e:
#     # Обробка помилок, аналогічно методу __exit__
#     print(f"Error occurred: {e}")
#
# else:
#     # Виконується, якщо не було винятків
#     print("Код виконався успішно без помилок.")
#
# finally:
#     # Частина коду, яка відповідає завершенню менеджера контексту (як у __exit__)
#     print("=" * 10)
