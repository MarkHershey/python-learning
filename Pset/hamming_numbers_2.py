def hamming(n):
    """Returns the nth hamming number"""
    hamming = [1]
    i = j = k = 0
    while n:
        while hamming[i] * 2 <= hamming[-1]:
            i += 1
        while hamming[j] * 3 <= hamming[-1]:
            j += 1
        while hamming[k] * 5 <= hamming[-1]:
            k += 1
        hamming.append(min(hamming[i] * 2, hamming[j] * 3, hamming[k] * 5))
        n -= 1

    return hamming[-2]


print(hamming(970))


# hamming(968) should be 41943040
# hamming(969) should be 41990400
# hamming(970) should be 42187500
