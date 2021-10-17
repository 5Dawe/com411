# A program to help Beep and Bop escape the large boulder.

def identify():
    print(f"What lies before us?")
    seen = str(input())
    if seen == "a large boulder":
        print(f"Time to run!")
    else:
        print(f"We will be fine")

identify()



