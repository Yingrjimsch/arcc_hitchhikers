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

""" Verbindung von zwei Pixeln über horizontal-vertikal (vonwwareb)"""

def connect_horizontal_vertical(matrix, pixel_src, pixel_dest):
    """
    Connection of two pixels via horizontal - vertical connection. Pixel receives the color of the start pixel
    :param matrix:
    :param pixel_src:
    :param pixel_dest:
    :return: matrix_changed
    """
    point_src = (pixel_src[1],pixel_src[0])
    point_dest = (pixel_dest[1],pixel_dest[0])

    row_src = point_src[0]
    column_src = point_src[1]

    row_dest = point_dest[0]
    column_dest = point_dest[1]

    color = matrix[row_src][column_src]
    
    print("before\n", np.asarray(matrix))

    if row_src < row_dest:
        #top-bottom
        for i in range(column_src + 1, column_dest +1):
            matrix[row_src][column_src + 1] = color
            column_src +=1
        for j in range(row_src +1, row_dest):
            matrix[row_src+1][column_dest] = color
            row_src += 1
    else:
        #bottom-top
        for i in range(column_src + 1, column_dest + 1):
            matrix[row_src][column_src + 1] = color
            column_src += 1
        for j in range(row_dest +1, row_src):
            matrix[row_src - 1][column_dest] = color
            row_src -= 1
    return matrix

