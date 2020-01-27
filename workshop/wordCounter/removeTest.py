# function to remove leading and trailling whitespaces
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


print(removeWhitespaces("  test ndfsfdf/../8       ") == "test ndfsfdf/../8")
print(removeWhitespaces("  testsdfsdfsdfsdfsdf       ") == "testsdfsdfsdfsdfsdf")
print(removeWhitespaces("       ") == "")
print(removeWhitespaces("") == "")
print(removeWhitespaces("test") == "test")
print(removeWhitespaces("test ") == "test")
print(removeWhitespaces(" ,test ") == ",test")
print(removeWhitespaces(" t e s t ") == "t e s t")
print(removeWhitespaces(" 34985734 ") == "34985734")


import string
# function to remove leading and trailling punctuations
def removePunctuations(target):
        start = 0
        end = len(target)
        for i in range(end):
            if target[i] in string.ascii_letters:
                start = i
                break
        while end >= 1:
            if target[end-1] in string.ascii_letters:
                break
            end -= 1
        return target[start:end]

print(removePunctuations("{thisidfhsdf}") == "thisidfhsdf")
print(removePunctuations("{thisidfhsdf") == "thisidfhsdf")
print(removePunctuations("thisidfhsdf.") == "thisidfhsdf")
print(removePunctuations("thisidfhsdf\'") == "thisidfhsdf")

def stripForWord(word):
    return word.lower().strip().strip(string.punctuation).capitalize()
print("?" == "?")

print(stripForWord("       {thisidfhsdf}") == "Thisidfhsdf")
print(stripForWord("{thisidfhsdf     ") == "Thisidfhsdf")
print(stripForWord("   'thisidfhsdf'  ") == "Thisidfhsdf")
print(stripForWord("thisdfhsdf\'") == "Thisdfhsdf")
print(stripForWord("“sword?") == "sword")
print(stripForWord("“sword?"))
print(stripForWord("“；‘sword?") == "sword")
print(stripForWord("“；‘sword?"))
