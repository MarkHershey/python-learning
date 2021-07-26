a = 12
print(f"a is {a}")
print(f"Data Type of a is {type(a)}")

b = 3.1415926
print(f"b is {b}")
print(f"Data Type of b is {type(b)}")

c = "message"
print(f"c is {c}")
print(f"Data Type of c is {type(c)}")

d = True
print(f"d is {d}")
print(f"Data Type of d is {type(d)}")

e = None
print(f"e is {e}")
print(f"Data Type of e is {type(e)}")


# type conversion
print("------------------")
print(b, type(b), sep=" | ")
b = int(b)
print(b, type(b), sep=" | ")
b = float(b)
print(b, type(b), sep=" | ")
b = str(b)
print(b, type(b), sep=" | ")
