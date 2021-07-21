"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
   Основная сущность (класс) этого проекта — одежда, которая может иметь
   определенное название. К типам одежды в этом проекте относятся пальто и
   костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
   (для костюма). Это могут быть обычные числа: V и H, соответственно. Для
   определения расхода ткани по каждому типу одежды использовать формулы: для
   пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
   методов на реальных данных. Реализовать общий подсчет расхода ткани.
   Проверить на практике полученные на этом уроке знания: реализовать
   абстрактные классы для основных классов проекта, проверить на практике работу
   декоратора @property.
"""

from abc import ABC, abstractmethod


class Dress(ABC):

    def __init__(self, measurements):
        self.measurements = measurements

    @property
    @abstractmethod
    def fabric_usage(self):
        ...


class Coat(Dress):
    @property
    def fabric_usage(self):
        return (self.measurements / 6.5 + 0.5)


class Suite(Dress):
    @property
    def fabric_usage(self):
        return (2 * self.measurements + 0.3)


coat = Coat(10)
suite = Suite(20)

print(coat.fabric_usage + suite.fabric_usage)
