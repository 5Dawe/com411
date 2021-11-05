# A program to help Beep and Bop identify the patterns.



def short_pattern():
    pattern = {"sequence":"101", "occurences":5}
    return pattern


def medium_pattern():
    pattern = {"sequence":"111000", "occurences":25}
    return pattern


def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurences":50}
    return pattern


def run():
    print(f"Analysing patterns...")
    sequences = {}
    sequences["Short Sequence"] = short_pattern()
    sequences["Medium Sequence"] = medium_pattern()
    sequences["Long Sequence"] = long_pattern()
    for key, value in sequences.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run()
