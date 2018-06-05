def answer(l):
    """
    Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples"
    of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and
    2000 inclusive.  The elements of l are between 1 and 999999 inclusive. The answer fits within a signed 32-bit
    integer. Some of the lists are purposely generated without any access codes to throw off spies,
    so if no triples are found, return 0.
    >>> answer([1, 2, 3, 4, 5, 6])
    3
    >>> answer([1, 1, 1])
    1
    """
    triple_count = 0

    divides_counter = [0] * len(l)
    for item in range(0, len(l)):
        j = 0
        for j in range(0, item):
            if l[item] % l[j] == 0:
                divides_counter[item] += 1
                triple_count += divides_counter[j]
    return triple_count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
