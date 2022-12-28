# ARC - Preprocessing 
This, very important, part is performed for each ARC task in order to extract as much information as possible. The more information that can be collected and combined, the easier it will be to identify patterns, repetitions and ultimately task logics.


<p align="center">
  <img src="https://media.tenor.com/QfgUqeUeB6kAAAAM/monsieur-propre-mr-propre.gif" />
</p>


Most of the Tasks from the ARC Dataset consist of around three examples and one task with an unknown output. Every example task consists of a two dimensional array with inputs (numbers 0-9) and a two dimensional array with outputs (also numbers 0-9)
These arrays are read in and converted to `Grid` objects, which have following attributes:

 - `raw` ➔ the raw 2 dimensional array of numbers (normalized to start at 0,0)
 - `shape` ➔ the dimensions x,y of the grid e.g. (8,8)
 - `sum` ➔ the summed up value of all numbers in `raw`
 - `size` ➔ the number of numbers which are not background, as for now which are not 0
 - `pixels` ➔ the raw grid as pixel objects
	 - `coord` ➔ the **absolute** x and y coordinates
	 - `color` ➔ number between 0 and 9
 - `colors` ➔ unique array of occurring numbers
 - `objects` ➔ an array with all detected objects in the grid. (see [Object Detection](#Object-Detection))

### Object Detection
Detecting objects is a key part of the challenge, because most of the logics depend on transformation, collision, translation, counting etc. of objects. After some research and multiple iteration where it was tried to recursively find subobjects, it was decided to start simpler.
It is achieved by clustering all numbers by color and neighbours with help of skimage's 2-connectivity. [^1]
```
2-connectivity

[ ]  [ ]  [ ] 
   \  |  /    
[ ]--[x]--[ ] 
   /  |  \    
[ ]  [ ]  [ ]
```
[^1]: https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.label
