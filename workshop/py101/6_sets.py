s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(2)
s.add(1)
s.add(0)

print("set s | ", s)


odd = set((1, 3, 5, 7, 9, 11))
even = {2, 4, 6, 8, 10}

s1 = odd.intersection(even)
print("the intersection of odd and even | ", s1)
s2 = odd.union(even)
print("the union of odd and even | ", s2)
s3 = odd.difference(s)
print("the difference between s and odd | ", s3)
