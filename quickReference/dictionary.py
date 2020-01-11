def print_line_break():
    print()
    print("--------------------")
    print()

# create an empty dictionary
newDict = {}

# create an dictionary
age = {"Jason": 19, "Tim": 34, "Jeff": 48, "haha": -43}

# create an dictionary from a sequence of key-value pairs (a list of tuples)

# add key-value pair into a dictionary
age["Sundar Pichai"] = 47

# delete an item from dictionary
del age["haha"]

# change value
print(age["Jason"])  # 19
age["Jason"] = 20  # 20
age["Jason"] += 1  # 21
print(age["Jason"])  # 21

print_line_break()

# counting items: change value without knowing whether the key exist
# (1)
if "Hershey" in age:
    age["Hershey"] += 1
else:
    age["Hershey"] = 1
# (2)
try:
    age["Hershey"] += 1
except:
    age["Hershey"] = 1

# traverse all key-value pairs
for i in age.items():
    print(i, type(i))

print_line_break()

# traverse all keys in a dictionary
# 1
for i in age:
    print(i)
# 2
for k, v in age.items():
    print(k)

print_line_break()

# get a list of keys
# 1
keys = list(age.keys())
# 2
keys = list(age)
print(keys)


print_line_break()

# traverse all values in a dictionary
for i in age:
    print(age[i])

print_line_break()

# get a list of valuse
values = list(age.values())
print(values)

print_line_break()

'''
python dictionary is an unordered data type, so you cannot
sort dictionary and preserve the order as a dictionary
'''
# get a list of keys from a dictionary in alphabetical order
names = sorted(age) # function "sorted()" always return a list
print(names)

# get a list of keys from a dictionary and sorted by its value


# check if a key exist
if "Jason" in age:
    print("Jason exist")
else:
    print("nah")
