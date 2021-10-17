# Ask for three whole numbers

print("\nPlease enter your first whole number.")
first_number = int(input(">"))

print("\nPlease enter your second whole number.")
second_number = int(input(">"))

print("\nPlease enter your third whole number.")
third_number = int(input(">"))

# Check the which numbers are odd and even and add to counters

print(f"\nThanks! I will now check how many odd and even numbers we have")

# Reset counters to zero
count_even = 0
count_odd = 0

# Check the first number
if first_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd = count_odd + 1

# Check the second number
if second_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd = count_odd + 1

# Check the third number
if third_number % 2 == 0:
    count_even = count_even + 1
else:
    count_odd = count_odd + 1

# Display the results of the count

print(f"\nThere were {count_odd} odd numbers and {count_even} even numbers")
