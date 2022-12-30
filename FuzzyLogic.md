# ARC - Fuzzy logic
## What is fuzzy logic?
[Fuzzy Logic](https://google.com/search?q=fuzzy+logic)

## Why fuzzy logic?
TODO// Why we decided to try to use fuzzy logic?

Fuzzy logic promises many similarities to a neural network. As we were thinking about using a NN anyway, we took a closer
look at fuzzy logic. One advantage of using fuzzy logic in comparison to a NN would be the comprehensibility of the process.
This would allow us to understand and debug our solution.
Even though the goal of the ARC-Challenge would be to get rid of the human thought process, it would not be possible in our opinion.
The tasks are built by humans, and therefore it would be a mistake to not include this kind of logic into the solving process.
By defining the rules for fuzzy logic discretely and by ourselves, we hoped to  be able to inject such human thought processes into it. 



## How could the preprocessing and our obtained correlations be used in fuzzy logic?
Thanks to the preprocessing, the correlations are possible to make, since the grids of the task are transformed into a grid-object.
What the preprocessing and the correlations are can be viewed more precisely in the md-files:
- [preprocessing](preprocessing.md)
- [correlations](correlations.md)

With help of the correlations, the rules for the fuzzy logic can be built.
The values of a correlation can be used as the input actions in the ruleset.
This means for example, the parameter colorDiff could be used to build different rules and create different outcomes based on its values.

## Our implementation/ implementation approaches of fuzzy logic
To define a ruleset, it is necessary to know what should be the input and output of the rule.

If (`variable_1` is `about value`) and (`variable_2` is `very high`) then `action`.

### ARC- Variables
### Define lingustic variables and terms 
TODO// What are our variables
#### Variables
* `detect(x,y)`
* `detect(y,x)`
* `detect(x,y,count)`
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
