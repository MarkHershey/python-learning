from copy import copy, deepcopy

def printObj(obj, name):
    n = len(name)
    if n <= 13:
        print("-"*(13-n-1), f"{name} | {obj}")
    else:
        print(f"{name} | {obj}")
    print(f"--- Data Type | {type(obj)}")
    print(f"----- Address | {hex(id(obj))}")
    print()


a = ["David", "David", "Maria", [1, 2, 3, 4, 5]]
printObj(a, "a")

x = 1
printObj(x, "x")
printObj(a[3][0], "a[3][0]")

b = a # new variable b will point to the same address as a
printObj(b, "b")

c = a[:] # shallow copy
printObj(c, "c")

d = copy(a) # shallow copy
printObj(d, "d")

e = deepcopy(a) # deep copy
printObj(e, "e")

printObj(d[3], "d[3]")
printObj(e[3], "e[3]")
