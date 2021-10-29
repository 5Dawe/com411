# A variation of our previous program to help Beep and Bop escape the cave.

#function to create list
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

#function to print items of list in pairs, looping for length of list
def run():
    movements()
    print(f"Moving...")
    loc_var = movements()
    #print(f"{loc_var}")
    list_len = int(len(loc_var))
    for items in range(0, list_len, 2):
        print(f"{loc_var[items]} for {loc_var[(items+1)]} steps")


if __name__ == "__main__":
    run()