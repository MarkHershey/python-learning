import string


file = "J. K. Rowling - Harry Potter and the Chamber of Secrets.txt"

doc = open(file, 'r')

dict = dict()

for line in doc:
    for word in line.split():
        x = len(word) - 1
        word = word.lower()
        if word[x] not in string.ascii_letters:
            word = word[0:x]

        try:
            dict[word] += 1
        except:
            dict[word] = 1


        # if i not in ('.', ',', ' '):
        #     t += i.lower()
        # else:
        #     try:
        #         dict[t] += 1
        #         t = ""
        #     except:
        #         if t != "":
        #             dict[t] = 1
        #         t = ""
#
sorted = sorted(dict, key=lambda x:dict[x], reverse=True)


print(f"Number of Unique Words: {len(dict)}")
print("Word Count Ranking: ")
x = 20

for i in sorted:
    if x >= 0:
        x -= 1
        print(f"{i}: {dict[i]}")
    else:
        break
