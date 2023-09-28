#!/usr/bin/python3
"""
0-pascal_triangle
"""

def factorial(n):
    """
    Find the factorial of n
        n! = n x (n-1) x (n-2)... 1
        example: 5! = 5 x 4 x 3 x 2 x 1 = 120
        return: n!
    """
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

def pos_pascal_triangle(level, index):
    """
        Solve combinations for getting positional value in level.
        fomular: nCr = n!/r!(n-r)!
    """
    return factorial(level) / (factorial(index) * factorial(level - index))

def pascal_triangle(n):
    """ Solves the pascal triangle """
    triangle = []
    for level in range(n):
        node = []
        for index in range(level + 1):
            node.append(int(pos_pascal_triangle(level, index)))
        triangle.append(node)
    return triangle
