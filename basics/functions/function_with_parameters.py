# A program to help Beep and Bop climb the ladder with display.

def display_ladder(steps):
    for count in range(0, steps, 1):
        print(f"|   |")
        print(f"*****")
    print(f"|   |")

def climb_ladder():
    print(f"How many steps remain?")
    steps_remain = int(input())
    print()
    display_ladder(steps_remain)

climb_ladder()
