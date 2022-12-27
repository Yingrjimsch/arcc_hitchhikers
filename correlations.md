# Correlations
In this section it is briefly explained which correlations exist, how they are obtained and what the correlations method should return.

To get the best possible result the goal is to find as many correlations as possible. Because of that the Grids should be compared with each other as follows
1. X number of input and X number of output grids are generated from preprocessing and are given as parameters to the `correlate` function.
2. every input is compared with it's specific output and all other inputs
3. for every comparison a **correlation object** and a **grid object** should be returned.

## Example
As an example, the following input, output data are provided:

![Correlation Example](correlation_example.png)

These two two-dimensional arrays are mapped into grids and look like this after preprocessing:
//TODO new grids with objects per color
<table style="width: 100%; display: table">
<tr>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>

```json
{
    "raw": [
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,5,5,0,0,0,0],
        [0,0,0,0,0,1,1,0],
        [0,0,0,0,2,2,2,0],
        [0,0,0,0,0,0,0,0]
    ],
    "shape": [8,8],
    "sum": 24,
    "size": 13,
    "pixels": [
        ...
        {
            "color": 1,
            "coord": [1,2]
        },
        {
            "color": 1,
            "coord": [1,3]
        },
        {
            "color": 1,
            "coord": [1,4]
        },
		...
        {
            "color": 1,
            "coord": [2,2]
        },
        {
            "color": 1,
            "coord": [2,3]
        },
        {
            "color": 1,
            "coord": [2,4]
        },
        ...
        {
            "color": 5,
            "coord": [4,2]
        },
        {
            "color": 5,
            "coord": [4,3]
        },
        ...
        {
            "color": 1,
            "coord": [5,5]
        },
        {
            "color": 1,
            "coord": [5,6]
        },
		...
        {
            "color": 2,
            "coord": [6,4]
        },
        {
            "color": 2,
            "coord": [6,5]
        },
        {
            "color": 2,
            "coord": [6,6]
        },
        ...
    ],
    "colors": [0,1,2,5],
    "objects": [
        {
            "raw": [
                [1.0,1.0,1.0],
                [1.0,1.0,1.0]
            ],
            "shape": [2,3],
            "sum": 6.0,
            "size": 6,
            "pixels": [
                {
                    "color": 1,
                    "coord": [1,2]
                },
                {
                    "color": 1,
                    "coord": [1,3]
                },
                {
                    "color": 1,
                    "coord": [1,4]
                },
                {
                    "color": 1,
                    "coord": [2,2]
                },
                {
                    "color": 1,
                    "coord": [2,3]
                },
                {
                    "color": 1,
                    "coord": [2,4]
                }
            ],
            "colors": [1.0],
            "objects": null
        },
        {
            "raw": [
                [5.0,5.0]
            ],
            "shape": [1,2],
            "sum": 10.0,
            "size": 2,
            "pixels": [
                {
                    "color": 5,
                    "coord": [4,2]
                },
                {
                    "color": 5,
                    "coord": [4,3]
                }
            ],
            "colors": [5.0],
            "objects": null
        },
        {
            "raw": [
                [1.0,1.0]
            ],
            "shape": [1,2],
            "sum": 2.0,
            "size": 2,
            "pixels": [
                {
                    "color": 1,
                    "coord": [5,5]
                },
                {
                    "color": 1,
                    "coord": [5,6]
                }
            ],
            "colors": [1.0],
            "objects": null
        },
        {
            "raw": [
                [2.0,2.0,2.0]
            ],
            "shape": [1,3],
            "sum": 6.0,
            "size": 3,
            "pixels": [
                {
                    "color": 2,
                    "coord": [6,4]
                },
                {
                    "color": 2,
                    "coord": [6,5]
                },
                {
                    "color": 2,
                    "coord": [6,6]
                }
            ],
            "colors": [2.0],
            "objects": null
        }
    ]
}
```

</td>
<td>

```json
{
    "raw": [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,1,1,1],
	[0,0,0,0,0,1,1,1],
	[0,0,0,0,0,0,5,5],
	[0,0,0,0,0,0,2,2],
	[0,0,0,0,0,2,2,2]
    ],
    "shape": [8,8],
    "sum": 26,
    "size": 13,
    "pixels": [
        ...
        {
            "color": 1,
            "coord": [3,5]
        },
        {
            "color": 1,
            "coord": [3,6]
        },
        {
            "color": 1,
            "coord": [3,7]
        },
        ...
        {
            "color": 1,
            "coord": [4,5]
        },
        {
            "color": 1,
            "coord": [4,6]
        },
        {
            "color": 1,
            "coord": [4,7]
        },
        ...
        {
            "color": 5,
            "coord": [5,6]
        },
        {
            "color": 5,
            "coord": [5,7]
        },
        ...
        {
            "color": 2,
            "coord": [6,6]
        },
        {
            "color": 2,
            "coord": [6,7]
        },
        ...
        {
            "color": 2,
            "coord": [7,5]
        },
        {
            "color": 2,
            "coord": [7,6]
        },
        {
            "color": 2,
            "coord": [7,7]
        }
    ],
    "colors": [0,1,2,5],
    "objects": [
        {
            "raw": [
                [1.0,1.0,1.0],
                [1.0,1.0,1.0]
            ],
            "shape": [2,3],
            "sum": 6.0,
            "size": 6,
            "pixels": [
                {
                    "color": 1,
                    "coord": [3,5]
                },
                {
                    "color": 1,
                    "coord": [3,6]
                },
                {
                    "color": 1,
                    "coord": [3,7]
                },
                {
                    "color": 1,
                    "coord": [4,5]
                },
                {
                    "color": 1,
                    "coord": [4,6]
                },
                {
                    "color": 1,
                    "coord": [4,7]
                }
            ],
            "colors": [1.0],
            "objects": null
        },
        {
            "raw": [
                [5.0,5.0]
            ],
            "shape": [1,2],
            "sum": 10.0,
            "size": 2,
            "pixels": [
                {
                    "color": 5,
                    "coord": [5,6]
                },
                {
                    "color": 5,
                    "coord": [5,7]
                }
            ],
            "colors": [5.0],
            "objects": null
        },
        {
            "raw": [
                [0.0,2.0,2.0],
                [2.0,2.0,2.0]
            ],
            "shape": [2,3],
            "sum": 10.0,
            "size": 5,
            "pixels": [
                {
                    "color": 2,
                    "coord": [6,6]
                },
                {
                    "color": 2,
                    "coord": [6,7]
                },
                {
                    "color": 2,
                    "coord": [7,5]
                },
                {
                    "color": 2,
                    "coord": [7,6]
                },
                {
                    "color": 2,
                    "coord": [7,7]
                }
            ],
            "colors": [0.0,2.0],
            "objects": null
        }
    ]
}
```

