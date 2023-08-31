#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0


"""
Start with the assumption that the current land cell contributes
4 sides to the perimeter
"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                
              """
              Check neighbors (up, down, left, right) and subtract
              1 from perimeter for each neighboring land cell
              """
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    
    return perimeter
