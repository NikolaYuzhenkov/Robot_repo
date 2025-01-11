# # print(dir(str)) # НАДРУКУВАТИ МЕТОДИ ОБЕКТУ
# # print(dir(print)) # НАДРУКУВАТИ МЕТОДИ ОБЕКТУ
#
# # class Car:
# #     # Атрибут класса
# #     wheels = 4  # Все машины имеют 4 колеса
# #
# #     # Конструктор класса (создаёт объект)
# #     def __init__(self, brand, year):
# #         # Атрибуты экземпляра (индивидуальны для каждой машины)
# #         self.brand = brand
# #         self.year = year
# #
# #     # Метод для описания действия
# #     def start_engine(self):
# #         print(f"{self.brand} engine started!")
#
# # class Rectangle:
# #     def __init__(self, a, b): # ТУТ ТАКОЖ МОЖНА ДОДАВАТИ ВАЛІДАЦІЮ
# #         self.side_a = a
# #         self.side_b = b
# #     def get_square(self):
# #         return self.side_a * self.side_b
# #     def get_perimeter(self):
# #         return (self.side_a + self.side_b) * 2
# #
# # rectangle_1 = Rectangle(23, 34)
# # print(rectangle_1.get_square())
# #
# # rectangle_2 = Rectangle(54, 667)
# # print(rectangle_2.get_square(), rectangle_2.get_perimeter() )
# #
# # not_lower_text = "SDFGDFGSDF" # def islower(self, *args, **kwargs): # real signature unknown
# # print(not_lower_text.islower())
#
# class Rectangle:
#     def __init__(self, a, b):
#         if a > 0:
#             self.side_a = a
#         else:
#             raise ValueError("side_a must be greater than zero")
#         if b > 0:
#             self.side_b = b
#         else:
#             raise ValueError("side_b must be greater than zero")
#
#     def get_square(self):
#         return self.side_a * self.side_b
#
#     def get_perimeter(self):
#         return (self.side_a + self.side_b) * 2
#
#
# # Тестуємо
# # rectangle_1 = Rectangle(0, 34)  # Це викличе ValueError
# # print(rectangle_1.get_square())
#
#
# rect_1 = Rectangle(10, 15)
# rect_2 = Rectangle(8, 16)
#
# # Сравниваем площади
# if rect_1.get_square() > rect_2.get_square():
#     print('rect 1 is bigger')
# else:
#     print('rect 2 is bigger or they are the same')
