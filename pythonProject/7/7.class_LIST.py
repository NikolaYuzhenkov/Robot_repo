############### LIST #######################
# lst = []
# new_lst = list() - функція list яка може трансформувати дані
# lst_with_data = ["test", 1234, lst] - запис різних типів даних в списов (int, str, lst, etc.)
# new_lst_with_data = list([1, 2, 3])
#
# ------Операції з LIST:------
# -> Створення
# -> Додавання елементів: .append, .extend
# -> Видалення елементів: .remove, .del
# -> Зєднання двух листів в один: lst1 + lst2
# -> Ітерування по елементах list за допомгою for

##########CREATE LIST################

# my_emty_list = []
# my_sec_emprty_list = list()


##############CREATE LIST FROM STR########################

# my_name = "Nikola"
# my_name_list = list(my_name)
# # print(my_name_list)
#
# some_text = "This is a simple text"
# splited = some_text.split("i")  # slpit - за замовчуванням ділить текст по пробілам
# #але можна задати в якості аргумента певне значення
# print(splited)

##############LIST WITH DIFF TYPE OF DATA###############

# lst = ['String', 1223, True, 1.23, 1.23, 1.23, 1.23]
# print(lst)

####################LIST IN LIST#################

# new_list = ['New list', lst, 2344, 2.45, '23dfg']
# print(new_list)

############## ЗВЕРНЕННЯ ДО СИМВОЛІВ ЗА ІНДЕКСОМ ####################
#print(new_list[0]) # - перший елемент - 0, останній - це -1

###############    СРІЗ      ###################
# print(new_list[2:4]) # Определяем с какого єлемента по какой берем
# print(new_list[1:]) # Беремо з першого списку й по останній
# print(new_list[:2]) # Беремо з 0 по 2

################## ШАГ ##########################

# print(new_list[::2]) #мы берем всю строку, то есть от начала (за это отвечает первое двоеточие)
# до конца(второе доветочие) и третьим параметром  передаем с каким шагом нужно брать следующую букву.
# В данном случае шаг равен двум, но у нас не страка а спиок, так что мы будем брать каждый второй элимент

################ INDEX METHOD #############
#print(new_list.index(2.45)) # Допомогає знайти INDEX елемента

################# ПОШУК ІНДЕКСА ЧЕРЕЗ FOR IN ##################

# for item in new_list:
#     if type(item) == list and 1.23 in item:
#         print(item.index(1.23))

################ ЗАМІНА ЕЛЕМЕНТУ У СПИСКУ ЗА ІНДЕКСОМ ################

# new_list[0] = 10
# print(new_list)

################### LIST APPEND ####################

# APPEND - може прийняти лише один обджект
# small_list = [1]
# small_list.append(1)
# print(small_list)
#
# small_list.append([1])
# print(small_list)
#
# small_list[2].append(2)
# print(small_list)

######################## EXTENDED #########################

# big_list = [1, 1, 1]
# other_list = [2, 2, 2]
#
# big_list.extend(other_list)
# print(big_list)

################## MERGE #################

# big_list = [1, 1, 1]
# other_list = [2, 2, 2]
# print(big_list + other_list)

######################## ITERATION #####################

# my_numbers = [1, 2, 3, 4, 5]
# for item in my_numbers:
#     print(item)
#     print(my_numbers.index(item))

#################### INDEXES AND SLICES ::: #######################3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
#
# print(numbers[0:-2]) #OR print(numbers[0:9])

# print(new_list[::2]) #мы берем всю строку, то есть от начала (за это отвечает первое двоеточие)
# до конца(второе доветочие) и третьим параметром  передаем с каким шагом нужно брать следующую букву.
# В данном случае шаг равен двум, но у нас не страка а спиок, так что мы будем брать каждый второй элимент
#print(numbers[0:9:3])

# print(numbers[3::2]) # починаємо з третього елементу та беремо шаг 2
# print(numbers[:5:2]) # починаємо з 0 елементу та беремо шаг 2 й йдемо до 5 елементу

# print(numbers[::-1]) # зворотній порядок
#print(numbers[-1:-5:-1]) # зворотній порядок із вказуванням діапозону
# print(numbers[-3::-1]) # зворотній порядок лише із зазначенням початку
# print(numbers[:-7:-1]) # зворотній порядок лише із зазначенням кінця

################# IN LIST #######################

my_list = ['apple', 'banana', True, False, 1.234]
print('apple' in my_list)

if "apple" in my_list:
    print(my_list.index('apple'))
else:
    print('Mot in list')