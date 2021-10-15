# Beep displays a user specified number of mountains

print(f"\nHow many mountains should I display?")
mountains = int(input(">"))

for count in range(mountains):
    print(f"     /\\")
    print(f"    /  \\")
    print(f"   /    \\")
    print(f"  /      \\")

