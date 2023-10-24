command = 'P'

match command:
    case'P':
        print('Print')
    case 'q':
        print('Quit')
    case _:
        print("Unknown command")




color = 'green'
print(color)
color = "green"
print(color)
color = """
        We can assign many colors
        red, green, and blue
        """
print(color)


color = 'green'
print(color[0])
print(color[3])
print(color[-4])


string = 'blue and gold'
print("|" + string[0:5] + "|")
print(string[5:13])
print(string[:4])
print(string[5:])

print()
print(string[-4:])
print(string[5:13:2])
print(string[-2:-10:-2])



string1 = input("Enter a string: ")
string2 = input("Enter a second string: ")
print("The new string is ", string1[0:2] + string2[2:], string2[0:2] + string1[2:])


greeting = 'Welcome '
day = 'to our business'
newGreeting = greeting + day
print(newGreeting)

length = len(newGreeting)
print("\nThe length of the new string", newGreeting, "is:", length)


string = input("Enter a string: ")
newString = string.replace(string[0], '#')
print("The new string is ", newString)