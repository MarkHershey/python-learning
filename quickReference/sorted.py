import numpy as np
import string

'''
list.sort() verses sorted()
'''

list_A = list(np.random.randint(low=1, high=99, size=30))
print("Original List A: ")
print(list_A)
a = list_A.sort() # inplace sort function does NOT return anything

print(list_A) # original list has been sorted
print(a) # variable a is not assigned anything
print()


list_B = list(np.random.randint(low=1, high=99, size=30))
print("Original List B: ")
print(list_B)
b = sorted(list_B) # sorted() returns a new list

print(list_B) # original list remain unchanged
print(b) # new list in sorted order
print()

'''
more about sorted()
'''
list_C = np.random.randint(low=1, high=999, size=26)
print("Original List C: ")
print(list_C)

alpha = list(string.ascii_uppercase)
dict = {}
for k,v in zip(alpha, list_C):
    dict[k] = v
print("Original dictionary: ")
print(dict)
c = sorted(dict, key = dict.get)
for i in c:
    print("{}: {}".format(i, dict[i]))
