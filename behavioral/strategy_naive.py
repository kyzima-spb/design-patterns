"""
Реализация в лоб без использования шаблона проектирования.
"""

from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """Сотрудник"""

    def __init__(self, firstname, lastname, hours_worked):
        self._firstname = firstname
        self._lastname = lastname
        self._hours_worked = hours_worked

    def get_fullname(self):
        """Возвращает полное имя сотрудника."""
        return f'{self._firstname} {self._lastname}'

    @abstractmethod
    def calculate_salary(self):
        """Считает зарплату сотрудника."""


class HourlyPaymentEmployee(Employee):
    """Сотрудник с почасовой оплатой труда."""

    def __init__(self, firstname, lastname, hours_worked, cost_per_hour):
        super().__init__(firstname, lastname, hours_worked)
        self._cost_per_hour = cost_per_hour

    def calculate_salary(self):
        return round(self._cost_per_hour * self._hours_worked, 2)


class FixedRateEmployee(Employee):
    """Сотрудник с фиксированной ставкой."""

    DEFAULT_COUNT_WORKDAYS = 22

    def __init__(self, firstname, lastname, hours_worked, salary, work_day_duration=8):
        super().__init__(firstname, lastname, hours_worked)
        self._salary = salary
        self._work_day_duration = work_day_duration

    def calculate_salary(self):
        days = (self._hours_worked / self._work_day_duration)
        return round(self._salary * days / self.DEFAULT_COUNT_WORKDAYS, 2)


if __name__ == '__main__':
    employees = [
        HourlyPaymentEmployee('Вася', 'Пупкин', 3, 1500),
        FixedRateEmployee('Петя', 'Пупкин', 56, 35000),
    ]

    for person in employees:
        print(f'{person.get_fullname()} заработал {person.calculate_salary()}')
