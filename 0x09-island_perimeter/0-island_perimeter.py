#!/usr/bin/python3
"""Island perimeter
"""


def check_border(square, grid, col_idx, row_idx):
    """Check if square is bordered by land or water.

    Args:
        square (int): Peice of land
        grid (List[List]): Area of water.
        col_idx (int): Column index
        row_idx (int): Row index

    Returns:
        int: number of water bodered by.
    """
    total = 0
    row = grid[row_idx]
    size = len(grid)

    # check vertical borders
    def check_v(col_idx, prev_row=None, next_row=None):
        res = 0
        if prev_row is None:
            res = next_row[col_idx]
        elif next_row is None:
            res = prev_row[col_idx]
        else:
            res = next_row[col_idx] + prev_row[col_idx]
        return res

    # check horizontal borders
    def check_h(row, prev_col=None, next_col=None):
        res = 0
        if prev_col is None:
            res = row[next_col] if next_col is not None else 0
        elif next_col is None:
            res = row[prev_col] if prev_col is not None else 0
        else:
            res = row[next_col] + row[prev_col]
        return res

    # get total borders
    if row_idx == 0:
        total += check_v(col_idx, next_row=grid[row_idx + 1])
    elif row_idx >= size - 1:
        total += check_v(col_idx, prev_row=grid[row_idx - 1])
    else:
        total += check_v(col_idx, prev_row=grid[row_idx - 1],
                         next_row=grid[row_idx + 1])

    if col_idx == 0:
        total += check_h(row, next_col=col_idx + 1)
    elif col_idx >= len(row) - 1:
        total += check_h(row, prev_col=col_idx - 1)
    else:
        total += check_h(row, prev_col=col_idx - 1, next_col=col_idx + 1)

    return 4 - total


def island_perimeter(grid):
    """Find the perimeter of the island in grid coordinates.

    Args:
        grid (List[List]): Integer List of List
    """
    borders = []
    for row_idx, row in enumerate(grid):
        if 1 in row:
            for col_idx, square in enumerate(row):
                if square == 1:
                    border = check_border(square, grid, col_idx, row_idx)
                    borders.append(border)
    return sum(borders)
