'''Author: ALDA TREESA JOSY 
Date:17/11/2024
Description:Write a Python program that continuously asks the user for a number using the input() function. The program should add the numbers entered by the user and print the cumulative sum. The loop should stop when the user enters a negative number. When the loop stops, print the total sum of the positive numbers entered.'''



sum = 0

while True:
 
    number = float(input("Enter a number (negative number to stop):"))
    if number < 0:
        break 
    
    
    sum += number
print(f"The total sum of positive numbers is: {sum}")