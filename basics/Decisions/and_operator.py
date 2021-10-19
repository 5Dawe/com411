# Beep asks use what he heard and saw
def run():

    print(f"\nWhat did i hear?")
    i_hear = str(input(">").lower())
    print(f"\nWhat did i see?")
    i_see = str(input(">").lower())

    # Decide if to continue
    if (i_hear == "grrr") and (i_see == "two red eyes"):
        print(f"\nThere is a scary creature. I should get out of here!")
    else:
        print(f"\nI am a little scared but I will continue.")


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
