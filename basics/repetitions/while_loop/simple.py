# Beep asks user how many cables to remove

# declare variable for iterations
iterations = 0

print(f"\nHow many cables should I remove")
to_remove = int(input(">"))
while iterations < to_remove:
    print(f"Cable removed.")
    iterations = iterations + 1


# Beep removes cables
