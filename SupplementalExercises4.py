"""
Class: CS230--Section 3
Name: Taice Brenner
Description: Supplemental Exercises on Functions
I pledge that I have completed the programming assignment
independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

print("Exercise # 1: ")
amount = int(input("Purchase amount: "))
tax = 0.0625
salestax = amount * tax
print(f"Sales tax due: ${salestax:.2f}")


print("\nExercise # 2: ")
string = input("Enter a string: ")
upper = sum(1 for a in string if a.isupper())
lower = sum(1 for b in string if b.islower())
print(f"No. of Upper-Case characters: {upper}\nNo. of Lower-Case characters: {lower}")


print("\nExercise # 3: ")
distance = float(input("Enter distance traveled: "))
cost = float(input("Enter cost per gallon: "))
miles = 50
galloncost = (distance / miles) * cost
print(f"The cost to travel {distance:.2f} miles when the cost for gallon is ${cost:.2f} is ${galloncost:.2f}.")


print("\nExercise # 4: ")
def is_anagram(string1, string2):
    string1 = [letter for letter in string1]
    string1.sort()
    string2 = [letter for letter in string2]
    string2.sort()
    return string1 == string2
anagram = is_anagram('debit card', 'bad credit')
if anagram:
    print(f"'{'debit card'}' and '{'bad credit'}' are anagrams.")
else:
    print(f"{'debit card'}and {'bad credit'} are not anagrams.")
anagram = is_anagram('dirty room', 'dormitory')
if anagram:
    print(f"{'dirty room'} and {'dormitory'} are anagrams.")
else:
    print(f"'{'dirty room'}' and '{'dormitory'}' are not anagrams.")


print("\nExercise # 5: ")
def caught_speeding(speed, birthday):
    if birthday == False:
        if speed <= 60:
            result = 0
            print(f'{result} - No ticket')
        elif (speed >= 61) and speed <= 80:
            result = 1
            print(f'{result} - Small ticket')
        else:
            result = 2
            print(f'{result} - Big ticket')
    if birthday == True:
        if speed <= (60+5):
            result = 0
            print(f'{result} - No ticket')
        elif (speed >= (61+5)) and speed <= (80+5):
            result = 1
            print(f'{result} - Small ticket')
        else:
            result = 2
            print(f'{result} - Big ticket')

caught_speeding(60, False)
caught_speeding(65, False)
caught_speeding(65, True)