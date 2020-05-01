class Person:
    # static variable
    currentYear = 2020

    def __init__(self, name, birthYear=None):
        self.name = name
        self.birthYear = birthYear

    @property
    def name(self):
        print("name getter ran")
        return self._name

    @name.setter
    def name(self, value):
        print("name setter ran")
        if type(value) is str:
            self._name = value
        else:
            raise TypeError("name attribute accepts string only")

    @property
    def birthYear(self):
        print("birthYear getter ran")
        return self._birthYear

    @birthYear.setter
    def birthYear(self, value):
        print("birthYear setter ran")
        if value == None:
            self._birthYear = None
        elif type(value) not in (int, None):
            raise TypeError("birthYear attribute accepts integer only")
        elif value < 1900:
            raise ValueError("birthYear attribute value less than 1900 not supported")
        elif value > Person.currentYear:
            raise ValueError("birthYear cannot be larger than current year")
        else:
            self._birthYear = value

    @birthYear.deleter
    def birthYear(self):
        self._birthYear = None

    @property
    def age(self):
        print("age getter ran")
        if self._birthYear == None:
            return None
        else:
            return Person.currentYear - self._birthYear

    def __str__(self):
        return f"{self.name}(Age: {self.age})"
