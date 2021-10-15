# Beep will calculate factorial of a number: a function that multiplies a number by every number below it till 1

# declare variables
iterations = 0
factorial = 1
print(f"\nPlease enter a number:")

#gather input from user
to_fac = int(input(">"))
count = to_fac

#loop to gather each number
while iterations < count:
    factorial = factorial * to_fac
    print(f"{factorial}")
    print(f"{count}")
    print(f"{iterations}")
    print(f"{to_fac}")
    to_fac = to_fac - 1
    iterations = iterations + 1
    print(f"\n")

print (f"\nThe factorial is {factorial}")