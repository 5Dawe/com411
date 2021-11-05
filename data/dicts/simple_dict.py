# A program to help Beep and Bop decipher the pattern

# function to create a dictionary
def pattern():
    sequences = {}
    sequences["Short Sequence"] = 3
    sequences["Medium Sequence"] = 2
    sequences["Long Sequence"] = 1
    return sequences


# then add the item and the count to the set.
def run():
    print(pattern())


if __name__ == "__main__":
    run()
