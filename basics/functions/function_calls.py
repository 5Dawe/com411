# A program which manipulate cryptic words.
def run():
    print(f"Please enter some text")
    u_string = str(input())
    print(f"What should i do with the text?")
    print(f"1) Display in a box")
    print(f"2) Display lower case")
    print(f"3) Display upper case")
    print(f"4) Display mirrored")
    print(f"5) Repeat")
    u_imp = str(input())
    if u_imp == "1":
        s_len = len(u_string)
        for count in range(0, s_len+4, 1):
            print(f"#", end="")
        print(f"\n# {u_string} #")
        for count in range(0, s_len+4, 1):
            print(f"#", end="")
    elif u_imp == "2":
        u_string = u_string.lower()
        print(u_string)
    elif u_imp == "3":
        u_string = u_string.upper()
        print(u_string)
    elif u_imp == "4":
        for pos in range(len(u_string) - 1, -1, -1):
            print(u_string[pos], end="")
    elif u_imp == "5":
        print(f"\nHow many repetitions would you like?")
        reps = int(input())
        for rep in range(0, reps, 1):
            print(u_string)
    else:
        print(f"Sorry, {u_imp} is not one of the options")

# Run the program
run()
print(f"\nAll Done.")