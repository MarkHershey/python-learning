text = open("test.txt", "r")
for i in text:
    print("---start---")
    print(i, type(i))
    for x in i:
        print(x)
    print("---end---")
