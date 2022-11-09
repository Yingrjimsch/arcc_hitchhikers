# -*- coding: utf-8 -*-
import numpy as np

def rotate_clockwise(matrix):
    return np.array(list(zip(*(reversed(matrix)))))

def rotate_anticlockwise(matrix):
    return np.array(list(zip(*matrix))[::-1])

def rotate_180(matrix):
    return rotate_clockwise(rotate_clockwise(matrix))

def flip_horizontally(matrix):
    return np.array(list(reversed(matrix)))

def flip_vertically(matrix):
    return rotate_anticlockwise(flip_horizontally(rotate_clockwise(matrix)))

"""
def rotate(matrix, move):
    if move == 0:
        return matrix
    elif move == 1:
        return mirror(matrix)
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
        return mirror(matrix)
    elif move == 2:
        return rotate_anticlockwise(matrix)
    elif move == 3:
        return rotate_clockwise(matrix)
    else:
        print('This is not possible')
"""
        
"""!!!!!!!!Wrapper für matrizen!!!!!!!!"""


"""Funktion extrahiert alle gleichen Farben, returnt matrizen pro farbe"""

"""Rand Hinzufügen (nxm => n+2xm+2) (kochma2)"""

"""nachbaren erkennen (zurückgeben) pro pixel (kochma2)"""

"""prüfen dass nachbaren ähnliche farbe haben"""

"""prüfen ob array dimensionen gleich sind  (vonwareb)"""

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


