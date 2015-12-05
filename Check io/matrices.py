__author__ = 'mslavin'


# BEST SOLUTION:
# def weak_point(matrix):
#     n = len(matrix)
#     row = min(range(n), key=lambda r:sum(matrix[r][c] for c in range(n)))
#     col = min(range(n), key=lambda c:sum(matrix[r][c] for r in range(n)))
#     return row, col

from collections import defaultdict


def weak_point(matrix):
    x = rowing(matrix)
    y = colling(matrix)
    result = (x, y)
    return result


def rowing(matrix):

    rows = {}

    for i, row in enumerate(matrix):
        rows[i] = sum(row)

    drows = defaultdict(set)

    for k, v in rows.items():
        drows[v].add(k)
    ddrows = {k: v for k, v in drows.items() if len(v) > 1}

    if min(rows.values()) in ddrows:
        smallest = min(ddrows.keys())
        return min(ddrows.get(smallest))
    else:
        smallest = min(rows.values())
        return drows.get(smallest).pop()


def colling(matrix):

    find_cols = []
    for i in range(len(matrix[0])):
        find_cols.append([row[i] for row in matrix])

    columns = {}
    for i, row in enumerate(find_cols):
        columns[i] = sum(row)

    dcols = defaultdict(set)

    for k, v in columns.items():
        dcols[v].add(k)
    ddcols = {k: v for k, v in dcols.items() if len(v) > 1}

    if min(columns.values()) in ddcols:
        smallest = min(ddcols.keys())
        return min(ddcols.get(smallest))
    else:
        smallest = min(columns.values())
        return dcols.get(smallest).pop()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"