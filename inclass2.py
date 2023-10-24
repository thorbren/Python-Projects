num1 = 6
num2 = 7
print(num1 == num2)

sales_tax = .0625
if sales_tax > .05:
    print("The sales tax is greater than 5 percent")

sales_tax = float(input("Enter the sales tax (enter as a decimal please): "))

if sales_tax > .05:
    print("The sales tax is high--it is greater than 5 percent.")
else:
    print("The sales tax is low--it is less than or equal to 5 percent.")

number = int(input("Enter a number: "))
if (number % 2) == 0:
    print(" The number {0} is even.".format(number))
else:
    print("The number {0} is odd.".format(number))

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("The number", num, "is even.")
else:
    print("The number", num, "is odd.")

x = 5
y = 2
if x >= 2 or (x + y) > 9:
    print("This works")
else:
    print("This does not work")

x = 4
y = 0
if x >= 5 and (x / y) > 2:
    print("This works")
else:
    print("This does not work")

for letter in "Python":
    print(letter)

for count in range(10):
    print(count)

for i in range(1,11):
    print(i, end=" ")

for i in range(1, 11):
    print(i, end="* *")

# FizzBuzz

for count in range(1, 51):
    if count % 3 == 0:
        print("Fizz")
    if count % 5 ==0:
        print("Buzz")
    print(count, end=" ")