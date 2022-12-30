# ARC - Fuzzy logic
## Why fuzzy logic?

Fuzzy logic promises many similarities to a neural network (NN). As we were thinking about using a NN anyway, we took a closer
look at fuzzy logic. One advantage of using fuzzy logic in comparison to a NN would be the comprehensibility of the process.
This would allow us to understand and debug our solution.
Even though the goal of the ARC-Challenge would be to get rid of the human thought process, it would not be possible in our opinion.
The tasks are built by humans, and therefore it would be a mistake to not include this kind of logic into the solving process.
By defining the rules for fuzzy logic discretely and by ourselves, we hoped to  be able to inject such human thought processes into it. 


## How could the preprocessing and our obtained correlations be used in fuzzy logic?
Thanks to the preprocessing, the correlations are possible to make, since the grids of the task are transformed into a grid-object.
What the preprocessing and the correlations are, can be viewed more precisely in the md-files:
- [preprocessing](preprocessing.md)
- [correlations](correlations.md)

With help of the correlations, the rules for the fuzzy logic can be built.
The values of a correlation can be used as the input actions in the ruleset.
This means for example, the parameter `colorDiff` could be used to build different rules and create different outcomes based on its values.

## Different Approaches for fuzzy model
In general, we had the fuzzy logic in mind, to evaluate which actions need to be performed, to reach the end state.
For that, our model will take one input-grid and the corresponding output-grid, to get the correlations. From these correlations, different rule-sets can be built.

To define a rule-set, it is necessary to know what should be the input and output of the rule.
A  rule can look something like this:

If (`variable_1` is `about value`) and (`variable_2` is `very high`) [and... ]* then `output` is `action`.

Our `variables` are defined in the [correlations](correlations.md#correlation-attributes), which are simply the different attributes of a correlation-object.

For our output of the fuzzy logic, we had different ideas:

### Idea 1
One idea was, that the output of the fuzzy logic will be the truth-values of the predefined [actions](README.md#implemented-methods).

To gain the necessary actions to perform, the most true values will be used. 

#### Problem
Different actions need to be performed in specific orders.
Therefore it has to be figured out the order of the actions, which needs to be tested more or less by brute-force, until one specific order of those selected actions result in the correct output.

### Idea 2
To improve Idea 1, we had the idea to chain those "generalized" action to more specific rules, to perform a precise action.
For example a rule would tell, an action should be `move`, then this will be passed into another rule to perform an action `move_left`.

If (`variable_1` is `about value`) and (`variable_2` is `very high`) [and... ]* then `temp_output1` is `move`.
</br>
If (`temp_output1` is `move`) and (`variable_3` is `low`) [and... ]* then `temp_output2` is `move_left`.
</br>
If (`temp_output2` is `move_left`) and (`variable_4` is `close to 10`) [and... ]* then `output` is `move_left_amount`.

From the attribute `move_left_amount` we should have a guessed value, how far the object should be moved to the left.

#### Problem
Unfortunately, this solution requires a tremendous amount of rules, which we were not able to implement due to our restricted time capacity.

Probably we also think for some actions, it is not that easy to define rules from correlations alone. For example a `bounce_from_wall` is not possible to see with a rule just by comparing in- and output.
Here, the human thought-process needs to be taken into consideration. 

## Defuzzification
With the ideas listed above, it should be possible to evaluate *one action* to perform.
Unfortunately, an ARC-Problem will never be solved simply by performing one specific action on an object.
It needs a *sequence of actions*.

To get an evaluation about the order of actions to perform, we have also considered different options:

### Idea 1
One idea to simply choose the order with the actions sorted of the truth-values of the fuzzy logic.

For example with this output: <br>
`output = {"move": 0.767, "flip": 0.231, "color": 0.653}` <br>
the order would be `move`, `color` and then `flip`.

The problem with that idea is, that it is most likely not accurate to get an order of actions based on their truth values, since all of them were only executed alone and not in a chain.
This can result in a totally different outcome.


### Idea 2
A different approach which is more plausible, is by adding some more output actions, which store a truth value of how plausible it is, that this action is executed first or second.

An output could look like that: <br>
`output = {"move": 0.767, "move_first": 0.62, "move_second": 0.12 "flip": 0.231, "flip_first": 0.23, "flip_second": 0.73, "color": 0.653}` <br>
the order would be `move`, `flip` and then `color` (since it is not relevant, when color is needed to be executed, it does not have an "order"-attribute.)

