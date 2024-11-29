# Day 15:  Unique Numbers

## Problem Description:

In this task, you will work with sets in Python to handle a collection of unique numbers. You need to:

1. Create a set of numbers.
2. Add new numbers to the set.
3. Remove numbers from the set.
4. Check if a specific number exists in the set.

### Example:

#### Input:

```python
numbers = {1, 2, 3, 4, 5}
Functions:
add_number(numbers, number):

Adds a number to the set if it is not already present.
remove_number(numbers, number):

Removes a number from the set.
check_number(numbers, number):

Checks if a specific number exists in the set.
unique_numbers(numbers):

Returns the list of all unique numbers in the set.
Expected Output:
After add_number(numbers, 6), the set should have the number 6.
After remove_number(numbers, 3), the set should no longer have 3.
After check_number(numbers, 4), the result should be True.
After unique_numbers(numbers), the result should be the list of unique numbers.
