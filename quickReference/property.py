class Person:
    def __init__(self, name, age=0):
        # Initialise Person.name
        if type(name) == str:
            self.name = name
        else:
            print("Person.name can be String only.")

        # Initialise Person._age
        if type(age) not in (int, float):
            print("Age can be integer or float only.")
        elif age < 0:
            print("Age cannot less than zero.")
        else:
            self._age = age
        
    def __str__(self):
        return f"{self.name}(Age: {self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value) not in (int, float):
            print("Age can be integer or float only.")
        elif value < 0:
            print("Age cannot less than zero.")
        else:
            self._age = value

    @age.deleter
    def age(self):
        # we don't actually want to delete the age attribute from the memory
        # because in this case, it makes no sense if a person don't have an age attribute
        # so we assume when we use del(person.age)
        # we actually meant to remove the age info from this person
        self._age = None

p1 = Person("Mike")
print(p1)
p2 = Person("Jack", "22")

p1.age = 23
print(p1.age)
p1.age = -1

del(p1.age)
print(p1)
