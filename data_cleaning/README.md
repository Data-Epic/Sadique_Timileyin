## Missing Data
The First Step I took was getting the data from the Google sheet, then I converted it into a CSV file to access the null values.

The total number of missing values in the data set is 170,137 null values which l replaced with 'MISSING'

Formatted the date columns to assign them to datetime datatype.


## Inconsistent Data

I found inconsistent data in the Date column and the weight column.

I dealt with the inconsistency using the replace and split function in pandas 

I found inconsistent data in the Time column I tried my best, but it was too messed up