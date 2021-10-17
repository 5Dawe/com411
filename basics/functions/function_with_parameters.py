# A program to help Beep and Bop climb the ladder.

def climb_ladder(steps_to_go, steps_crossed):
    if steps_to_go > steps_crossed :
        print(f"Still some way to go!")
    else:
        print(f"We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)
