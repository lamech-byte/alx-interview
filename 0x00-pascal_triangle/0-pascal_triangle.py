#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1] + [
                triangle[i - 1][j] + triangle[i - 1][j + 1]
                for j in range(i-1)] + [1]
        triangle.append(row)

    return triangle
