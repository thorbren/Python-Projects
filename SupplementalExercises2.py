"""
Class: CS230--Section 3
Name: Taice Brenner
Description: Supplemental Exercises on Control Structures
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("Exercise #1: ")

print("The first 10 odd numbers are:")
for num in range(1, 20):
    if num % 2 != 0:
        print(num)


print("\nThe first five multiples of 10 are:")
for num in range(1,51):
    if num % 10 == 0:
        print(num)


print("Exercise #2: ")

number = int((input("Enter a number: ")))
for n in range(number, 0, -1):
    print(n * '*', end="\n")


print("Exercise #3: ")

fourMultiple = 0
eightMultiple = 0
while True:
    number = int((input("Enter a postitive number: ")))
    if number == 0:
        break
    if number % 4 == 0:
        fourMultiple += 1
    if number % 8 == 0:
        eightMultiple += 1

print(f"You entered {fourMultiple} multiples of 4 and {eightMultiple} multiples of 8.")


print("Exercise #4: ")
for n in range(1,9):
    print(f"{n}{n + 1}", end=", ")


print("\nExercise #5: ")
total = 0

for number in range(1,101):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print("The total of the numbers from 1 to 100 that are multiples of three or five is", total)


print("Exercise #6: ")

startNumber = str(input("Enter starting number: "))
terms = int(input("Enter number of terms: "))

lastNumber = startNumber

for i in range(0,terms):
    print(startNumber * (i + 1), end=', ')