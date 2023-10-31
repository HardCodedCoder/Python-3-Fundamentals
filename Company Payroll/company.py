from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee


class Company:
    def __init__(self) -> None:
        self.employees = []

    def add_employee(self, new_employee) -> None:
        if new_employee is None:
            raise ValueError("The passed employee mustn't be None!")
        self.employees.append(new_employee)

    def print_employees(self) -> None:
        print('Current Employees: ')
        for employee in self.employees:
            print(employee.fname, employee.lname)
        print("------------------------")

    def pay_employees(self):
        print('Paying Employees:')
        for employee in self.employees:
            print('Paycheck for: ', employee.fname, employee.lname)
            print(f'Amount: ${employee.calculate_paycheck():,.2f}')
            print("------------------------------")


def main() -> None:
    my_company = Company()

    employee1 = SalaryEmployee("Max", "Mustermann", 10000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Hermine", "Musterfrau", 25, 50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee("Moritz", "Farbenfroh", 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.print_employees()
    my_company.pay_employees()


main()
