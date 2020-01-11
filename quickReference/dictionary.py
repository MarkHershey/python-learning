def example(n):
    if type(n) in [type(1), type(1.1)]:
        n = str(n)
    print()
    print()
    print("--------------------------Example {}--------------------------".format(n))


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
example(1)
print(age["Jason"])  # 19
age["Jason"] = 20  # 20
age["Jason"] += 1  # 21
print(age["Jason"])  # 21


# counting items: change value without knowing whether the key exist
example(2)
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

# check if a key exist
if "Jason" in age:
    print("Jason exist")
else:
    print("nah")


# traverse all key-value pairs
example(3)
for i in age.items():
    print(i, type(i))


# traverse all keys in a dictionary
example(4)
# 1
for i in age:
    print(i)
# 2
for k, v in age.items():
    print(k)


# get a list of keys
example(5)
# 1
keys = list(age.keys())
# 2
keys = list(age)
print(keys)


# traverse all values in a dictionary
example(6)
for i in age:
    print(age[i])


# get a list of valuse
example(7)
values = list(age.values())
print(values)


"""
python dictionary is an unordered data type, so you cannot
sort dictionary and preserve the order as a dictionary
"""
example(8.1)

grade_stat = {"A": 12, "F": 2, "B": 33, "C": 92, "E": 19, "D": 64}
print(grade_stat)
# get a list of keys from a dictionary in alphabetical order
grades = sorted(grade_stat)  # function "sorted()" always return a list
print(grades)

# get a list of keys from a dictionary and sorted by its value
example(8.2)
grades = sorted(grade_stat, key=grade_stat.get, reverse=True)
print(grades)
for grade in grades:
    print("{}: {}".format(grade, grade_stat[grade]))


# get a list of sorted values from a dictionary
example(8.3)
val = []
for k, v in grade_stat.items():
    val.append(v)
print("unsorted list of values", val)
print("sorted list of values", sorted(val))
