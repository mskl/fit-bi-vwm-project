# fit-bi-vmw-semestralka
Semestral project for the BI-VMW subject at the FIT CTU.

# About
This project was developed as a semestral assignment for the BI-VMW subject at the FIT CTU.

## Algorithms

### query function
Query functions are used to return the data from the database.

#### naive algorithm
Compute overall score for every object by looking into each sorted list.
Return k objects with the highest overall score.

#### fagin's algorithm
Sequentially access all the sorted lists in parallel until there are k objects that have been seen in all lists.
Perform random accesses to obtain the scores of all seen objects
Compute score for all objects and return the top-k
#### top-k treshold
Set the threshold t to be the aggregate of the scores seen in this access.
Do random accesses and compute the scores of the seen objects.
Maintain a list of top-k objects seen so far.
Stop, when the scores of the top-k are greater or equal to the threshold.
Return the top-k seen so far.
### aggregation function
I have implemented 2 functions to get the best items based on the parameters selected by the checkbox.
#### sum
This function sums the selected parameters.
#### max
This function selects the highest value among selected parameters. This is the same as doing average of the elements since the ratings are normalised.
