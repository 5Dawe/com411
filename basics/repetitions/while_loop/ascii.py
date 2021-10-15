# Beep asks user how many bars to charge

# declare variable for iterations
iterations = 0

# get input
print(f"\nHow many bars should be charged?")
to_charge = int(input(">"))

# loop while charging
while iterations < to_charge:
    print(f"\nCharging...", end="")
    iterations = iterations + 1
    bars = 0
    while bars < iterations:
        print(f"█ ", end="")
        bars = bars + 1


# Beep removes cables
