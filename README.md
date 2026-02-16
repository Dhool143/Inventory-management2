# Inventory Management System

## Problem Description
This project implements a function called `duplicateZeros` that modifies
an inventory array in place.

For every occurrence of `0` (representing out-of-stock products),
the function duplicates the zero and shifts the remaining elements to the right.
The array length remains fixed.



## Example

Input:
[4,0,1,3,0,2,5,0]

Output:
[4,0,0,1,3,0,0,2]



## Approach

- Count number of zeros
- Use two pointers
- Traverse backward to avoid overwriting values
- Only write inside valid array bounds



## Time Complexity
O(n)

## Space Complexity
O(1)



