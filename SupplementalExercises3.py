"""
Class: CS230--Section 3
Name: Taice Brenner
Description: Supplemental Exercises on String Data Types
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("Exercise # 1: ")
def reverse_slicing(string):
    return string[::-1]

string = input("Enter a string: ")
string2 = reverse_slicing(string)
print(f"The string, {string}, backwards, is {string2} ")


print("\nExercise # 2: ")
def vowels(string2):
    print(string2)
    vowel = "aeiouyAEIOUY"
    count = 0

    for char in string2:
        if char in vowel:
            count += 1
    return count

string2 = input("Enter a string: ")
count = vowels(string2)
print(f"{count}")


print("\nExercise # 3: ")
string3 = "Programming in Python"

print("#1 Print the length of the string: ", len(string3))
print("#2 Print the position where 'n' appears the first time is: ", string3.index("in"))
print("#3 Print the number of times 'n' appears is: ", string3.count("n"))
print("#4 Print the number of spaces is: ", string3.count(" "))
print("#5 Print the substring 'Pro': ", string3[0:3])
print("#6 Print the substring 'thon': ", string3[17:])
print("#7 Print the substring 'Programming in Py': ", string3[:17])
print("#8 Split the string at the spaces: ", string3.split())
print("#9 Print the substring 'a': ", string3[5])
print("#10 Print the string in uppercase: ", string3.upper())
print("#11 Print the string in lowercase: ", string3.lower())
print("#12 Print the string but replace 'in' with 'with': ", string3.replace("in", "with"))


print("\nExercise # 4: ")
string4 = input("Enter a string: ")
index = len(string4) // 2
chars = string4[index - 1:index +2]
print("The middle three characters are: ", chars)


print("\nExercise # 5: ")
string5 = input("Enter a string: ")
rotation = int(input("Enter the number of characters to rotate--the number must be less than the number of characters in the string: "))
if rotation >= len(string5):
    print("Enter the number of characters to rotate--the number must be less than the number of characters in the string: ")
else:
    rightRotate = string5[-rotation:] + string5[:-rotation]
    leftRotate = string5[rotation:] + string5[:rotation]
    print(f"The string, {string5}, rotated to the left {rotation} characters is {leftRotate}")
    print(f"The string, {string5}, rotated to the right {rotation} characters is {rightRotate}")


print("\nExercise # 6: ")
string6 = input("Enter first string: ")

while len(string6) < 2:
    print("String must be at least two characters long! Please re-enter: ")
    string6 = input("Enter first string: ")

string7 = input("Enter second string: ")

while len(string7) < 3:
    print("String must be at least three characters long! Please re-enter: ")
    string7 = input("Enter second string: ")

string8 = string6 + string7 + string7 + string6
print("The new string is ", string8)


print("\nExercise # 7: ")
string9 = input("Enter a string: ")
print(f"The string is '{string9}'.")

for i in range(len(string9)):
    print(f"\nThe characters in position {i} is {string9[i]}")