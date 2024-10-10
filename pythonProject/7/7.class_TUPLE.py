# Кортежі (tuple)
#
# Tuple це колекція, яка дозволяє зберігати безліч значень різних типів в одній змінній, проте ці дані не можуть бути змінені.
# Для того, щоб створити tuple, використовують:
# --> круглі дужки ()
# --> вбудовану функцію tuple()
#
#
# > tuple = (1, 2, 3)
# > new_tuple = tuple([1, 2, 3]) # перетворення list на tuple

######### TUPLE (IMMUTABLE) #############

############### CREATE TUPLE ###############
# tuple_data = (1, 2, 3, 4, 'TST', None, True)
# print(type(tuple_data))
# print(tuple_data)
#
# empty_tuple = () # emty tuple
# second_emty_tuple = tuple()
# print(empty_tuple, second_emty_tuple)

############## TUPLE AS FUNCTION RESULT ##################

# def tuple_function():
#     return 1, 2 # по дефолту повертаються декілька значень як Tuple
#
# result = tuple_function()
# print(result)
# lst = list(result) # перетворюємо в список
# print(lst)

# we cant use .append or etc.


############# MODIFY TUPLE #################

# def tuple_function():
#     return 1, 2
#
# result = tuple_function()
# print(result[0])
# # уся ця фігня зроблена для того щоб просто додати до тюплу який незмінюванний, ще один допис, аргуемнт, оюбєкт
# list_tuple = list(result)
# list_tuple.append(3)
# result = tuple(list_tuple)
# print(result)

tpl = (1, 2, 3, 4, 5)  # tuple is itterable object

# for item in tpl:
#     print(item)

print(len(tpl))

##### built in methods tpl.index() and tpl.count()#####

print(tpl.index(1)) # ШУКАЄМО САМЕ ЗА ЗНАЧЕННЯМ ЗНАЧЕННЯ 1 ЗНАХОДИТЬСЯ ЗА ІНДЕКСОМ НУЛЬ
print(tpl.count(1)) # ПІДРАХОВУЄ КІЛКІСТЬ АРГУМЕНТІВ ПЕРЕДАНИХ ДО ФУНКЦІЇ, У НАШОМУ ВИПАДКУ ЛИШЕ ОДНА ОДИНИЦЯ

#################  #################