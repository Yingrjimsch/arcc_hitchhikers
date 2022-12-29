# ARC - FuzzyLogic
## Why FuzzyLogic?
TODO// Why we decided to use FuzzyLogic?

## How do we use our preprocessing and our obtained correlations in FuzzyLogic?
TODO// Explanation

## Our implementation/ implementation approaches of FuzzyLogic
TODO// Sequence of FuzzyLogic in connection with ARC problems

### ARC- Variables
### Define lingustic variables and terms 
TODO// What are our variables
#### Variables
* `decect(x,y)`
* `decect(y,x)`
* `decect(x,y,count)`
* `dim(x,y)` -> possible values -1, 0, 1
* `countPixel(x,y)`
* `countPixelColor(x,y)`
* `background(x,y)`
* `isObjectIn(x,y)`
* `isObjectIn(y,x)`
* `isObjectInColor(x,y,color)`
* `isObjectInColor(y,x,color)`
* `isObjectInMultiColor(y, x)`
* `isObjectInLocation(x, y)`
* `detectObj(y,x,count)`
* `isObjectBigObj(y,x)`
* `isObjectBigObj(y,x)`
* `isObjectBigObj(y,x,color)`
* `isObjectBigObj(y,x,color)`
#### Actions
* `move()`
* `rotate()`
* `coloring()`
* `connect()`
* `flip()`
* `multiply()`
### Construct membership functions for them
TODO// What are our membership functions? 
### Construct knowledge base of rules
TODO// What are our rules? 
* `if detect(x,y) then...`
* `if detect(y,x) then...`
* `if detect(x,y,count) then...`
* `if detect(y,x,count) then...`
* `if dim(y,x) then...`

## ARC- Fuzzification
### Convert crips data into fuzzy data sets using membership functions

## ARC- Fuzzy- Inferences
### Evaluate rules in the rule base
### Combine results from each-rule

## ARC- Defuzzification
### Convert output data into non-fuzzy values
