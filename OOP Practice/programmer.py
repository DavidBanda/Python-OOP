from employee import Employee


class Programmer(Employee):
    """
    >>> prog_1 = Programmer('Enrique', 'Guzman', 20000, 'Backend')
    >>> prog_2 = Programmer('Jofiel', 'Batista', 30000, 'Frontend')
    >>> prog_1 + prog_2
    50000
    >>> prog_1.fullname
    'Enrique Guzman'
    >>> prog_2.fullname
    'Jofiel Batista'
    """

    def __init__(self, first_name: str, last_name: str, pay: float, area: str):
        super().__init__(first_name, last_name, pay)
        self.__area = area

    def __add__(self, other_programmer: Employee):
        return self.pay + other_programmer.pay


if __name__ == '__main__':
    import doctest
    doctest.testmod()
