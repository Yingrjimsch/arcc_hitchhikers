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

"""prüfen dass nachbaren ähnliche farbe haben"""

"""prüfen ob array dimensionen gleich sind  (vonwareb)"""

"""prüfen ob farb summe gleich bleibt (vonwareb)"""

"""pixel verschieben (vonwareb)"""
def move_pixel(matrix, pixel, vector):
    """
    Moves a pixel by the specified vector
    :param matrix:
    :param pixel: as [x,y]
    :param vector:
    :return: changed matrix
    """
    #changes pixel [x,y] to point (y,x)
    point = (pixel[1], pixel[0])
    #changes vector [x,y] to vector_transformed (y,x)
    vector_transformed = (vector[1], vector[0])
    matrix_copied = np.asarray(matrix)
    '''
    Checks if the pixel is moved beyond the edge of the matrix.
    If yes, the original pixel is set to color black and no new pixel is set at the new position.
    '''
    if (point[0] + vector_transformed[0] or point[1] + vector_transformed[1]) > matrix_copied.shape[0] - 1:
        matrix_copied[point] = 0
        return matrix_copied
    color = matrix_copied[point]
    print("color: ", color)
    matrix_copied[point[0] + vector_transformed[0], point[1] + vector_transformed[1]] = color
    matrix_copied[point] = 0
    return matrix_copied

"""gruppe(objekt) verschieben"""

"""muster erkennen (wiederholung von farben)"""

"""objekt skalieren"""

"""objekt erkennen (default objekte angeben wie quadrat, rechteck, kreuz)"""


"""objekt duplizieren"""

"""wandinteraktion erkennen"""

"""pixel farbe ändern"""


"""objekt farbe ändern"""

"""racetrack connect shortest path (42oli)"""


