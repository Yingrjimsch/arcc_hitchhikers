# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:07:33 2022

"""
import numpy as np
import matplotlib.pyplot as plt
import json
from json import JSONEncoder
from matplotlib import colors

cmap = colors.ListedColormap(['black', 'blue', 'red', 'green', 'yellow', 'grey', 'pink', 'orange', 'cyan', 'darkred'])

def printGrid(ax, data):
  ax.imshow(data, cmap=cmap, norm=colors.Normalize(vmin=0, vmax=9))
  ax.grid(which='major', axis='both', color='w', linewidth=1)
  ax.set_xticks(np.arange(-.5, len(data[0]), 1));
  ax.set_yticks(np.arange(-.5, len(data), 1));
  ax.set_yticklabels([])
  ax.set_xticklabels([])

def getSize(grid):
  return f'{len(grid)}x{len(grid[0])}'

def displayIO(grids):
  plt.rcParams['figure.figsize'] = [20, 5]
  fig, axs = plt.subplots(1,len(grids));
  fig.figsize=(12, 1)
  for i, grid in enumerate(grids):
    axs[i].set_title(f'{grid[1]}'); 
    printGrid(axs[i], grid[0]);
  plt.show()


class HitchHikersEncoder(JSONEncoder):
  """
    Used as follows:
    import json
    json.dumps(g, indent=4, cls=HitchHikersEncoder)
  """
  def default(self, obj):
    if isinstance(obj, np.integer):
      return int(obj)
    if isinstance(obj, np.floating):
      return float(obj)
    if isinstance(obj, np.ndarray):
      return obj.tolist()
    return obj.__dict__
  