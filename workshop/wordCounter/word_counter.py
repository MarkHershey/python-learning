text = open("Doc0.txt", 'r')
h = 0
t = ""
dict = dict()
for line in text:
    for i in line:
        if i not in ('.', ',', ' '):
            t += i.lower()
        else:
            try:
                dict[t] += 1
                t = ""
            except:
                if t != "":
                    dict[t] = 1
                t = ""

sorted = sorted(dict, key=lambda x:dict[x], reverse=True)

for i in sorted:
    print(f"{i}: {dict[i]}")
