# Beep adjusts night vision based on user input

print(f"\nWhat level of brightness is required?")
bri_req = (int(input(">"))+1)

print(f"Adjusting brightness level...")
for count in range(2, bri_req, 2):
    print(f"Beep's brightness level:", end="")
    for beep_bri in range(0, count, 1):
        print(f"*", end="")
    print(f"")
    print(f"Bop's brightness level:", end="")
    for bop_bri in range(0, count, 1):
        print(f"*", end="")
    print(f"\n")
    print (f"{count}")


print(f"\nAdjustments complete!")
