"""
Strategy (Policy)


Определяет семейство алгоритмов,
инкапсулирует каждый из них и делает их взаимозаменяемыми,
позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.
"""

from abc import ABCMeta, abstractmethod


class SalaryStrategy(metaclass=ABCMeta):
    """Стратегия оплаты труда."""

    @abstractmethod
    def calculate(self, hours_worked):
        """Считает размер заработной платы."""


class HourlyPaymentStrategy(SalaryStrategy):
    """Почасовая оплата труда."""

    def __init__(self, cost_per_hour):
        """
        Arguments:
            cost_per_hour (int): стоимость часа.
        """
        self._cost_per_hour = cost_per_hour

    def calculate(self, hours_worked):
        return round(self._cost_per_hour * hours_worked, 2)


class FixedRate(SalaryStrategy):
    """Фиксированная ставка."""

    DEFAULT_COUNT_WORKDAYS = 22

    def __init__(self, salary, work_day_duration=8):
        """
        Arguments:
            salary (float): размер оклада.
            work_day_duration (int): количество часов в рабочем дне.
        """
        self._salary = salary
        self._work_day_duration = work_day_duration

    def calculate(self, hours_worked):
        days = (hours_worked / self._work_day_duration)
        return round(self._salary * days / self.DEFAULT_COUNT_WORKDAYS, 2)


class Employee:
    """Сотрудник"""

    def __init__(self, firstname, lastname, hours_worked, salary_strategy):
        self._firstname = firstname
        self._lastname = lastname
        self._hours_worked = hours_worked
        self._salary_strategy = salary_strategy

    def get_fullname(self):
        """Возвращает полное имя сотрудника."""
        return f'{self._firstname} {self._lastname}'

    def calculate_salary(self):
        """Считает зарплату сотрудника."""
        return self._salary_strategy.calculate(self._hours_worked)


if __name__ == '__main__':
    employees = [
        Employee('Вася', 'Пупкин', 3, HourlyPaymentStrategy(1500)),
        Employee('Петя', 'Пупкин', 56, FixedRate(35000)),
    ]

    for person in employees:
        print(f'{person.get_fullname()} заработал {person.calculate_salary()}')
