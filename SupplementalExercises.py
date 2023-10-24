"""
Class: CS230--Section 3
Name: Taice Brenner
Description: Supplemental Exercises Data Types
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#Exercise 1

Celsius = float(input("Enter the Celsius temperature (enter as a decimal please): "))

Fahrenheit = float(((9/5) * Celsius) + 32)
Kelvin = float(Celsius + 273.15)

print("The Celsius temperature of {0} is ".format(Celsius), Fahrenheit, "degrees Fahrenheit")
print("The Celsius temperature of {0} is ".format(Celsius), Kelvin, "degrees Kelvin")


#Exercise 2

Hours = 40
Hourly = float(input("Enter the hourly wage: "))
Overtime = int(input("Enter the overtime hours: "))
Weekly = (Hours * Hourly) + ((1.5 * Hourly) * Overtime)

print("The employee's weekly pay is $", Weekly)

#Exercise 3

number = int(input("Enter a four-digit number: "))
thousand = number//1000
hundred = (number // 100) % 10
ten = (number//10) % 10
one = number % 10
sum = thousand + hundred + ten + one
print("The sum of the digits in {0} is".format(number), sum)

#Exercise 4

slices = 32
guests = int(input("Number of guests: "))
extra = slices % guests
opt1 = int(slices / guests)
opt2 = slices / guests
print("Option 1: {0} slices each,".format(opt1), "{0} left over".format(extra))
print("Option 2: {0} slices each".format(opt2))

#Exercise 5

num = int(input("Enter a number: "))
num2 = (num * 10) + num
num3 = (num2 * 10) + num
result = num + num2 + num3
print("The result is: ", result)