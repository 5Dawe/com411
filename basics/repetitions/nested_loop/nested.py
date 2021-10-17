# A program that allows us to display a grid of ASCII emoji.

print(f"How many rows should i have?")
u_rows = int(input())
print(f"How many columns should i have?")
u_cols = int(input())
print(f"\nHere i go...")
print()
for rows in range (0, u_rows, 1):
    for cols in range (0, u_cols, 1):
        print(f":-) ", end="")
    print()
print(f"\nDone!")

