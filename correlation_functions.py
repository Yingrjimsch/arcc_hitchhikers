import numpy as np
import collections

FILENAME = 'correlation_functions'

"""find and return the a grid of neighbouring pixels with selected pixel in center"""
def get_pixel_neighbours(matrix, pixel):
    neighbours = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            neighbours[i, j] = matrix[pixel[0]-1+i, pixel[1]-1+j]
    return neighbours

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

def same_shape_diff(grid_one, grid_two):
    return abs(np.asarray(grid_one) - np.asarray(grid_two))
    

def get_pixel_neighbours_recursive(matrix, pixel, seen_pos):
    if matrix[pixel[0], pixel[1]] == 0:
        return
    seen_pos.append(Pixel(matrix[pixel[0], pixel[1]], [pixel[0], pixel[1]]))
    for i in range(3):
        for j in range(3):
            d = Pixel(matrix[pixel[0]-1+i, pixel[1]-1+j], [pixel[0]-1+i, pixel[1]-1+j])
            if (all(obj.coord != d.coord for obj in seen_pos)) and d.color != 0:
                get_pixel_neighbours_recursive(matrix, d.coord, seen_pos)
    return seen_pos

#1. Suche erste Zahl, welche nicht 0 oder 10 ist
#2. Get Neighbours rekursiv bis alle neighbours schon im objekt oder 0 oder 10 sind
#3. suche nächste Zahl, welche in keinem objekt vorkommt und nicht 0 ist
def find_objects(matrix, size):
    #print(matrix)
    cluster = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0 or (cluster and any([i,j] == obj.coord for obj in np.concatenate(np.asarray(list(map(Grid.getPixels, cluster)), dtype=object)).ravel())):
                continue
            d = get_pixel_neighbours_recursive(matrix, [i, j], [])
            if math.ceil(np.asarray(d).size / 2) * 2 == size:
                return
            raw_child = normalize(d)
            cluster.append(Grid(raw_child, d))
    return cluster

def normalize(pixels):
    x = max(list(map(Pixel.getX, pixels))) - min(list(map(Pixel.getX, pixels)))
    y = max(list(map(Pixel.getY, pixels))) - min(list(map(Pixel.getY, pixels)))
    raw = np.zeros((x + 1,y + 1))
    
    for p in pixels:
        raw[(p.getX() - min(list(map(Pixel.getX, pixels))), p.getY() - min(list(map(Pixel.getY, pixels))))] = p.color
    return raw



"""
Vergleicht die Grid Objekte auf ihre properties
Returnt ein Grid Objekt mit allen korrelationen
(dinge die nicht gleich sind können mit einem Placeholder ausgefüllt werden) 
"""
def correlate(m1, m2):
    return