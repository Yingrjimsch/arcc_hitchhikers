import numpy as np
import correlation_functions as cf
import helper as hlp

import numpy as np
BORDER_VALUE = -1
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
        self.objects = []
        self.patterns = []
        
pixel = Pixel(1, [1,2])
pixel2 = Pixel(1, [1,2])
grid = np.asarray([[1, 2, 1], [2, 2, 2], [3, 1, 1]])
g = Grid(grid)



