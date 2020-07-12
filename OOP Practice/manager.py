from employee import Employee
from programmer import Programmer


class Manager(Employee):

    """
    >>> mgr = Manager('Alonso', 'Martinez', 30000)
    >>> prog_1 = Programmer('David', 'Banda', 10000, 'DevOps')
    >>> prog_2 = Programmer('Pedro', 'Martinez', 20000, 'Backend')
    >>> mgr.add_employee(prog_1)
    >>> mgr.add_employee(prog_2)
    >>> mgr.get_all_employees()
    Alonso Martinez's Employees
    --> David Banda
    --> Pedro Martinez
    >>> mgr.remove_employee(prog_2)
    >>> mgr.get_all_employees()
    Alonso Martinez's Employees
    --> David Banda
    """

    def __init__(self, first_name: str, last_name: str, pay: float, employees=None):
        super().__init__(first_name, last_name, pay)

        if employees is None:
            employees = []
        self.__employees = employees

    def add_employee(self, employee: Employee):
        if self.__check_employee(employee):
            print('Employee already added')
            return
        self.__employees.append(employee)

    def remove_employee(self, employee: Employee):
        if self.__check_employee(employee):
            self.__employees.remove(employee)
            return
        print('Employee not exist')

    def __check_employee(self, employee: Employee):
        if employee in self.__employees:
            return True
        return False

    def get_all_employees(self):
        print(f"{self.fullname}'s Employees")
        for employee in self.__employees:
            print(f'--> {employee.fullname}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
