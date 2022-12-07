# -*- coding: utf-8 -*-
import numpy as np
import collections


def connect_vertical_horizontal(matrix, pixel_src, pixel_dest):
    """
    Connection of two pixels via vertical - horizontal connection. Pixel receives the color of the start pixel
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

    if row_src < row_dest:
        #top-bottom
        for i in range(row_src, row_dest + 1):
            matrix[row_src][column_src] = color
            row_src += 1

        for j in range(column_src, column_dest - 1):
            matrix[row_dest][column_src + 1] = color
            column_src += 1
    else:
        #bottom-top
        for i in range(row_dest, row_src + 1):
            matrix[row_src][column_src] = color
            row_src -= 1

        for j in range(column_src, column_dest - 1):
            matrix[row_dest][column_src + 1] = color
            column_src += 1
    return matrix
