# Beep adjusts night vision based on user input

print(f"\nWhat level of brightness is required?")
bri_req = int(input(">"))

print(f"Adjusting brightness level...")
for count in range(2, bri_req, 2):
    print(f"Beep's brightness level:", end="")
    for beep_bri in range(0, {count}, 1):
        print(f"X", end="")


print(f"\nAdjustments complete!")