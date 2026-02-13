import logging

logging.basicConfig(
    filename="payroll.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:

    hra_percentage=20   

    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.salary = 0
        

    def calculate_salary(self):
        hra = (self.basic_salary * Employee.hra_percentage) / 100
        self.salary = self.basic_salary + hra
        logging.info("Salary of Employee: %s", self.salary)
        

    def apply_leave_deduction(self, leave_days):
        deduction = leave_days * 500
        self.salary -= deduction
        logging.warning("Leave deduction applied for Employee %s of %s", self.emp_id,deduction)

    def display_payslip(self):
        logging.info("Payslip of Employee %s", self.emp_id)
        logging.info("Employee ID:%s", self.emp_id)
        logging.info("Name:%s", self.name)
        logging.info("Salary:%s", self.salary)

    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra
        logging.info("HRA percentage updated to %s", new_hra)


e1 = Employee(1, "Ram", 20000)
e1.calculate_salary()
e1.apply_leave_deduction(2)
e1.display_payslip()

Employee.update_hra_percentage(30)
