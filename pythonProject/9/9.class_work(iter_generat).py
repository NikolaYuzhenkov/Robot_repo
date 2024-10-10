# Ітератори
#
# Ітератор це об'єкт, по якому можна ітеруватися.
# ← Ітератори мають властивості, які дозволяють їм бути використаними в таких конструкціях Python, як for ... in
# ← Особливістю ітератора є те, що у цьому об'єкті реалізовано методи
# _iter_() та _next_(). Якщо об'єкт реалізує цей метод, він може бути ітерованим.
# ← Деякі вже знайомі нам типи даних реалізують ці методи. Це такі типи як list, tuple, string та інші.


# Для роботи з ітераторами у Python є дві вбудовані функції:
# → iter() за допомогою функції можна отримати ітератор об'єкта.
# ← next() при передачі в функцію ітератора, буде повертати по черзі кожен наступний елемент ітератора.
# >>>
# >>> string = 'test'
# >>> string_iterator iter(string)
# >>> next(string_iterator)
# 't'
# >>> next(string_iterator)
# 'e'
# >>> next(string_iterator)
# 's'
# >>> next(string_iterator)

# ← Ітератори також можна створювати за допомогою функцій, передаючи назву функції замість об('єкта-ітератора. Проте, для того, щоб був створений ітератор, '
# 'потрібно також передати в функцію iter() другий аргумент, sentinel.)
# Коли функція, яку ми передали в iter(), поверне значення, яке дорівнює sentinel, ітерацію буде завершено.
# >>> import random
# >>>
# >>> def iter_function():
# return random.randint(0,5)
# >>> iterator = iter(iter_function, 5) # stop if fuction returns 5
# >>> next(iterator)
# 4
# >>> next(iterator)
# 4
# >>> next(iterator)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# StopIteration

# Генератори це різновид ітераторів. Генератор також може бути використаний для ітерування, але при цьому, на відміну від ітератора,
# генератор повертає по одному об'єкту за 1 ітерацію, генеруючи його "на льоту", тоді як ітератор завантажує всі ітеровані об'єкти в пам'ять.
# Для реалізації такого функціоналу використовується ключове слово yield. Воно використовується так само, як return в функціях, проте,
# написавши в функції yield, вона стає генератором.
# На прикладі ви можете побачити генератор my_generator і його використання:
# >>> def my_generator(size):
#     values range(size)
#     for value in values:
#     yield value
# >>> generator = my_generator(3)
# >>> for item in generator:
# print(item)
# 0
# 1
# 2
# >>>>

# Важливо розуміти, що передаючи генератор в for in виконається код, який іде до ключового слова yield,
# але потім виконання зупиняється і продовжується тільки під час наступної ітерації. Ось декілька прикладів:
#
# Тобто генератор запам'ятовує останнє повернуте значення і стан генератора, і при наступній ітерації продовжує виконання коду,
# аж поки не закінчаться значення, що можуть бути повернуті.


############### LIVE CODING ITERATORS #################

from sys import getsizeof

################# SIMPLE ITERATOR ####################

# string = 'Im a string'
# print(next(string)) # TypeError: 'str' object is not an iterator - in function next only iterator can be sent

################ CREATE ITERATOR ################
# string_iterator = iter('Im a string')
# print(next(string_iterator)) # результатом виконання буде "I"
# print(next(string_iterator)) # результатом виконання буде "m"
# print(next(string_iterator)) # результатом виконання буде "  "
# print(next(string_iterator)) # результатом виконання буде "a"
# # etc. Ітерація продовжиться з міста де вона була зупинена
# # next(*args, **kwargs) Return the next item from the iterator.
# # iter(source, sentinel=None): Get an iterator from an object.
#
# string = 'Im a string'
# #            (iter(string)) (релізація під капотом)
# for item in string:  #next(iter(string)) (реалізація під капотом)#(значення які отримаються за допомогою некст будуть записуватся у ту змінну яка стоїть між for та in)
#     print(item)


################# ITERATION BY LISTS #######################

# my_list = [0, 1, 2, 3, 4, 5]
# print(type(my_list))
# print(next(my_list)) # TypeError: 'list' object is not an iterator

# my_list = [0, 1, 2, 3, 4, 5]
# my_list_iter = iter(my_list)
# print(type(my_list_iter))
# print(next(iter(my_list_iter)))
# print(next(iter(my_list_iter)))
# print(next(iter(my_list_iter)))

################ GENERATOR CREATION #################

def my_generator_function(size):
    value = 0
    while value < size:
        yield value
        value += 1


gen = my_generator_function(5)

print(my_generator_function)
print(gen)

for item in gen:
    print(item)

# try:
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
# except:
#     print('Iteration end')

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 22, 23124, 1241241]
#
#
# var = [item * 2 for item in lst] # list comprehension - в зміну ліст буде зроблена зaпис зі змінної item на основі минулого ліста
# print(getsizeof(var))
#
# second_var = (item * 2 for item in lst)
# print(getsizeof(second_var)) # RESULT: <generator object <genexpr> at 0x0000026E1A3636B0> - Таким чином створюється генератор



####################### НАПИСАННЯ ВЛАСНИХ ІТЕРАТОРІВ  #############################

# Для того, щоб об'єкт вважався ітератором, потрібно щоб у нього було 2 методи: _iter_() та _next_().
# ← Метод_iter_() це те, що повертається в якості об'єкта-ітератора.
# →
# Метод_next_() це те, що по суті викликається функцією next() і має повертати наступне значення ітерації.
# Приклад створення ітератора для чисел від 1 до 10:
# >>> class FromOneToTen:
# n=0# initial value, start of iteration.
# def _iter__(self):
#     return self
# def __next__(self):
#     if self.n 10: # stop iteration after 10 was returned
#     self.n += 1
#     return self.n
# else:
#     raise StopIteration()
# >>> one_to_ten_iterator FromOneToTen()
# > print(one_to_ten_iterator)
# >> <_main_.FromOneToTen object at 0x104988c40>
# >>> for item in one_to_ten_iterator:
# print(item)


# class MyIterator:
#     value = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value == 5:
#             raise StopIteration
#         tmp_value = self.value # при першій ітераціїї збережеться нуль
#         self.value += 1 # значення стане 1
#         return tmp_value
#
#
# my_iterator_object = MyIterator()
# #
# # print(next(my_iterator_object))
# # print(next(my_iterator_object))
# # print(next(my_iterator_object))
# # print(next(my_iterator_object))
# # print(next(my_iterator_object))
# # print(next(my_iterator_object))
#
# for item in my_iterator_object:
#     print(item)
#
# print('Iter is over')

####################### СТВОРЕННЯ ВЛАСНИХ ГЕНЕРАТОРІВ #########################

# Для створення генератора достатьно й будь-якій функціхх змінити return на yield.

# def my_generator():
#     stop = 10
#     value = 0
#     while value <= stop:
#         yield value
#         value += 1
#
# gener = my_generator()
# for item in gener:
#     print(item)
# #
# #
# # my_gen = (x for x in [1, 2, 3])
# # for item in my_gen:
# #     print(item)

