import string

# Open text file in reading mode
file = "Doc1.txt"
document = open(file, "r")
# initilise empty dictionary
dict = dict()
totalWordCount = 0

def removeWhitespaces(target):
    start = 0
    end = len(target)
    for i in range(end):
        if target[i] != " ":
            start = i
            break
    while end >= 1:
        if target[end-1] != " ":
            break
        end -= 1
    return target[start:end]

def removePunctuations(target):
        start = 0
        end = len(target)
        for i in range(end):
            if target[i] not in string.punctuation:
                start = i
                break
        while end >= 1:
            if target[end-1] not in string.punctuation:
                break
            end -= 1
        return target[start:end]

def stripForWord(word):
    return removePunctuations(removeWhitespaces(word.lower()))

for line in document:
    for word in line.split():
        totalWordCount += 1
        word = stripForWord(word)
        if word == "":
            continue
        x = len(word) - 1
        if word[x] not in string.ascii_letters:
            word = word[0:x]

        try:
            dict[word] += 1
        except:
            dict[word] = 1



sorted = sorted(dict, key=lambda x: dict[x], reverse=True)

print(dict, "\n")
x = 20
print(f"Word Count Ranking Top {x}: ")
for i in sorted:
    if x > 0:
        x -= 1
        print(f"{i}  |  {dict[i]}")
    else:
        break
print(f"Total Word Count: {totalWordCount}")
print(f"Number of Unique Words: {len(dict)}")
