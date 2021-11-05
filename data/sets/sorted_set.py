# A program to help Beep and Bop record how many of each type of item they saw (e.g. 2 skyscrapers, 5 neon signs, etc.).

# function to obtain input on observation from user, 7 times
def observed():
    observations = []
    for add_lst in range(0, 5, 1):
        print(f"Please enter an observation:")
        observations.append(input())
    return observations


# function to obtain user input to delete selected value
def remove_observations(obs_lst):
    print(f"")




# function to count the number of times a list item is present
# then add the item and the count to the set.
def run():
    print(f"Counting observations...")
    loc_vari = observed()
    usr_imp = "yes"
    while usr_imp == "yes":
        print(f"\nDo you wish to remove an observation (yes/no)?")
        usr_imp = str.lower(input())
        if usr_imp == "yes":
            print(f"What observation do you wish to remove?")
            usr_selection = input()
            loc_vari.remove(usr_selection)


    counting = set()
    for items in loc_vari:
        #print(loc_vari.count(items))
        items = (items, loc_vari.count(items))
        counting.add(items)
    print(f"\nObservations")
    for things in counting:
        print(f"{things[0]} observed {things[1]} time(s).")



if __name__ == "__main__":
    run()


