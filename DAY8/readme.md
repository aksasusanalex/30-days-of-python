Day 8: Combining Lists and Using for Loops
Task: Combine two lists and print the combined list using a for loop.
Description:
In this task, you will work with two separate lists and combine them into one list. After combining, you will use a for loop to print each element of the combined list.

You will:

Create two separate lists.
Use the extend() method to combine both lists into one.
Print the combined list using a for loop.
Example Code Template:
python
Copy code
# List 1
list1 = ["apple", "banana", "cherry"]

# List 2
list2 = ["date", "elderberry", "fig"]

# Combine the two lists using extend()
list1.extend(list2)

# Print each item from the combined list
for item in list1:
    print(item)
Instructions:
Create two separate lists. You can include any type of items, such as strings, numbers, or even other lists.
Use the extend() method to add all items from the second list (list2) into the first list (list1).
Use a for loop to print out each item from the now-combined list.
Example Output (if you combine fruit lists):
bash
Copy code
apple
banana
cherry
date
elderberry
fig
