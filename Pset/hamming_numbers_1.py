def hamming(n):
    """Returns the nth hamming number"""
    hamming = [1]
    x = 1
    while len(hamming) <= n * 3.5:
        new_hamming = []
        print(len(hamming))

        length = len(hamming)
        s = hamming
        if length >= 1000:
            s = hamming[int(length / 2) : length]

        for i in s:
            new_hamming.append(i * 2)
            new_hamming.append(i * 3)
            new_hamming.append(i * 5)
            x += 1
        # merge new number into hamming set
        hamming = sorted(list(dict.fromkeys(hamming + new_hamming)))
    print(x)
    return hamming[n - 1]


print(hamming(970))


# hamming(968) should be 41943040
# hamming(969) should be 41990400
# hamming(970) should be 42187500
