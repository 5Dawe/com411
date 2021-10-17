# Program should then count the number of dashes between the two markers

print(f"Please enter a sequence")
seq = str(input())
pos_1 = ""
pos_2 = ""

print(f"Please enter the character for the marker")
mark = str(input())

for pos in range(0, len(seq), 1):
    if seq[pos] == mark:
        if pos_1 == "":
            pos_1 = pos
        else:
            pos_2 = pos - 1
mark_dist = pos_2 - pos_1
print(f"\nThe distance between the markers is {mark_dist}")
