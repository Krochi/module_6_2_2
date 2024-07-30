# Задача "Изменять нельзя получать":

# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) -
# наследник класса Vehicle.
#
# I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
# Атрибут owner(str) - владелец транспорта. (владелец может меняться)
# Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
# Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
# Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
# А так же атрибут класса:
# Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
# Каждый объект Vehicle должен содержать следующий методы:
# Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
# Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
# Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
# Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
# а так же владельца в конце в формате "Владелец: <имя>"
# Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
# если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
# "Нельзя сменить цвет на <новый цвет>".
# Взаимосвязь методов и скрытых атрибутов:
# Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
# __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
# Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').

# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

# Пункты задачи:
# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.


class Vehicle:
    __COLOR_VARIANTS = ['orange', 'purple', 'grey', 'yellow']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        if color.lower() in (c.lower() for c in self.__COLOR_VARIANTS):
            self.color = color

        else:
            raise ValueError(f'Нельзя установить цвет на {color}. Допустимые цвета: {self.__COLOR_VARIANTS}')

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Иощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in (c.lower() for c in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на: {new_color}')


class Sedan(Vehicle):
    __PASSANGERS_LIMIT = 5
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

# Пример использования:
vehicle = Sedan('Avdot', 'Mazda', 175, 'grey')
vehicle.print_info() # изначальные свойства

# Меняем свойства (в т.ч. вызывая методы):
vehicle.set_color('pink')
vehicle.set_color('BLACK')
vehicle.owner = 'Vasyok'

# Проверяем что изменилось:
vehicle.print_info()


