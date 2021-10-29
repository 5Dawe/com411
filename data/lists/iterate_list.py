# A variation of a variation of our previous program to help Beep and Bop escape the cave.

#function to create list
def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print(f"Please enter a direction:")
    loc_var = directions()
    for index in range(len(loc_var)):
        print(f"{index}: {loc_var[index]}")

def run():
    menu()

if __name__ == "__main__":
    run()