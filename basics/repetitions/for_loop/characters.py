# a program that allows us to display a word character by character.

print(f"\nWhat strange markings do you see?.")
markings = str(input())
print(f"\nIdentifying...")
print(f"")

for pos in range(0,len(markings), 1):
    print(f"index {pos}: ", end="")
    print(markings[pos])

print(f"\nDone!")



