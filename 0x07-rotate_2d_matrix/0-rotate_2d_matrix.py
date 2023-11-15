#!/usr/bin/python3
"""Rotate 2d matrix
"""


def push(data, array):  # Adds data to index 0 of array
    temp = array
    array = []
    array.append(data)
    for i in temp:
        array.append(i)
    return array


def rotate_2d_matrix(matrix):
    temp = []  # placeholder for matrix data
    temp2 = matrix[:]  # copy of matrix
    col_len = len(matrix)  # number of rows
    row_len = len(matrix[0])  # number of columns
    for i in range(row_len):
        temp_row = []
        for row in matrix:
            temp_row = push(row[i], temp_row)
        temp.append(temp_row)
    for temps in temp:
        matrix.append(temps)
    for i in range(col_len):
        matrix.remove(temp2[i])
