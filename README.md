
#  ARC Challenge Team Hitchhikers

##  Implementation Guidelines

1. Pick a functionality which is not implemented yet but intrests you and create a branch with feat/<functionality_name>

2. Implement the functionality locally as you wish in python.

3. Create some simple examples to verify it working properly and paste these "tests" into the .ipby file (with imports)

4. Create a merge request which has to be reviewed by minimum one other person

5. If everything is okay, thank you very much for your contribution!

  

##  Definitions

In this section we try to find a common vocabulary for our technical solution, so everyone knows imediately what we talk about.

###  Grid indicies

Pixels have to be accessed as normal array ( i.e. input for pixel (x,y)=[y,x])

| | | | |

|--|--|--|--|

| [0,0] | [0,1] | [0,2] | [0,3] |

| [1,0] | [1,1] | [1,2] | [1,3] |

| [2,0] | [2,1] | [2,2] | [2,3] |

| [3,0] | [3,1] | [3,2] | [3,3] |

  

###  How are boundaries handled

All Datapoints outside of our grid should have the same value **-1**

  

###  Pixels

A pixel defines one of the "fields" in a grid. It has two values which are defined as follows:

* color: *Number | Value of pixel between 0-9*

* location: *Array | x and y coordinates in the grid [y,x]*

  

###  Grid

A Grid is a two dimensional Array with shape NxM and it's values are defined as follows:

* shape: *Array | N and M of Array where N is vertically and M is horizontally [N,M]*

* size: *Number | Sum of pixels in the Grid (NxM)*

* pixels: *Array | Collection of all Pixels which the grid contains*

* colors: *Array | All color values of the pixels array collected*

* square: *Boolean | if array of shape NxN then 1 else 0*

* cluster: *Array | all clusters which can be found in the grid (objects)*

  
  

###  Correlations (Not Complete)

To get the best possible result we want to find as many correlations as possible. Because of that we want to compare two Grids with each other. After comparing them with a `compare` function we will get a collection of information, we can use as colleration factors:

* sameShape: *Boolean | do the grids have the same shape (grid1.shape - grid2.shape == 0?)*

* sameSize: *Boolean | do the grids have the same size (grid1.size - grid2.size == 0?)*

* sameColors: *Boolean | do the grids have the same colors in them?*

* colorDiff: *Array | all colors which are in one but not in the other grod*

* sameClusters: *Array | all clusters which can be found in both grids (with scaling or transformation)*

* diff: *Grid | a grid wich contains the difference between both (grid1 - grid2)*

  
  
  
  

###  Moonshots

* Wrap all matricies of the dimension n*m with a grid of the dimension n+2 x m+2 where the "border" contains a boundary value

  

##  Strategies

In this section we try to define our overall strategy(s) which we try to think through and implement with the given time we have.

  

Our first thought was it to create as much transformation functions like `rotate`, `flip` or `gravitate` and try to figure out a way for getting as fast as possible to our solution. In our mind we could "store" the used functions and reuse it on another known Input/Output set to double check if this is the right chaining of functions:
```mermaid
graph TD
start[get random transformation function] --> perform[perform transformation on Grid]
perform --> eval{evaluate similarity Input/Output}
eval -->|similarity is better| store{Store transformation function}
store -->|Input == Output| finish[Compare transformations with other examples]
store -->|Input != Output| start
```
as soon as we finished this process with all the examples we could compare the transformation chains with each other.

After little consideration we were not as convinced as at the beginning, that we would get anywhere with this approach. Because of that we started thinking about what we try to achieve. One very important piece in our thinking step was to listen to Francoise Chollet in [this Video](https://www.youtube.com/watch?v=jkBCyingDbk). As he created the ARC dataset we thought, that we need to understand what his vision of ARC is. Pretty much at the beginning he mentioned four different components that needed to be fullfilled to solve the ARC problem, namely Objectness, Agentness, Numbers, Geometry (OANG). Now wouldn't it be a good point to start from to create functions which are attuned to these concepts? It might help, it might not but it doesn't hurt.
### Objectness
A human environment is full of objects which change or interact with each other. In our environment (the NxM Grid) we should be possible to detect objects, compare them and get conclusions for the final result out of them.
#### Changing Objects
* Change Color
* Change Position
* Scale
* Rotate
* Flip
* Duplicate
* Split
* Extend
* ...
#### Interacting Objects
* Bounce off
* overlapp
* Outline
* Inline
* ...
### Agentness

### Numbers
* Compare / Subract Numbers
	* Size
	* Number of different colors
	* Number of pixel by color
	* Number of same objects
	* Number of same patterns
	* Dimension
	* ...
### Geometry
* Distance
* Scaling
* Orientation
* Object position
* ...
