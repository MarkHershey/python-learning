#################### version 1 #################################################

a = list(range(10))
# print(a, id(a))

res_1 = list(a)
# print(res_1, id(res_1))

for i in a:
    if i in (3, 5):
        print(">>>", i, id(i))
        res_1 = list(filter(lambda x: x != i, res_1))
        # print(type(res_1), id(res_1))


print(list(res_1))


#################### version 2 #################################################

b = list(range(10))
# print(b, id(b))

res_2 = list(b)
# print(res_2, id(res_2))

for i in b:
    if i in {3, 5}:
        print(">>>", i, id(i))
        res_2 = filter(lambda x: x != i, res_2)
        for w in res_2:
            pass
        # print(type(res_2), id(res_2))
        res_2 = list(res_2)

print(list(res_2))


#################### version 3 #################################################


c = list(range(10))
# print(c, id(c))

res_3 = list(c)
# print(res_3, id(res_3))

for i in c:
    if i in (3, 5):
        print(">>>", i, id(i))
        res_3 = filter(lambda x: x != i, res_3)
        # print(type(res_3), id(res_3))


print(list(res_3))
