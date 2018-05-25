
def answer(l, t):
    """
    :param l: A not empty list of positive integers
    :param t: The value of the sum of a sublist.
    :return: Return the first occurrence of a sublist that sums up to the value of t.
    >>> answer([4, 3, 5, 7, 8], 12)
    [0, 2]
    >>> answer([4, 43, 45, 7, 12], 12)
    [4, 4]
    >>> answer([45, 3, 5, 7, 8], 45)
    [0, 0]
    >>> answer([4, 3, 5, 7, 8], 8)
    [1, 2]
    >>> answer([4, 3, 33, 7, 8], 33)
    [2, 2]
    >>> answer([13], 13)
    [0, 0]
    >>> answer([1, 2, 3, 4], 50)
    [-1, -1]
    """
    len_of_list = len(l)

    for start_index in range(len_of_list):
        value = l[start_index]
        end_index = start_index
        # make sure we didn't find the value of t in the list and we wont run off the end of the list
        while value < t and end_index + 1 < len_of_list:
            end_index += 1
            value += l[end_index]
        if value == t:
            return [start_index, end_index]
    # not found
    return [-1, -1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
