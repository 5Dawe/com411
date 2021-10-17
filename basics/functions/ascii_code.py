# A program that determines the ASCII code for a character.
print(f"Program started!")
print(f"Please enter a standard character:")
u_ch = str(input())
if len(u_ch) == 1:
    print(f"The ASCII code for {u_ch} is: ", end="")
    print(ord(u_ch))
else:
    print(f"Sorry, please enter a single character")
print(f"Program ended!")

