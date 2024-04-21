# =================== while loop ====================== #

# x = 1
#
# while x < 10:
#     print(x) # будуть виведені числа від одного до 10 і 10 буде із дописом FINAL RESULT
#     x += 1
#
# print(f'FINAL RESULT {x}')

# x = 100
#
# while x > 0:
#     if x % 5 == 0: # ищем числа, которые без остатка делятся на 2
#         print(x)
#     x -= 1 # цикл всегда нужно заканчивать условием false - поскольку если цслвие всегда будет тру, то цикл станет нескончаемый


# =========== for ... in ..., list example ========= #

# lst = [1, 2, 3] # type list
#
# for item in lst:
#     print(item)
#     item = 100 # кожен раз перезаписуємо зміну
#     print(item)

# lst = [1, 2, 3, 4, 5, 6]
#
# for item in lst:
#     if item % 2 == 0:
#         print(item)

# =========== for ... in ..., list example with input ========= #

# text = input('Enter text here: ')
#
# words = text.split()
#
# print(words)
#
# for word in words:
#     print(word)

# text = input('Enter text here: ') # Якщо хочемо порахувати слова в тексті - правильний варіант
#
# words = text.split()
# print(len(words))

# ============ ignore value ============ #

# text = input('Enter text here: ')
#
# words = text.split()
#
# x = 0
#
# for _ in words:
#     x += 1
#
# print(f'Words count is: {x}')


# ============= for ... in ... str example =========== #

# word = input('Entee your text here: ')
#
# for letter in word: # count each symbol
#     print(letter)
#
#
# word = input('Entee your text here: ')
#
# for letter in word:
#     if letter.isdigit():
#         print('This is a digit')
#     elif letter.isalnum():
#         print('This is alnum')
#     else:
#         print('Else')

# ============= for ... in ... + range example =========== #

# for i in range(10):
#     print(i)
#
# number = 5
#
# for i in range(number):
#     print(i)

# for i in range(10, 15): # діапазон
#     print(i)

# for i in range(1, 100, 10): # почали з 1 і кожну ітерацію до нашого значення додається 10 - STEP
#     print(i)


# =================== continue =================== #

# if i % 2 == 0: continue:
# # Умова if перевіряє, чи є поточне значення i парним. Якщо так, то виконується оператор continue,
# # який призводить до переходу до наступної ітерації циклу без виконання наступних рядків коду.
#
# for i in range(10):
#     print('The start of it')
#     if i % 2 == 0:
#         continue
#     print(i)
#     print(f'This is an iteration')

# x = 5
#
# while x > 0:
#     print('Start of iteration') # після першого циклу ітерації, значення x стало - 4, далі пішов другий цикл із значенням вже 4
#     if x % 5 == 0:
#         print('X can be divided by 5')
#     elif x % 2 == 0: # у другому циклі ітерації ми перевіряли чи х є парним, оскільки нащше число є парним, то ми віднімаємо 1
#         x -= 1
#         continue  # якщо блок коду elif виконується, то цикл продовжується
#     print(f'The value of x is {x}')
#     x -= 1 # якщо у блоці elif потрапило число не парне, то виконуєтьс частина цього коду.


# =================== break =================== #

# for i in range(10):
#     if i == 7:
#         break
#     print(f'The value of i is {i}')
#
# print('Text after break')

# x = 5
# while x > 0:
#     if x == 2:
#         break
#     else:
#         print(f'The value of x is {x}')
#         x -= 1

# ===================== infinite loops ======================= #

# while True:
#     print('Infinite loop')

while True:
    command = input('Enter a command: ')
    if command == 'weather':
        print('Sun is shining')
    elif command == 'exit':
        break
    else:
        print('Try to type "weather" or "exit"')
        continue
