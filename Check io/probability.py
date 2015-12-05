import itertools

def sum_to_n(n, size, limit=None,):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail


def probability(dice_number, sides, target):
    import math
    probably = 0
    for partition in sum_to_n(target, dice_number, sides):
        print(partition)
        for i in partition:
            if partition.count(i) > 1: # need to move the below out of the for loop??!
                probably += ((1/sides)**dice_number)  # THIS NEEDS TO BE FIXED! what to multiply by?
                print(probably)
            else:
                probably += ((1/sides)**dice_number)*math.factorial(dice_number)
                #print(itertools.permutations(partition, 3))
                print(probably)
    print(probably)



probability(3, 4, 7)




# def sum_to_n(n, size, limit=None,):
#     """Produce all lists of `size` positive integers in decreasing order
#     that add up to `n`."""
#     if size == 1:
#         yield [n]
#         return
#     if limit is None:
#         limit = n
#     start = (n + size - 1) // size
#     stop = min(limit, n - size + 1) + 1
#     for i in range(start, stop):
#         for tail in sum_to_n(n - i, size - 1, i):
#             yield [i] + tail
#
#
# def probability(dice_number, sides, target):
#     probably = 0
#     for partition in sum_to_n(target, dice_number, sides):
#         print(partition)
#         if len(set(partition)) == 1:
#             probably += ((1/sides)**2)
#         else:
#             probably += ((1/sides)**2)*2
#     print(probably)
#
#
# probability(3, 6, 7)