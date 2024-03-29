# A program to help Beep and Bop record how many of each type of item they saw (e.g. 2 skyscrapers, 5 neon signs, etc.).

# function to obtain input on observation from user, 7 times
def observed():
    observations = []
    for add_lst in range(0, 7, 1):
        print(f"Please enter an observation:")
        observations.append(input())
    return observations

# function to count the number of times a list item is present
# then add the item and the count to the set.
def run():
    print(f"Counting observations...")
    loc_vari = observed()
    counting = set()


    for items in loc_vari:
        #print(loc_vari.count(items))
        items = (items, loc_vari.count(items))
        counting.add(items)

    for things in counting:
        print(f"{things[0]} observed {things[1]} time(s).")





if __name__ == "__main__":
    run()


