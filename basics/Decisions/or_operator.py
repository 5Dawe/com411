def run():

    # Ask user what type of adventure Beep should have
    print(f"\nWhat type of adventure should i have?")
    adventure_type = str(input(">").lower())

    # Identify what type of adventure
    if (adventure_type == "scary") or (adventure_type == "short"):
        print(f"\nEntering the dark forest!")
    elif (adventure_type == "safe") or (adventure_type == "long"):
        print(f"\nTaking the safe route!")
    else:
        print(f"\nNot sure what route to take.")


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
