# ARC Challenge Team Hitchhikers
## Implementation Guidelines
1. Pick a functionality which is not implemented yet but intrests you and create a branch with feat/<functionality_name>
2. Implement the functionality locally as you wish in python.
3. Create some simple examples to verify it working properly and paste these "tests" into the .ipby file (with imports)
4. Create a merge request which has to be reviewed by minimum one other person
5. If everything is okay, thank you very much for your contribution!

## Definitions
In this section we try to find a common vocabulary for our technical solution, so everyone knows imediately what we talk about.
 
### Matrix indicies
Pixels have to be accessed as normal array ( i.e. input for pixel (x,y)=[y,x])
|  |  |  |  |
|--|--|--|--|
| [0,0] | [0,1] | [0,2] | [0,3] |
| [1,0] | [1,1] | [1,2] | [1,3] |
| [2,0] | [2,1] | [2,2] | [2,3] |
| [3,0] | [3,1] | [3,2] | [3,3] |

### How are boundaries handled
All Datapoints outside of our matrix should have the same value **10**


### Moonshots
* Wrap all matricies of the dimension n*m with a matrix of the dimension n+2 x m+2 where the "border" contains a boundary value
