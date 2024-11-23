Day 9: List Operations and Nested Loops
Task: Perform operations on lists, including nested loops to handle lists of lists.
Description:
Python provides a variety of operations to manipulate lists. You can modify items, add new items, or even combine lists. In this task, you will use a nested loop to iterate through a list of lists (a 2D list) and perform operations on the inner lists.

Example 1: Working with List Operations
python
Copy code
# Creating a list of mixed data types
my_list = [10, "Hello", 3.14, True]

# Adding an item to the list
my_list.append("New Item")

# Removing an item from the list
my_list.remove(3.14)

# Accessing an element by index
print("Second item:", my_list[1])

# Printing the updated list
print("Updated list:", my_list)
Output:

sql
Copy code
Second item: Hello
Updated list: [10, 'Hello', True, 'New Item']
Explanation:
append(): Adds a new item to the end of the list.
remove(): Removes the first occurrence of a specific item.
Lists are dynamic, so you can add or remove elements as needed.
