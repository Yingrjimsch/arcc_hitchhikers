import math

import numpy as np
import collections

from preprocessing import Pixel, Grid

FILENAME = 'correlation_functions'

"""find and return the a grid of neighbouring pixels with selected pixel in center"""
# def get_pixel_neighbours(matrix, pixel):
#     neighbours = np.zeros((3,3))
#     for i in range(3):
#         for j in range(3):
#             neighbours[i, j] = matrix[pixel[0]-1+i, pixel[1]-1+j]
#     return neighbours

# def equal_matrix_dimensions(matrix_one, matrix_two):
#     """
#     Checks if dimensions of input matrix and output matrix are equal
#     :param array_one:
#     :param array_two:
#     :return: boolean
#     """
#
#     matrix_one_new = np.asarray(matrix_one)
#     matrix_two_new = np.asarray(matrix_two)
#     return matrix_one_new.shape == matrix_two_new.shape

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
(dinge die nicht gleich sind werden mit einem Placeholder 'NaN' ausgefüllt) 
"""
def correlate(preprocessed_task):
    correlations = []
    # Create List of correlations between each input and output
    for i in range(len(preprocessed_task)):
        corr = Correlation(preprocessed_task[i][0], preprocessed_task[i][1])
        correlations.append(corr)
    return correlations


class Correlation:
    def __init__(self, grid1: Grid, grid2: Grid):
        self.grid1 = grid1
        self.grid2 = grid2
        self.sameShape = grid1.shape == grid2.shape
        self.sameColorCount = self.color_count(grid1) == self.color_count(grid2)
        self.sameSize = grid1.size == grid2.size
        self.sameColors = np.all(grid1.colors == grid2.colors)
        color_diff_prep = self.color_count(grid1)
        color_diff_prep.subtract(self.color_count(grid2))
        self.colorDiff = color_diff_prep
        self.sameObjectsIdpPosFixCol = self._get_same_objects_idp_pos_fix_col()
        self.sameObjectsFixPosFixCol = self._get_same_objects_fix_pos_fix_col()
        self.sameObjectsFixPosIdpCol = self._get_same_objects_fix_pos_idp_col()
        self.sameObjectsIdpPosIdpCol = self._get_same_objects_idp_pos_idp_col()
        self.diff = grid1.raw - grid2.raw

    """Counter of different colors"""
    def color_count(self, grid: Grid):
        pixels = grid.getPixels()
        counter = collections.Counter()
        for pixel in pixels:
            counter[pixel.color] += 1
        return counter

    def _get_same_objects_idp_pos_fix_col(self):
        objects1 = self.grid1.objects
        objects2 = self.grid2.objects
        same = []

        for o1 in objects1:
            for o2 in objects2:
                if np.array_equal(o1.raw, o2.raw):
                    same.append(o1)
                    break
        return same

    def _get_same_objects_fix_pos_fix_col(self):
        objects1 = self.grid1.objects
        objects2 = self.grid2.objects
        same = []

        for o1 in objects1:
            for o2 in objects2:
                if np.array_equal(o1.raw, o2.raw):
                    is_same = True
                    for i, pixel in enumerate(o1.pixels):
                        if not np.array_equal(pixel.coord, o2.pixels[i].coord):
                            is_same = False
                    if is_same:
                        same.append(o1)
        return same

    def _get_same_objects_fix_pos_idp_col(self):
        objects1 = self.grid1.objects
        objects2 = self.grid2.objects
        same = []

        for o1 in objects1:
            for o2 in objects2:
                if o1.raw.shape == o2.raw.shape:
                    same_pos = True
                    for i, pixel in enumerate(o1.pixels):
                        if not np.array_equal(pixel.coord, o2.pixels[i].coord):
                            same_pos = False
                    if same_pos:
                        same.append(o1)
        return same

    def _get_same_objects_idp_pos_idp_col(self):
        objects1 = self.grid1.objects
        objects2 = self.grid2.objects
        same = []

        for o1 in objects1:
            for o2 in objects2:
                if o1.raw.shape == o2.raw.shape:
                    same.append(o1)
                    break

        return same
