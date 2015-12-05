def checkio(matrix):
    for row in matrix:
        for i in row:
            if row.count(i) >= 4:
                if str(i)*4 in ''.join(str(s) for s in row):
                    return True

    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])
        for row in transposed:
            for i in row:
                if row.count(i) >= 4:
                    if str(i)*4 in ''.join(str(s) for s in row):
                        return True

    h = len(matrix)
    w = len(matrix[0])
    dags = [[matrix[h-1-q][p-q] for q in range(min(p, h-1), max(0, p-w+1)-1, -1)] for p in range(h+w-1)]
    print(dags)
    for row in dags:
        for i in row:
            if row.count(i) >= 4:
                if str(i)*4 in ''.join(str(s) for s in row):
                    return True

    new_matrix = []
    for row in matrix:
        new_row = list(reversed(row))
        new_matrix.append(new_row)

    j = len(new_matrix)
    k = len(new_matrix[0])
    dags2 = [[new_matrix[j-1-z][p-z] for z in range(min(p, j-1), max(0, p-k+1)-1, -1)] for p in range(j+k-1)]
    print(dags2)
    for row in dags2:
        for i in row:
            if row.count(i) >= 4:
                if str(i)*4 in ''.join(str(s) for s in row):
                    return True

    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"