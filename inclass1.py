"""
Class: CS230--Section 3
Name: Taice Brenner
Description:
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("Booleans")
print(True)
print(False)
print(type(True))
print(type(False))
print("\"Hello Python\"")

number2 = 125
cost = 2.50
price = cost * number2
tax = price * .05
total = price + tax
print("The total price is", total)

var1 = True
var2 = True
var3 = False
print("Both values are", var1 and var2)
print("One of the variables is", var2 or var3)

sentence = "I love Python programming"
print('p' in sentence)
print('p' not in sentence)

SALES_TAX = .0625
number2 = int(input("Enter the number of items you would like: "))
cost = float(input("Enter the cost of items you would like: "))
price = cost * number2
tax = price * SALES_TAX
total = price + tax
print("The total price is: ", total)

import math
print(math.pi)

print()
print(math.sqrt(4))

print()
print(math.pow(2,3))

import math
radius = int(input("Enter the radius: "))
area = math.pi * (radius**(2))
circumference = 2 * math.pi * radius
print("The circumference is : ")
print("The area is: ")

number = int(input("Enter the first number: "))
number = int(input("Enter the second number: "))
number = int(input("Enter the third number: "))
