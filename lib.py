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


"""Funktion extrahiert alle gleichen Farben, returnt matrizen pro farbe (vonwareb)""" 
def matrix_per_color(matrix):
    """
    Extract all equal color pixels from a matrix and return one matrix per color
    :param matrix:
    :return: result_matrices
    """
    matrix = np.asarray(matrix).flatten()
    result_matrices = []
    for i in range(1, 9):
        matrix_copy = np.copy(matrix == i)
        matrix_result = np.zeros(matrix_copy.shape)
        if np.sum(matrix_copy == True) > 0:
            for j in range(matrix_copy.size):
                if matrix_copy[j]:
                    matrix_result[j] = i
            result_matrices.append(matrix_result)
    return result_matrices

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

"""gruppe(objekt) verschieben (vonwareb)"""
def move_object(matrix, colorobject, vector):
    """
    Moves an object by the specified vector
    :param matrix:
    :param colorobject:
    :param vector:
    :return: changed matrix
    """
    np_matrix = np.asarray(matrix)
    for pixel in colorobject:
        move_pixel(np_matrix, pixel, vector)
    return np_matrix

"""muster erkennen (wiederholung von farben)"""

"""objekt skalieren"""

"""objekt erkennen (default objekte angeben wie quadrat, rechteck, kreuz)"""


"""objekt duplizieren"""

"""wandinteraktion erkennen"""

"""pixel farbe ändern (vonwareb)"""
def change_color_pixel(matrix, pixel, color):
    """
    changes color pixel (value in matrix)
    :param matrix:
    :param point: as [x,y]
    :param color: value from 1 to 9
    :return: matrix with changed pixel
    """
    point = (pixel[1], pixel[0])
    matrix = np.asarray(matrix)
    #print("before: \n", matrix)
    matrix[point] = color
    #print("after: \n", matrix)
    return matrix


"""objekt farbe ändern (vonwareb)"""
def change_color_object(matrix, colorobject, color):
    """
    changes color of a whole object in a matrix
    :param matrix:
    :param object:
    :param color:
    :return:
    """

    for pixel in colorobject:
        change_color_pixel(matrix, pixel, color)
    return matrix

"""racetrack connect shortest path (42oli)"""


