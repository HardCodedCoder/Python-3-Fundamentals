class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary) -> None:
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self) -> float:
        # Salary is split evenly by 52 weeks of the year.
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self) -> float:
        return self.weekly_hours * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate) -> None:
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def calculate_paycheck(self) -> float:
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num*self.com_rate
        return regular_salary + total_commission