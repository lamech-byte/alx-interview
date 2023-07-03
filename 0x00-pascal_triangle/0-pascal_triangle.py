#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: The generated Pascal's Triangle as a nested list of integers.

    """
    if n <= 0:
        return []

    # Start with the first row containing only 1
    triangle = [[1]]

    for i in range(1, n):
        # Generate the current row based on the previous row
        row = [1] + [
            triangle[i - 1][j] + triangle[i - 1][j + 1]
            for j in range(i - 1)
        ] + [1]
        triangle.append(row)

    return triangle
