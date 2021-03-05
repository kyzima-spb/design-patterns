<?php

/**
 * Strategy (Policy)
 *
 * Определяет семейство алгоритмов,
 * инкапсулирует каждый из них и делает их взаимозаменяемыми,
 * позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.
 */


/**
 * Стратегия оплаты труда
 */
interface SalaryStrategyInterface
{
    /**
     * Считает размер заработной платы.
     * 
     * @param int $hoursWorked количество отработанных часов.
     */
    public function calculate(int $hoursWorked): float;
}


/**
 * Почасовая оплата труда.
 */
class HourlyPaymentStrategy implements SalaryStrategyInterface
{
    private $costPerHour;

    /**
     * @param int $costPerHour стоимость часа.
     */
    public function __construct(int $costPerHour)
    {
        $this->costPerHour = $costPerHour;
    }

    public function calculate(int $hoursWorked): float
    {
        return round($this->costPerHour * $hoursWorked, 2);
    }
}
     

/**
 * Фиксированная ставка.
 */
class FixedRate implements SalaryStrategyInterface
{
    const DEFAULT_COUNT_WORKDAYS = 22;

    private $salary;
    private $workDayDuration;

    /**
     * @param float $salary размер оклада.
     * @param int $workDayDuration количество часов в рабочем дне.
     */
    public function __construct(float $salary, int $workDayDuration=8)
    {
        $this->salary = $salary;
        $this->workDayDuration = $workDayDuration;
    }

    public function calculate(int $hoursWorked): float
    {
        $days = $hoursWorked / $this->workDayDuration;
        return round($this->salary * $days / static::DEFAULT_COUNT_WORKDAYS, 2);
    }
}


/**
 * Сотрудник
 */
class Employee
{
    private $firstname;
    private $lastname;
    private $hoursWorked;
    private $salaryStrategy;

    public function __construct(
        string $firstname,
        string $lastname,
        int $hoursWorked,
        SalaryStrategyInterface $salaryStrategy
    ) {
        $this->firstname = $firstname;
        $this->lastname = $lastname;
        $this->hoursWorked = $hoursWorked;
        $this->salaryStrategy = $salaryStrategy;
    }

    /**
     * Возвращает полное имя сотрудника.
     */
    public function getFullname(): string
    {
        return $this->firstname . ' ' . $this->lastname;
    }

    /**
     * Считает зарплату сотрудника.
     */
    public function calculate_salary(): float
    {
        return $this->salaryStrategy->calculate($this->hoursWorked);
    }
}
        

$employees = [
    new Employee('Вася', 'Пупкин', 3, new HourlyPaymentStrategy(1500)),
    new Employee('Петя', 'Пупкин', 56, new FixedRate(35000)),
];

foreach ($employees as $person) {
    echo $person->getFullname() . ' заработал ' . $person->calculate_salary() . PHP_EOL;
}
