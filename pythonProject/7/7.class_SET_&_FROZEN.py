# Set - це колекція, яка дозволяє зберігати безліч унікальних значень різних типів в одній змінній.
# Дані в set:
# ← не впорядковані
# ← не можуть бути змінені
# ← можуть бути видалені чи додані
# Для того, щоб створити set, використовують:
# → фігурні дужки {}
# ← вбудовану функцію set()
# > my_set = {1, 2, 3}
# > new_set = set([1, 2, 3]) # перетворення list на set
# > new_unique_set = set([1, 1, 2, 2]) # {1, 2} — отримання
# унікальних даних із list

#################### ОПЕРАЦІЇ З SET ###################
# > my_set = {1, 2, 3}
# > my_set.add(4) # {1, 2, 3, 4} — додати елемент
# > my_set.remove(1) # {2, 3, 4} - видалити елемент
# > new_set = {4, 5, 6}
# > my_set & new_set # {4} - отримати тільки значення, які спільні для двох set
# > my_set | new_set # {2, 3, 4, 5, 6) — отримати всі значення, які зустрічаються в двох set
# > my_set.pop() # -> {2}, отримати перший елемент set, видаливши його із my_set
# > new_unique_set = set([1, 1, 2, 2]) # {1, 2} - отримання унікальних даних із list

############# CREATE A SET #################

# my_set = set()
# second_set = {5, 5, 5, 5, 3, 3, 3, 5, 4, 4, 2, 1, 1, 2, 2, 7} #Порядок йде від меношого числа до більшого (сортуються по значенню хеша)
# print(second_set)

#print(list(second_set)) # Таким чином отримаємо відсортований лист

# ЗВЕРНЕННЯ ЗА ІНДЕКСОМ НЕМОЖЛИВЕ - print(second_set[0])
#print(len(second_set)) # показує кількість саме унікальних елементів

################ UPDATE A SET REMOVE OR ADD #################

########## ADD ###########
# second_set.add(0)
# print(second_set)

############## REMOVE ##########3
# second_set.add(3) #додати вже існуючий елемент ми не можемо оскільки це не буде унікальним значенням
# second_set.remove(5) # Видяляє елемент
# second_set.remove(3)
# print(second_set)

############# POP() ##############3
# poped_element = second_set.pop() # видяляє самй перший елемент та записує його у будь яку зміну
# print(second_set)
# print(poped_element) # записало перший елемент у цю зміну

####################  SET | OR, UNION()  ####################
# PIPE OR UNION() ДОПОМОГАЄ ЗНАЙТИ УСІ УНІКАЛЬНІ ЕЛЕМЕНТИ ЯКІ МІСТЯТЬСЯ У ОБОХ СЕТАХ
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}
#
# print(first_set | second_set)
#
# unique = (first_set | second_set)
# print(list(unique))

####### UNION #########

# union_unique = first_set.union(second_set)
# print(union_unique)

########## SET & AND INTERSECTION() ##############

print(first_set & second_set) # Отримаємо лише ті значення що знаходяться у одній множині та у інщій
inter = first_set & second_set
print(inter)

inster_sec = first_set.intersection(second_set)
print(inster_sec)

############## SET " - " UNIQUE FOR FIRST, DIFFERENCE() ###########

# ОТРИМАЄМО ТІЛЬКИ ТІ ЗНАЧЕННЯ ЯКІ Є У ПЕРШОМУ СЕТІ ТА ЯКИХ НЕМАЄ У ДРУГОМУ СЕТІ

# print(first_set - second_set)
# print(second_set - first_set)
# print(first_set.difference(second_set))
# print(second_set.difference(first_set))

############# SET "^" - UNIQUE FOR FIRST, SYMMETRIC_DIFFERENCE() ##########
# ОТРИМАЄМО УНІКАЛЬНІ ЗНАЧЕННЯ ЯКІ НЕ ПЕРЕТИНАЮТЬСЯ, ТОБТО ЦЕ У НАС УСІ ОКРІМ 4 ТА 5

# print(first_set ^ second_set)
# print(first_set.symmetric_difference(second_set))