</td>
</tr>
</table>


As a human can see pretty fast one part of the logic behind the input / output is it to move all the colored pixels to the bottom right corner. Another (not that clear) logic is to color all pixels below the gray line with one color and those above it with another color. In this case red and blue.

With these two grids the `correlation` function can be called. Which needs to compare both of these grids and get correlations as follows:
//TODO: matthias maybe you find more correlations we can use
* `sameShape = true` | ... no zooming, scaling, cropping happened ...
* `sameColorCount = false` | ... some kind of color swapping ...
* `sameSize = true` | ... no added pixels, removed pixels, duplicating (same amount non-background pixels)...
* `sameColor = true` | ... no added colors, recoloring of existing things ...
* `colorDiff = []` | same as `sameColor`in this case ...
* `sameObjects = [[[1,1,1],[1,1,1]],[[5,5]]]` | //TODO: WIP --> objects which are 100% the same
* `similarObjects = []` | //TODO: WIP --> objects which are similar by percentage
* `differentObjects` | //TODO: WIP --> objects which are not similar with anything at all
* `diff = [
 [0 0 0 0 0 0 0 0]
 [0 0 1 1 1 0 0 0]
 [0 0 1 1 1 0 0 0]
 [0 0 0 0 0 1 1 1]
 [0 0 5 5 0 1 1 1]
 [0 0 0 0 0 1 4 5]
 [0 0 0 0 2 2 0 2]
 [0 0 0 0 0 2 2 2]]` | ... pixels have been moved, the number 4 is interesting ...
 
 The other generated value will be a `Grid` object, which is an abstracton of the compared Grids as follows:
 ```json
 {
    "raw": [
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,5,5,0,0,0,0],
        [0,0,0,0,0,1,1,0],
        [0,0,0,0,2,2,2,0],
        [0,0,0,0,0,0,0,0]
    ],
    "shape": [8,8],
    "sum": ?,
    "size": 13,
    "pixels": [
        ...
        {
            "color": 1,
            "coord": ?
        },
        {
            "color": 1,
            "coord": ?
        },
        {
            "color": 1,
            "coord": ?
        },
		...
        {
            "color": 1,
            "coord": ?
        },
        {
            "color": 1,
            "coord": ?
        },
        {
            "color": 1,
            "coord": ?
        },
        ...
        {
            "color": 5,
            "coord": ?
        },
        {
            "color": 5,
            "coord": ?
        },
        ...
        {
            "color": ?,
            "coord": ?
        },
        {
            "color": ?,
            "coord": ?
        },
		...
        {
            "color": 2,
            "coord": ?
        },
        {
            "color": 2,
            "coord": ?
        },
        {
            "color": 2,
            "coord": ?
        }
    ],
    "colors": [0,1,2,5],
    "objects": [
        {
            "raw": [
                [1.0,1.0,1.0],
                [1.0,1.0,1.0]
            ],
            "shape": [2,3],
            "sum": 6.0,
            "size": 6,
            "pixels": [
                {
                    "color": 1,
                    "coord": ?
                },
                {
                    "color": 1,
                    "coord": ?
                },
                {
                    "color": 1,
                    "coord": ?
                },
                {
                    "color": 1,
                    "coord": ?
                },
                {
                    "color": 1,
                    "coord": ?
                },
                {
                    "color": 1,
                    "coord": ?
                }
            ],
            "colors": [1.0],
            "objects": null
        },
        {
            "raw": [
                [5.0,5.0]
            ],
            "shape": [1,2],
            "sum": 10.0,
            "size": 2,
            "pixels": [
                {
                    "color": 5,
                    "coord": ?
                },
                {
                    "color": 5,
                    "coord": ?
                }
            ],
            "colors": [5.0],
            "objects": null
        },
        {
            "raw": [
                [2.0,2.0,2.0]
            ],
            "shape": ?,
            "sum": ?,
            "size": ?,
            "pixels": [
                {
                    "color": 2,
                    "coord": ?
                },
                {
                    "color": 2,
                    "coord": ?
                },
                {
                    "color": 2,
                    "coord": ?
                }
            ],
            "colors": ?,
            "objects": null
        }
    ]
}
 ```
