# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.color} {self.name} начала движение.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        return f'Машина {self.name} повернула на {direction}.'

    def show_speed(self):
        return f'Скорость {self.name} равна: {self.speed}'


class TownCar(Car):
    # def __init__(self, name, speed, color, is_police=False):
    #     super(TownCar, self).__init__(self, name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Машина {self.name} превысила допустимую скорость 60 км/ч. ' \
                   f'Скорость {self.name} составляет: {self.speed} км/ч'
        else:
            return f'Скорость {self.name} в пределах нормы.'


class WorkCar(Car):
    # def __init__(self, name, speed, color, is_police=False):
    #     super(WorkCar, self).__init__(self, name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Машина {self.name} превысила допустимую скорость 40 км/ч. ' \
                   f'Скорость {self.name} составляет: {self.speed} км/ч'
        else:
            return f'Скорость {self.name} в пределах нормы.'


class SportCar(Car):
    # def __init__(self, name, speed, color, is_police=False):
    #     super(SportCar, self).__init__(self, name, speed, color, is_police)
    def show_speed(self):
        if self.speed > 90:
            return f'Машина {self.name} превысила допустимую скорость 90 км/ч. ' \
                   f'Скорость {self.name} составляет: {self.speed} км/ч'
        else:
            return f'Скорость {self.name} в пределах нормы.'


class PoliceCar(Car):
    # def __init__(self, name, speed, color, is_police=True):
    #     super().__init__(name, speed, color, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - это полицейская машина.'
        else:
            return f'{self.name} - это не полицейская машина.'


town = TownCar('Ford', 100, 'Серый', False)
print(town.go(), town.show_speed(), town.turn('право'), town.stop(), '\n')

work = WorkCar('Volkswagen', 40, 'Желтый', False)
print(work.go(), work.show_speed(), work.turn('лево'), work.stop(), '\n')

sport = SportCar('Ferrari', 120, 'Синий', False)
print(sport.go(), sport.show_speed(), sport.turn('лево'), sport.turn('право'), sport.stop(), '\n')

police = PoliceCar('Opel', 100, 'Бело-голубой', True)
print(police.go(), police.show_speed(), police.turn('право'), police.turn('лево'), police.stop(), '\n')
