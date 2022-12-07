import os
import json
import numpy as np

BORDER_VALUE = 10
TRAINING_DATA_FOLDER_NAME = 'arcdata/evaluation';
fileNames = os.listdir(TRAINING_DATA_FOLDER_NAME);
fileNames = list(filter(lambda x: 'label' not in x, fileNames))

class Pixel:
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        
class Grid:
    def __init__(self, raw_grid):
        self.raw = raw_grid
        self.shape = raw_grid.shape
        self.sum = np.sum(raw_grid)
        self.size = len(np.nonzero(raw_grid!=BORDER_VALUE))
        self.pixels = [Pixel(color, i) for i,color in enumerate(raw_grid.flatten())]
        self.colors = np.unique(raw_grid)
        self.objects = find_objects(matrix)
        self.patterns = []

def evaluate_effectiveness_of_function(function):
    """
    The idea of this function is that a newly created library function can be tested directly on the evaluation data 
    (how many problems could be solved right away with this functionality).
    """
    solved_files = []
    #print(fileNames)
    for fileName in fileNames:
        with open(f'{TRAINING_DATA_FOLDER_NAME}/{fileName}', 'r') as file:
            data = json.loads(file.read())
            result = []
            #print(data)
            for i in data['train']:
                #print(i)
                result.append(np.array_equal(function(i['input']), np.array(i['output'])))
            if np.all(result):
                solved_files.append(fileName)
    return solved_files



def add_border(matrix):
    ''''Outline a grid so out of bounds exceptions can be minimized (nxm => n+2xm+2)'''
    return np.pad(matrix, 1, mode='constant', constant_values=BORDER_VALUE)

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


""""
This function is used by find_objects
"""
def get_neighbouring_pixels_recursively(matrix, pixel, seen_pos):
    if matrix[pixel[0], pixel[1]] == 0:
        return
    seen_pos.append(Pixel(matrix[pixel[0], pixel[1]], [pixel[0], pixel[1]]))
    for i in range(3):
        for j in range(3):
            d = Pixel(matrix[pixel[0]-1+i, pixel[1]-1+j], [pixel[0]-1+i, pixel[1]-1+j])
            if (all(obj.coord != d.coord for obj in seen_pos)) and d.color != 0:
                get_neighbouring_pixels_recursively(matrix, d.coord, seen_pos)
    return seen_pos

#1. Suche erste Zahl, welche nicht 0 oder 10 ist
#2. Get Neighbours rekursiv bis alle neighbours schon im objekt oder 0 oder 10 sind
#3. suche nächste Zahl, welche in keinem objekt vorkommt und nicht 0 ist
def find_objects(matrix):
    cluster = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0 or (cluster and any([i,j] == obj.coord for obj in np.concatenate(np.asarray(cluster, dtype=object)).ravel())):
                continue
            d = get_neighbouring_pixels_recursively(matrix, [i, j], [])
            cluster.append(np.array(d))
    return cluster