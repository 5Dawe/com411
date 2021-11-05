# olympics project: modules for processes

#This function takes a list named data as a parameter and
# extracts the set of distinct years.
def list_years(data):
    started("Listing years...")
    years_set = ()
    for lines in data:
        years_set.append(lines[9])
    display_years(years_set)
    completed()

# This function takes a list named data as a parameter and
# tallies up the number of gold, silver and bronze medals.
def tally_medals(data):
    started("Tallying medals")
    medal_tally_dict = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for lines in data:
        if lines[14] == "Gold":
            medal_tally_dict["Gold"] += 1
        elif lines[14] == "Silver":
            medal_tally_dict["Silver"] += 1
        elif lines[14] == "Bronze":
            medal_tally_dict["Bronze"] += 1
    display_team_medal_tally(medal_tally_dict)
    completed()


# This function takes a list named data as a parameter and
# tallies up the number of gold, silver and bronze medals for each team.
def tally_team_medals(data):
    started("Tallying medals for each team.")
    team_medal_tally_dict = {}
    for lines in data:
        if lines[6] not in team_medal_tally_dict:
            loop_gold = 0
            loop_silver = 0
            loop_bronze = 0
            if lines[14] == "Gold":
                loop_gold += 1
            elif lines[14] == "Silver":
                loop_silver += 1
            elif lines[14] == "Bronze":
                loop_bronze += 1
            team_medal_tally_dict = lines[6]: ####add medals here
            pattern = {"sequence": "1100110011001100", "occurences": 50}
    completed()



