"""
Create new string named result where all upper case letters in s are lowercase and all other characters are a "-"
"""
s = "Bentley University, Waltham, MA"
result = ""
for ch in s:
    if ch.isupper():
        result = result + ch.lower()
    else:
        result = result + '-'
print(result)

firstName = "Tom"
lastName = "Brady"
code = firstName[:2] + lastName[1] + lastName[-1]
code = code.upper()
print(code)


age = int(input("How old are you? "))
if age < 3:
    print("You get in for free.")
elif age <= 12:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")


word = input("Enter a word: ")
newWord = word.replace("a", "@").replace("e", "#").replace("i", "!").replace("o", "%").replace("u", "^")
print("The new word is: " + newWord)

word = input("Enter a word: ").lower()

for ch in word:
    if ch == 'a':
        word = word.replace(ch,'@')
    elif ch == 'e':
        word = word.replace(ch,'#')
    elif ch == 'i':
        word = word.replace(ch,'!')
    elif ch == 'o':
        word = word.replace(ch,'%')
    elif ch == 'u':
        word = word.replace(ch,'^')
print(word)



donut = int(input("How many donuts? "))
if donut % 12 == 0:
        print(donut + " donuts is " + (donut / 12) + " dozen donuts")
else:
        print(donut + " donuts is " + (donut / 12) + " dozen donuts and " + (round(donut % 12)) + " donuts")