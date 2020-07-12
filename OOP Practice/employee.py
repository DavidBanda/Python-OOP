class Employee:
    """
    >>> emp_1 = Employee('David', 'Banda', 20000)
    >>> emp_1.fullname
    'David Banda'
    >>> emp_1.fullname = 'Jose Fernandez Chavez'
    >>> emp_1.fullname
    'Jose Fernandez'
    >>> emp_1.pay
    20000
    """

    __raise_amount: float = 1.00
    __num_employees: int = 0

    def __init__(self, first_name: str, last_name: str, pay: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pay = pay

        Employee.__increase_num_employees()

    @property
    def fullname(self):
        return f'{self.__first_name} {self.__last_name}'

    @fullname.setter
    def fullname(self, name: str):
        name = list(name.split(' '))
        if len(name) in [2, 3]:
            self.__first_name = name[0]
            self.__last_name = name[1]
        else:
            self.__first_name = name[0]
            self.__last_name = name[2]

    @property
    def pay(self):
        return self.__pay

    @property
    def email(self):
        fist_name = self.__first_name.lower()
        last_name = self.__last_name.lower()
        return f'{last_name}.{fist_name}@nearsoft.com'

    @classmethod
    def __increase_num_employees(cls):
        cls.__num_employees += 1

    @classmethod
    def num_of_employees(cls):
        return cls.__num_employees


if __name__ == '__main__':
    import doctest
    doctest.testmod()
