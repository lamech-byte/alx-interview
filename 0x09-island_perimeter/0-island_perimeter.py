#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of an island described by the given grid.

    Args:
    grid (list of list of int): A grid representing the island, where
    0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.

    Notes:
    - Cells are connected horizontally/vertically (not diagonally).
    - The grid is rectangular, with width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn’t have "lakes" (water inside that isn’t connected to
    the water surrounding the island).
    """

    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    
    return perimeter
