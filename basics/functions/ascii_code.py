# A program that determines the ASCII code for a character.
print(f"Program started!")
print(f"Please enter an ASCII code:")
u_asc = abs(int(input()))


if u_asc in range (32, 127, 1):
    print(f"The character represented by the ASCII code {u_asc} is: ", end="")
    print(chr(u_asc))
else:
    print(f"Sorry, please enter a character from the printable range")
print(f"Program ended!")

