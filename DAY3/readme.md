Day 3:  If/Else Condition
Task: Use nested if/else statements to determine the type of triangle based on side lengths.
Problem Description:
You are given three integers representing the lengths of the sides of a triangle. You need to determine the type of triangle:

Equilateral: All three sides are equal.
Isosceles: Exactly two sides are equal.
Scalene: All three sides are different.
Invalid Triangle: The sides do not form a valid triangle (i.e., the sum of any two sides must be greater than the third side).
Input:
Three integers, a, b, and c, representing the lengths of the sides of a triangle.
Output:
A message indicating whether the triangle is Equilateral, Isosceles, Scalene, or Invalid.
Steps to Solve:
Check for Triangle Validity: A triangle is valid if the sum of any two sides is greater than the third side:


a+b>c

a+c>b

b+c>a
Determine the Type of Triangle:

If all sides are equal, it's Equilateral.
If exactly two sides are equal, it's Isosceles.
If all sides are different, it's Scalene.
