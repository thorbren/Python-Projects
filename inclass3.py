num = 1
while num <= 10:
    print("The number is:", num)
    num += 1

total = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        break
    number = float(data)
    total += number
print("The sum is", total)


menuChoice = True

while menuChoice:
    print("""
    1 = Option 1,
    2 = Option 2,
    3 = Option 3,
    4 = Quit
     Enter choice: """)
    choice = int(input(""))
    if choice == 1:
        print("You chose option 1.")
    elif choice == 2:
        print("You chose option 2.")
    elif choice == 3:
        print("You chose option 3.")
    else:
        menuChoice = False


import random
num = random.random()
print(num, "\n")

minimum = 1
maximum = 100
for x in range (10):
    num = minimum + random.random() * (maximum - minimum)
    print(round(num, 3), end=' ')