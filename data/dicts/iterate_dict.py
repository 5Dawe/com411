# A program to help Beep and Bop decipher the pattern

# function to create a dictionary
def pattern():
    sequences = {}
    sequences["Short Sequence"] = 3
    sequences["Medium Sequence"] = 2
    sequences["Long Sequence"] = 1
    return sequences

# function should iterate through the keys of the dictionary and display each on a new line.
def display_keys(data):
    print(f"\nKeys:")
    for key in data.keys():
        print(key)

# The function should iterate through the values of the dictionary and display each on a new line.
def display_values(data):
    print(f"\nValues:")
    for value in data.values():
        print(value)


# The function should iterate through each key-value pair and display it on a new line.
def display_items(data):
    print(f"\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


# then add the item and the count to the set.
def run():
    print(f"\nDictionary:")
    print(pattern())
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


if __name__ == "__main__":
    run()
