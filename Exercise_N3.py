
def bomber_man(n, grid):
    rows = len(grid)
    columns = len(grid[0])

    if n == 1:
        return grid
    elif n % 2 == 0:
        return ['O' * columns for i in range(rows)]

    n = n // 2
    for k in range((n + 1) % 2 + 1):
        new_grid = [['O'] * columns for i in range(rows)]

        adjecent_cells = [[0, 0], [0, -1], [0, 1], [1, 0], [-1, 0]]

        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == "O":
                    for adjecent_cell in adjecent_cells:
                        if 0 <= x + adjecent_cell[0] < rows and 0 <= y + adjecent_cell[1] < columns:
                            new_grid[x + adjecent_cell[0]][y + adjecent_cell[1]] = '.'

        grid = new_grid
    return [''.join(i) for i in grid]