# -*- coding: utf-8 -*-
import numpy as np

def rotate_clockwise(matrix):
    return np.array(list(zip(*(reversed(matrix)))))

def rotate_anticlockwise(matrix):
    return np.array(list(zip(*matrix))[::-1])

def reverse(matrix):
    return np.array(list(reversed(matrix)))

def rotate(matrix, move):
    if move == 0:
        return matrix
    elif move == 1:
        return reverse(matrix)
    elif move == 2:
        return rotate_clockwise(matrix)
    elif move == 3:
        return rotate_anticlockwise(matrix)
    else:
        print('This is not possible')

def rotate_back(matrix, move):
    if move == 0:
        return matrix
    elif move == 1:
        return reverse(matrix)
    elif move == 2:
        return rotate_anticlockwise(matrix)
    elif move == 3:
        return rotate_clockwise(matrix)
    else:
        print('This is not possible')        