# fit-bi-vmw-semestralka
Semestral project for the BI-VMW subject at the FIT CTU.

# About
This project was developed as a semestral assignment for the BI-VMW subject at the FIT CTU.
##Algorithms
###query function
Query functions are used to return the data from the database.
####naive algorithm
Compute overall score for every object by looking into each sorted list.
Return k objects with the highest overall score.
####fagin's algorithm
Sequentially access all the sorted lists in parallel until there are k objects that have been seen in all lists.
Perform random accesses to obtain the scores of all seen objects
Compute score for all objects and return the top-k
####top-k treshold
Set the threshold t to be the aggregate of the scores seen in this access.
Do random accesses and compute the scores of the seen objects.
Maintain a list of top-k objects seen so far.
Stop, when the scores of the top-k are greater or equal to the threshold.
Return the top-k seen so far.
###aggregation function
I have implemented 2 functions to get the best items based on the parameters selected by the checkbox.
- sum

This function sums the selected parameters.
- max

This function selects the highest value among selected parameters. This is the same as doing average of the elements since the ratings are normalised.

####speed comparison (number of accesses to the DB)
The top-k does clearly the least number of random accesses to the DB.
number of random accesses
Number of accesses to the DB on dataset containing 7 000 items.
speed comparison (time spent running)
These are the results on the dataset containing about 7000 elements. The y axis represents query time and the x axis the size of the query. The top-k algorithm is faster for the query of the size lower than the half of the dataset. Fagin's algorithm outperforms the top-k on the dataset presented in runtime comparison. The naive algorithm just sorts the array. When querying more than half of the database, it outperforms the top-k algorithm that starts to work like a heap sort but with added overhang. The test was run with a sum function using all 3 parameters.
Time comparison of different datasets using the sum aggregate function
dataset containing 7 000 elementsdataset containing 160 000 elements
From left to right: dataset containing 7 000 items, dataset containing 160 000 items.
Structure
The data is stored in 3 arrays each containing a KeyValue pair (car, value). Each array is sorted when the server starts or when a dataset is loaded. 