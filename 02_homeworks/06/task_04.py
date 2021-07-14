"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
   атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
   turn(direction), которые должны сообщать, что машина поехала, остановилась,
   повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
   WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
   показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
   переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
   40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте
   экземпляры классов, передайте значения атрибутов. Выполните доступ к
   атрибутам, выведите результат. Выполните вызов методов и также покажите
   результат.
"""

class Car():
    def __init__(self, speed, color, name, is_police) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print('Car runs')

    def stop(self):
        print('Car stops')

    def turn(self, direction):
        dic_directions = {
            'w': 'forward',
            's': 'backward',
            'a': 'left',
            'd': 'right',
        }
        print(f'Car turns {dic_directions[direction]}')
    
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    is_police = 0
    name = 'town car'

    def show_speed(self):
        if self.speed > 60:
            print('Exceed speed limit!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police) -> None:
        super().__init__(speed, color, name, is_police)
        self.is_police = 0
        self.name = 'sport car'

car_one = TownCar(150, 'green')
car_one.show_speed()
print(car_one.name, car_one.color, car_one.is_police, car_one.speed)
# TownCar, SportCar,
#    WorkCar, PoliceCar