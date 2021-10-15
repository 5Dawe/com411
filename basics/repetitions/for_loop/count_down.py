# Beep counts down from a user defined number

print(f"\nHow far are we from the cave?")
steps = int(input(">"))

for count in range(steps, 0, -1):
    print(f"{count} steps remaining")

print(f"\nWe have reached the cave!")