class Employee:
    def __init__(self, fname, lname, salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary
        
    def calculate_paycheck(self) -> None:
        # Salary is split evenly by 52 weeks of the year.
        return self.salary/52