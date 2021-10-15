# Beep asks user how many live cables to avoid

# declare variable for iterations
iterations = 0

print(f"\nHow many live cables should I avoid")
to_avoid = int(input(">"))
while iterations < to_avoid:
    print(f"Avoiding...", end="")
    iterations = iterations + 1
    print(f"Done! {iterations} live cables avoided.")


# Beep removes cables
