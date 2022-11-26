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
        self.shape = raw_grid.shape
        self.size = np.sum(raw_grid)
        self.pixels = [Pixel(color, i) for i,color in enumerate(raw_grid.flatten())]
        self.colors = np.unique(raw_grid)

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