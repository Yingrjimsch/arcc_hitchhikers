# Tobi's eskapaden

## Per-Task Training
One approach that was initially discussed was the possibility on training a model on each task instead of having one algorythm to solve all of them.

### Idea prerequisites

The basic idea here is that you have a neural network. This network represents a function in a classic Ai sense. If you have for example 3 inputs and 3 correct outputs, this network is able to learn a mapping (function) between those inputs and outputs (depending on if each layer can be derivated, as far as I understood mathematically).

#### Simple Task Examples

Task1
||||
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

Solution1
||||
|---|---|---|
| 0 | 1 | 0 |
| 0 | 0 | 0 |
| 0 | 0 | 0 |

Task2
||||
|---|---|---|
| 0 | 0 | 0 |
| 0 | 0 | 1 |
| 0 | 0 | 0 |

Solution2
||||
|---|---|---|
| 0 | 0 | 1 |
| 0 | 0 | 0 |
| 0 | 0 | 0 |

Task3
||||
|---|---|---|
| 0 | 0 | 0 |
| 0 | 0 | 0 |
| 1 | 0 | 0 |

Solution3
||||
|---|---|---|
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 0 | 0 |

-> Here the logic is that if there is a 1, it moves upwards.

A network is created with input grid 3x3 and output grid 3x3. The layers in between may be any kinds of layers.

If you train the network on these three problems only, the problem now is that this network will overfit.

Assumption 1: If the NN finds a solution to all three tasks, it can correctly solve the last task.

This assumption is wrong:

For example, the network would, after training, "contain" the human readable logic:
If there is a 1 on index (3,2), move it to index (3,1).
If there is a 1 on index (2,3), move it to index (2,2).
If there is a 1 on index (1,3), move it to index (1,2).

The model is overfitted. If you run this on a new task, it won't solve it.

The logic that we want is different though -> it would need to be:
If there is a 1, move the index of it up one row.

-> The correct logic is more general.

Assumption 2: If we find the most general solution that can solve a set of problems, it must be able to solve the task.

We seem to need a way to be able to find out if this code is general or not.

### Kernel thoughts with example

A convoluted layer in a CNN has a kernel that modifies the input. With image stuff, this can be used to find edges. For our example here, using a kernel that looks like this:

||
|---|
| 0 |
| 1 |

would be able to solve the task correctly in a single layer.


### Functions to reduce complexity (Fuzzy Logic)

If you were to just try possible permutations on the input to get to the output, you would probably never arrive at a solution because there are too many permutations one can do.

Because we as humans have reasoning, we know for example that a pixel could act like an object with gravity and fall down onto a floor. A computer doesn't. Which is why we want to help the computer by having these kinds of functions predefined.

If we have a limited amount of those functions, we can try to run the functions with random parameters to arrive at a set of function calls that arrive at the solution.

FindObject(1) -> moveObject(up, 1)

In my mind, to solve all ARC tasks, we would need to be able to create a domain language that contains all of the possible ways to interpret and modify the grid. 



