"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
   name, surname, position (должность), income (доход). Последний атрибут должен
   быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
   например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
   на базе класса Worker. В классе Position реализовать методы получения полного
   имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
   Проверить работу примера на реальных данных (создать экземпляры класса
   Position, передать данные, проверить значения атрибутов, вызвать методы
   экземпляров).
"""


class Worker():

    def __init__(self, name, surname, position, income_dict) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_dict


class Position(Worker):

    def get_total_income(self):
        return sum(self._income.values())

    def get_full_name(self):
        return self.name + ' ' + self.surname


if __name__ == '__main__':
    income_dict = {"wage": 100, "bonus": 200}
    hr_info = Position('John', 'Doe', 'Ranger', income_dict)

    print(hr_info.name, hr_info.surname, hr_info.position, hr_info._income)
    print(hr_info.get_full_name(), hr_info.get_total_income())
