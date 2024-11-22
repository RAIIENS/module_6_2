# Создаём класс Vehicle со своими атрибутами, в данном случае с допустимыми цветами.
class Vehicle:
# Допустимые цвета
    __COLOR_VARIANTS = ['blue', 'yellow','red', 'green', 'black', 'white']
# Прописываем атрибуты объекта Vehicle.
    def __init__(self, owner, model, color, engine_power):
# Владелец
        self.owner = owner
# Модель (скрытый атрибут)
        self.__model = model
# Мощность двигателя (скрытый атрибут)
        self.__engine_power = engine_power
# Цвет (скрытый атрибут)
        self.__color = color

# Прописываем методы.

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

# Выводим начальную информацию об объекте Vehicle.

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

# Выводим информацию о возможности смены цвета у объекта Vehicle. Если цвет попадает в список
# допустимых цветов то можно, если нет, то нет.

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Создаем класс Sedan являющийся наследником class Vehicle со своими атрибутами.

class Sedan(Vehicle):

# Лимит пассажиров для седана
    __PASSENGERS_LIMIT = 5

# Инициализация родительского класса
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

# Наш пример использования классов в этой задаче.
vehicle1 = Sedan('Vova', 'Toyota camry', 'yellow', 300)

# Смотрим, какие свойства у объекта были в начале.
vehicle1.print_info()

# Пробуем поменять цвет.
vehicle1.set_color('Pink')
# Нельзя сменить цвет с yellow на Pink так как его нет в списке разрешенных цветов для покраски автомобиля.
vehicle1.set_color('BLACK')
# В этот цвет перекрасить автомобиль можно.
vehicle1.owner = 'Piter'
# Изменение владельца возможно.

# Смотрим, что поменялось
vehicle1.print_info()
# Поменялся цвет автомобиля с желтого на черный,
# и поменялся владелец с Vova на Piter/