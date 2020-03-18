from property import Person

print("---------------------------------------------")

p1 = Person("Mark", 1997)
print(f"p1: {p1}")

print("---------------------------------------------")

p1.birthYear = 1999
print(f"p1: {p1}")

print("---------------------------------------------")

p2 = Person("Meridith")
print(f"p2: {p2}")

print("---------------------------------------------")

p2.birthYear = 1989
print(f"p2: {p2}")

print("---------------------------------------------")

try:
    p2.age = 30
except AttributeError:
    print("Attribute Error catched as expected.")
else:
    print("!!! something is wrong")

print("---------------------------------------------")

try:
    p = Person(12, 1997)
except TypeError:
    print("Type Error catched as expected.")
else:
    print("!!! something is wrong")

print("---------------------------------------------")

try:
    p = Person("Jackson", "1999")
except TypeError:
    print("Type Error catched as expected.")
else:
    print("!!! something is wrong")

print("---------------------------------------------")

try:
    p = Person("Jackson", 100)
except ValueError:
    print("Value Error catched as expected.")
else:
    print("!!! something is wrong")

print("---------------------------------------------")

try:
    p = Person("Jackson", 2070)
except ValueError:
    print("Value Error catched as expected.")
else:
    print("!!! something is wrong")
