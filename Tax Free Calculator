string = 'Tax Free Calculator'
print(f'=' * 8 + string + '=' *8)

username = input("Please enter your name: ")
print("Welcome,", username)


name = input("Enter the name of the item: ")
price = float(input("Enter the price per item: "))
quantity = int(input("Enter the quantity purchased: "))
budget = float(input("Enter your budget: "))

TAXPERCENT = 0.0625
cost = price * quantity
tax = cost + (cost * TAXPERCENT)
print(f"\nIt cost ${tax:.2f} to buy", quantity, name, "outside tax free weekend.")
print(f"It cost ${cost:.2f} to buy", quantity, name, "during tax free weekend.")

amounttax = round((budget // ((price + (price * TAXPERCENT)))))
remaindertax = (budget % tax)
print("\nYou can buy", amounttax, name, f"outside tax free weekend, with ${remaindertax:.2f} left.")

amountreg = round(budget // price)
remainder = round(budget % price)
print("You can buy", amountreg, name, f"during tax free weekend, with ${remainder:.2f} left.")

end="\n"
