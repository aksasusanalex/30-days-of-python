Day 3: Arithmetic Operators #1
Task: Perform basic arithmetic operations using two user inputs.
Description:
In this task, you will use arithmetic operators to perform calculations based on user input. The program should ask for two numbers and then perform addition, subtraction, multiplication, and division.

Example:

python
Copy code
# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"

# Printing the results

Enter the second number: 5
The sum of 10.0 and 5.0 is: 15.0
The difference between 10.0 and 5.0 is: 5.0
The product of 10.0 and 5.0 is: 50.0
The quotient of 10.0 and 5.0 is: 2.0
