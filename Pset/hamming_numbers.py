def hamming(n):
    """Returns the nth hamming number"""
    hamming = {1}
    x = 1
    while len(hamming) <= n * 3.5:
        new_hamming = {1}
        for i in hamming:
            new_hamming.add(i * 2)
            new_hamming.add(i * 3)
            new_hamming.add(i * 5)
        # merge new number into hamming set
        hamming = hamming.union(new_hamming)
    hamming = sorted(list(hamming))
    return hamming[n - 1]


print(hamming(970))


# hamming(968) should be 41943040
# hamming(969) should be 41990400
# hamming(970) should be 42187500
