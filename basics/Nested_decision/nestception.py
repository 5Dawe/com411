# Helping Beep find his spare battery
# Nested IF statements

print("I need my spare battery, wWhere should I look?")
look_room = str(input(">").lower())

# Checking the bedroom
if look_room == "in the bedroom":
    print(f"\nWhere {look_room} should i look?")
    look_bedroom = str(input(">").lower())
    if look_bedroom == "under the bed":
        print(f"\nFound some shoes but no battery")
    else:
        print(f"\nFound some mess but no battery.")

# Checking the bathroom
if look_room == "in the bathroom":
    print(f"\nWhere {look_room} should i look?")
    look_bathroom = str(input(">").lower())
    if look_bathroom == "in the bathtub":
        print(f"\nFound a rubber duck but no battery")
    else:
        print(f"\nFound a wet surface but no battery.")

# Checking the bedroom
if look_room == "in the lab":
    print(f"\nWhere {look_room} should i look?")
    look_lab = str(input(">").lower())
    if look_lab == "on the table":
        print(f"\nYes! I found my battery!")
    else:
        print(f"\nFound some tools but no battery.")

else:
    print(f"\nI do not know where that is but I will keep looking.")
