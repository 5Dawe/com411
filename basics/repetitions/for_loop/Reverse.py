# a program that allows us to display a word character by character.

print(f"\nWhat phrase do you see?.")
phrase = str(input())
print(f"\nReversing...")
print(f"\nThe phrase is: ", end="")
for pos in range(len(phrase)-1, -1, -1):
    print(phrase[pos], end="")





