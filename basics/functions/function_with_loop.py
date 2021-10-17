# A program to help Beep and Bop cross the bridge.

def cross_bridge(steps):
    for count in range(0, steps, 1):
        print(f"Crossed step.")
    if steps > 5:
        print(f"The bridge is collapsing!")
    else:
        print(f"We must keep going!")

cross_bridge(3)


cross_bridge(6)
