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
    matrix_copied[point[0] + vector_transformed[0], point[1] + vector_transformed[1]] = color
    matrix_copied[point] = 0
    return matrix_copied

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

def gravitate_pixel(matrix, pixel):
    """
    Pixel following the gravitational force to the lowest possible field in the matrix
    :param matrix:
    :param pixel: which should be moved
    :return: matrix_changed
    """

    point = (pixel[1], pixel[0])
    row = point[0]
    column = point[1]
    matrix_changed = np.asarray(matrix)
    #print("before: \n", matrix_changed)
    color = matrix_changed[row][column]
    matrix_changed[row][column] = 0
    shape = matrix_changed.shape[0]
    for i in range(row+1, shape):
        if matrix[i][column] == 0:
            continue
        if matrix[i][column] != 0:
            point_new = (i-1, column)
            matrix_changed[point_new[0]][point_new[1]] = color
        else:
            point_new = (i, column)
            matrix_changed[point_new[0]][point_new[1]] = color
    return matrix_changed #add matrix.tolist() when convert to input type of matrix

def gravitate_object(matrix, pixel_group):
    """
    Group of Pixels (as object) following the gravitational force to the lowest possible fields in the matrix
    :param matrix:
    :param object: group of pixels which should be moved
    :return: matrix_changed
    """
    #print("before:\n", np.asarray(matrix))
    for pixel in pixel_group:
        matrix = gravitate_pixel(matrix, pixel)
    return matrix

def connect_diagonal(matrix, pixel_src, pixel_dest):
    """
    Diagonal connection of two points. Diagonal gets the color of the start pixel. 
    :param matrix:
    :param pixel_src
    :param pixel_dest
    :return: matrix_changed
    """
    print(np.asarray(matrix))
    point_src = (pixel_src[1],pixel_src[0])
    point_dest = (pixel_dest[1],pixel_dest[0])

    row_src = point_src[0]
    column_src = point_src[1]

    row_dest = point_dest[0]
    #column_dest = point_dest[1]
    color = matrix[row_src][column_src]
#bottom-top
    if row_src < row_dest:
        for i in range(row_src, row_dest-1):
            matrix[row_src + 1][column_src + 1] = color
            row_src += 1
            column_src += 1
#top-bottom
    else:
        for i in range(row_dest, row_src-1):
            matrix[row_src-1][column_src+1] = color
            row_src -=1
            column_src +=1
    return matrix

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