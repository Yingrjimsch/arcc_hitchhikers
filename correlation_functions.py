import math

import numpy as np
import collections

from preprocessing import Pixel, Grid

FILENAME = 'correlation_functions'

"""
Compares the grid-objects from input with their output.
Returns a list of correlation-objects.
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
