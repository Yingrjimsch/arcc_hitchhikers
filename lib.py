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
        
"""!!!!!!!!Wrapper für matrizen!!!!!!!!"""

"""Funktion extrahiert alle gleichen Farben, returnt matrizen pro farbe"""

"""nachbaren erkennen (zurückgeben) pro pixel"""

"""prüfen dass nachbaren ähnliche farbe haben"""

"""prüfen ob array dimensionen gleich sind"""

"""prüfen ob farb summe gleich bleibt"""

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


