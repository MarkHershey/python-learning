# create an empty dictionary
newDict = {}

# create an dictionaty
age = {"Jason":19, "Tim":34, "Jeff":48}

# add key-value pair into a dictionary
age["Sundar Pichai"] = 47

# change value
print(age["Jason"])
age["Jason"] = 20
age["Jason"] += 1
print(age["Jason"])

# change value without knowing whether the key exist
try:
    age["Hershey"] += 1
except:
    age["Hershey"] = 1

# get a list of keys

# get a list of values

# sort dictionary by key

# sort dictionary by value
