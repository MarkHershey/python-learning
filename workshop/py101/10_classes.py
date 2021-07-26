class People:
    def __init__(self, name, birthYear):
        self.name = name
        self.birthYear = birthYear
        self.age = 2020 - birthYear
        self.height = None
        self.pillar = None


p1 = People("Maria", 1999)
print(p1.name)
print(p1.birthYear)
print(p1.age)

p1.pillar = "Architecture and Sustainable Design (ASD)"

print(f"{p1.name} is {p1.age} years old, and she is majored in {p1.pillar}")
