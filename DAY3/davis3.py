"""Author: Davis Christy Robert
Date:24/01/2024
Description: If/Else Condition Task: Use nested if/else statements to
determine the type of triangle based on side lengths.
Problem Description: You are given three integers representing the
lengths of the sides of a triangle.
You need to determine the type of triangle:"""
a=int(input("enter the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c and a==c:
        print("This triangle is an Equilateral Triangle")

    elif a==b or b==c or c==a:
        print("This triangle is an Isosceles Triangle")

    else:
        print("The triangle is  an Scalene Traingle ")
else:
        print("its an invalid triangle")

