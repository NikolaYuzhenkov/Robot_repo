# class Tiger():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def roar(self):
#         print("Raaaaar!!!")
#
#     def attack(self):
#         print("Minus one hit")
#
#     def show(self):
#         return (f"Tiger characteristic: Tiger Name: {self.name}, Tiger age: {self.age}")
#
# NikolaTiger = Tiger("Nikola", 23)
#
# SegoTiger = Tiger("Sergo", 45)
#
# b = NikolaTiger.show()
# print(b)

class Gun:
    def __init__(self):  # Конструктор
        self.reload()  # Вызываем метод "перезарядить"
        print(self.ammo_count)

    def fire(self):  # Метод "стрелять"
        if self.ammo_count > 0:
            self.ammo_count -= 1  # Расходуем боеприпас
            print(f"Bang! Ammo left: {self.ammo_count}")
        else:
            print("No ammo left! Reload needed.")

    def reload(self):  # Метод "перезарядить"
        self.ammo_count = 10  # Забиваем магазин боеприпасами
        print("Reloaded to 10 ammo.")

# Создаем объект пушки
plazma_gun = Gun()

# Пример использования
plazma_gun.fire()  # Bang! Ammo left: 9
plazma_gun.fire()  # Bang! Ammo


