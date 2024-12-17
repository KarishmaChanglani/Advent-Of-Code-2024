import re

def create_grid():
    grid = []

    with open("input_day4.txt") as f:
        for line in f:
            grid.append(line.strip())

    return grid


def get_diagonals():
    diagonals = []
    rows, cols = len(grid), len(grid[0])

    # top-left to bottom-right
    for d in range(-(rows - 1), cols):
        diag = [grid[i][i - d] for i in range(max(0, d), min(rows, cols + d))]
        diagonals.append(diag)

    # top-right to bottom-left
    for d in range(rows + cols - 1):
        diag = [grid[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))]
        diagonals.append(diag)

    return diagonals


def count_with_pattern(grid, pattern):
    occurrences = 0
    for row in grid:
        row_str = ''.join(row)
        occurrences += len(re.findall(pattern, row_str))
        occurrences += len(re.findall(pattern, row_str[::-1]))  # check for matches on reversed
    return occurrences


def check_x_mas(grid, i, j):
    rows, cols = len(grid), len(grid[0])

    if i - 1 < 0 or i + 1 >= rows or j - 1 < 0 or j + 1 >= cols: # for corners
        return False

    patterns = ["MAS", "SAM"]

    l_diag = ''.join([grid[i - 1][j - 1], grid[i][j], grid[i + 1][j + 1]])
    r_diag = ''.join([grid[i - 1][j + 1], grid[i][j], grid[i + 1][j - 1]])

    if (l_diag in patterns and r_diag in patterns) or (l_diag[::-1] in patterns and r_diag[::-1] in patterns):
        return True

    return False


if __name__ == "__main__":
    grid = create_grid()

    pattern = r'XMAS'

    count = count_with_pattern(grid, pattern)
    count += count_with_pattern(list(zip(*grid)), pattern)  # vertical occurrences
    count += count_with_pattern(get_diagonals(), pattern)

    print("First part: " + str(count))

    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(1, rows - 1):
        for j in range(1,cols - 1):
            if check_x_mas(grid, i, j):
                count += 1

    print("Second part: " + str(count))


