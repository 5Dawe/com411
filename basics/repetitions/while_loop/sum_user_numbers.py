# Beep will calculate the sum of the first 100 numbers

# declare variables
iterations = 0
the_total = 0
print(f"\nHow many numbers should I sum up?")

#gather input from user of quantity of numbers to sum
to_sum = int(input(">"))

#loop to gather each number
while iterations < to_sum:
    iterations = iterations + 1
    print(f"\nPlease enter number {iterations} of {to_sum}")
    add_me = int(input(">"))
    the_total = the_total + add_me

print (f"\nThe answer is {the_total}")