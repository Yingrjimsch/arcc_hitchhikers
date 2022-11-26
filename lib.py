# -*- coding: utf-8 -*-
import numpy as np
import collections

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


"""Funktion extrahiert alle gleichen Farben, returnt matrizen pro farbe"""

"""Rand Hinzufügen (nxm => n+2xm+2) (kochma2)"""
def add_border(matrix):
    return np.pad(matrix, 1, mode='constant', constant_values=10)

"""nachbaren erkennen (zurückgeben) pro pixel (kochma2)"""
def get_pixel_neighbours(matrix, pixel):
    neighbours = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            neighbours[i, j] = matrix[pixel[0]-1+i, pixel[1]-1+j]
    return neighbours

"""prüfen dass nachbaren ähnliche farbe haben"""

"""prüfen ob array dimensionen gleich sind  (vonwareb)"""

def equal_matrix_dimensions(matrix_one, matrix_two):
    """
    Checks if dimensions of input matrix and output matrix are equal
    :param array_one:
    :param array_two:
    :return: boolean
    """

    matrix_one_new = np.asarray(matrix_one)
    matrix_two_new = np.asarray(matrix_two)
    return matrix_one_new.shape == matrix_two_new.shape

"""prüfen ob farb summe gleich bleibt (vonwareb)"""

def check_same_color_sum(matrix_one, matrix_two):
    """
    Compares two matrices for equality of the number of the same color values in both.
    Matrices are converted to dictionaries for this purpose
    :param matrix_one:
    :param matrix_two:
    :return: added colors, removed colors,
    modified colors (count of color pixels in matrix_one and count of color pixels in matrix_two),
    same colors (count of color pixels in matrix_one and count of color pixels in matrix_two ar equal),
    equality of matrix_one and matrix_two
    """

    dict_matrix_one = collections.Counter(np.asarray(matrix_one).flatten())
    dict_matrix_two = collections.Counter(np.asarray(matrix_two).flatten())
    dict_matrix_one_keys = set(dict_matrix_one.keys())
    dict_matrix_two_keys = set(dict_matrix_two.keys())
    shared_keys = dict_matrix_one_keys.intersection(dict_matrix_two_keys)
    added = dict_matrix_one_keys - dict_matrix_two_keys
    removed = dict_matrix_two_keys - dict_matrix_one_keys
    modified = {obj: (dict_matrix_one[obj], dict_matrix_two[obj]) for obj in shared_keys if dict_matrix_one[obj] != dict_matrix_two[obj]}
    same = set(obj for obj in shared_keys if dict_matrix_one[obj] == dict_matrix_two[obj])
    equality = len(same) == len(dict_matrix_one)
    return added, removed, modified, same, equality

"""pixel verschieben"""

"""gruppe(objekt) verschieben"""

"""muster erkennen (wiederholung von farben)"""

"""objekt skalieren"""

"""objekt erkennen (default objekte angeben wie quadrat, rechteck, kreuz)"""


"""objekt duplizieren"""

"""wandinteraktion erkennen"""

"""pixel farbe ändern"""


"""objekt farbe ändern"""

"""racetrack connect shortest path (42oli)"""


