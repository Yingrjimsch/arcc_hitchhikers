# ARC - Results and Conclusions
The abstract reasoning challenge accompanied us for 14 weeks. Many ideas were exchanged in brainstorming phases, many things were tried out.
Even if we cannot present "THE" solution of the ARC in the end, we can still take many learnings from it.

## Results
As it was already reported in [fuzzy logic](fuzzy_logic.md) it turned out to be more difficult than expected to apply the fuzzy logic to the ARC problems.
Possible reasons for this are:
* It would be not a simple task to generate fuzzy logic rules automatically.
* To generate rules for each transformation is very costly and has to be done by hand.
* Static rules only apply on a small set of problems.
* Correlations as input values are not always sufficient.
* Not found a solution yet to set the correct order of the transformations (list of transformations instead of only one).

## Conclusions
To summarize the journey of tackling the abstract reasoning challenge there are multiple things to say.
Not only the task by itself but also investing a lot of time, findig new and good ideas and working in the group was challenging.
Even through we had a lot of fun working on it, the time was marked by highs and lows.
Unfortunately we didn't manage to upload a finished version and reached our goal to complete one task, but we are pretty happy with the
quality of what we have so far.

### Our positive experiences
* opportunity to be a part of a very interesting challenge
* learning about fuzzy logic, python, AI- libraries
* try to handle an unsolved task
* insights in neuroscience (by talk of Prof. Dr. Benjamin Grewe and thoughts of Francois Chollet)

### Our drawbacks
* very time intensive semester (other subjects)
* initial hurdle because of lack of experience
* no consistent availability by all members

### Our next steps
Since this year's ARC is over, and we unfortunately could not reach a complete solution
(reasons for this were already mentioned under "Results"), here are some next possible steps:
* **preprocessing**:
  * collision- detection (object - object / object - boundary)
* **correlations**:
  * compare input with input and output with output
  * adding more relevant attributes (see [more](correlations.md#additional-ideas-of-attributes))
* **fuzzy logic**:
  * implement basic ideas for evaluation
* elaborate search algorithm for finding transformations
