# Correlations
In this section it is briefly explained which correlations exist, how they are obtained and what the correlations method should return.

To get the best possible result the goal is to find as many correlations as possible. Because of that the Grids should be compared with each other as follows
1. X number of input and X number of output grids are generated from preprocessing and are given as parameters to the `correlate` function.
2. every input is compared with it's specific output and all other inputs
3. for every comparison a **correlation object** and a **grid object** should be returned.

## Example
As an example, the following input, output data are provided:
//TODO Image
These two two-dimensional arrays are mapped into grids and look like this after preprocessing:
//TODO screenshot from Grids
<table>
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
    "size": 2,
    "pixels": [.
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
                [1,1,1],
                [1,1,1]
            ],
            "shape": [2,3],
            "sum": 6,
            "size": 2,
            "pixels": [
                {
                    "color": 1,
                    "coord": [2,3]
                },
                {
                    "color": 1,
                    "coord": [2,4]
                },
                {
                    "color": 1,
                    "coord": [2,5]
                },
                {
                    "color": 1,
                    "coord": [3,4]
                },
                {
                    "color": 1,
                    "coord": [3,3]
                },
                {
                    "color": 1,
                    "coord": [3,5]
                }
            ],
            "colors": [1],
            "objects": null
        },
        {
            "raw": [
                [5,5]
            ],
            "shape": [1,2],
            "sum": 10,
            "size": 2,
            "pixels": [
                {
                    "color": 5,
                    "coord": [5,3]
                },
                {
                    "color": 5,
                    "coord": [5,4]
                }
            ],
            "colors": [5],
            "objects": null
        },
        {
            "raw": [
                [0,1,1],
                [2,2,2]
            ],
            "shape": [2,3],
            "sum": 8.0,
            "size": 2,
            "pixels": [
                {
                    "color": 1,
                    "coord": [6,6]
                },
                {
                    "color": 1,
                    "coord": [6,7]
                },
                {
                    "color": 2,
                    "coord": [7,6]
                },
                {
                    "color": 2,
                    "coord": [7,5]
                },
                {
                    "color": 2,
                    "coord": [7,7]
                }
            ],
            "colors": [0,1,2],
            "objects": null
        }
    ]
}
```

</td>
<td>

```json
{
  "id": 5,
  "username": "mary",
  "email": "mary@example.com",
  "order_id": "f7177da"
}
```

</td>
</tr>
</table>