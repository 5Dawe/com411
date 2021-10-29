# Another variation of our previous program to help Beep and Bop escape the cave.

#function to create list
def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print(f"\nPlease enter a direction:")
    loc_var = directions()
    for index in range(len(loc_var)):
        print(f"{index}: {loc_var[index]}")
    user_input = int(input())
    user_choice = loc_var[user_input]
    return user_choice


def run():
    route = []
    print(f"Working out escape route...")
    for instructions in range(5):
        route.append(menu())
        #route[instructions] = resp
        #print(f"{route}")
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()