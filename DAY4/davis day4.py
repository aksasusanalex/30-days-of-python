"""
Author:Davis Christy Robert
Date:26-11-2024
Description:Write a Python program that continuously asks the user for a number using
the input() function.The program should add the numbers entered
by the user and print the cumulative sum.
The loop should stop when the user enters a negative number. When the loop stops,
print the total sum of the positive numbers entered.
"""
number=float(input("enter the number:"))#we are inputing a variable to store the value from user
sum=0
while number>0: #check if the number given by the user is postive
    sum = sum + number
    number = float(input("enter the number:"))
print("the total sum of positive numbers is:",sum)#if negative number is added by the user this statement will be printed