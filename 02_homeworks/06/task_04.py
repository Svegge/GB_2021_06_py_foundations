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
    is_police = 0
    name = 'Car'

    def __init__(self, speed, color) -> None:
        self.speed = speed
        self.color = color

    def go(self):
        print(f'{self.name} runs')

    def stop(self):
        print(f'{self.name} stops')

    def turn(self, direction):
        dic_directions = {
            'w': 'forward',
            's': 'backward',
            'a': 'left',
            'd': 'right',
        }
        print(f'{self.name} turns {dic_directions[direction]}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    """
    не понял разницу между передачей параметров через super()
    и и передачей через self. в примере ниже:
    """

    def __init__(self, speed, color):
        # super().__init__(speed, color)
        self.speed = speed
        self.color = color
        self.name = 'Town Car'

    def show_speed(self):
        if self.speed > 60:
            print('Exceed speed limit!')


class SportCar(Car):

    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.name = 'Sport Car'


class PoliceCar(Car):

    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.name = 'Police Car'
        self.is_police = 1


class WorkCar(Car):
    """
    не понял разницу между передачей параметров через super()
    и и передачей через self. в примере ниже:
    """

    def __init__(self, speed, color):
        # super().__init__(speed, color)
        self.speed = speed
        self.color = color
        self.name = 'Work Car'

    def show_speed(self):
        if self.speed > 40:
            print('Exceed speed limit!')


if __name__ == '__main__':
    car_one = TownCar(150, 'green')
    car_one.show_speed()
    print(
        car_one.name,
        car_one.color,
        car_one.is_police,
        car_one.speed,
        '\n',
        '-' * 10)

    car_two = SportCar(200, 'yellow')
    car_two.show_speed()
    print(
        car_two.name,
        car_two.color,
        car_two.is_police,
        car_two.speed,
        '\n',
        '-' * 10)

    car_three = PoliceCar(90, 'black')
    car_three.show_speed()
    print(
        car_three.name,
        car_three.color,
        car_three.is_police,
        car_three.speed,
        '\n',
        '-' * 10)

    car_four = WorkCar(90, 'brown')
    car_four.show_speed()
    print(
        car_four.name,
        car_four.color,
        car_four.is_police,
        car_four.speed,
        '\n',
        '-' * 10)

    car_four.go()
    car_four.stop()
    car_four.turn('a')
    car_four.turn('w')
