# Ask for two numbers

print("\nPlease enter your first number.")
firstnumber = float(input(">"))

print("\nPlease enter your second number.")
secondnumber = float(input(">"))

# Compare two numbers and determine which is bigger

print(f"\nComparing {firstnumber} and {secondnumber}...")

if firstnumber < secondnumber:
    print(f"\nYour first number {firstnumber} is smaller")
elif firstnumber > secondnumber:
    print(f"\nYour second number {secondnumber} is smaller")
else: print(f"\nboth your numbers are the same!")



