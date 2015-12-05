def count_neighbours(grid, row, col):
    length_grid = len(grid[0])  # width of grid is the number of columns
    width_grid = len(grid)  # length of grid is the number of rows
    count = 0

    coord_lines = [[(r, c) for c in range(length_grid)] for r in range(width_grid)]  # coordinates of grid

    for l, line in enumerate(coord_lines):
        for coord in line:
            r, c = coord
            if (r == row or r == row + 1 or r == row - 1) and (c == col or c == col + 1 or c == col - 1):  # accounts for surrounding spaces
                if 0 <= r < width_grid and 0 <= c < length_grid:  # to avoid Tuple out of Range Error
                    count += grid[r][c]  # since grid is 1s and 0s, we can just add the value at that position

    if grid[row][col] == 1:  # rules of challenge did not want to count if the given space was a 1 or not
        count -= 1

    return(count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

# Top Answer in Solutions:

# def count_neighbours(grid, row, col):
#     rows = range(max(0, row - 1), min(row + 2, len(grid)))
#     cols = range(max(0, col - 1), min(col + 2, len(grid[0])))
# ​
#     return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]