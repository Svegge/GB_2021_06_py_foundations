"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
   атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
   “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
   (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
   метода draw. Для каждого из классов методы должен выводить уникальное
   сообщение. Создать экземпляры классов и проверить, что выведет описанный
   метод для каждого экземпляра.
"""


class Stationery():
    title = 'main'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self) -> None:
        self.title = 'Pen'

    def draw(self):
        print(f'Draw with {self.title}')


class Pencil(Stationery):
    def __init__(self) -> None:
        self.title = 'Pencil'

    def draw(self):
        print(f'Draw with {self.title}')


class Handle(Stationery):
    def __init__(self) -> None:
        self.title = 'Handle'

    def draw(self):
        print(f'Draw with {self.title}')


if __name__ == '__main__':

    main = Stationery()
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    main.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
