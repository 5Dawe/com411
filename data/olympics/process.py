# olympics project: modules for processes

import tui

#This function takes a list named data as a parameter and
# extracts the set of distinct years.
def list_years(data):
    tui.started("Listing years...")
    years_set = set()
    for lines in data:
        years_set.add(lines[9])
    tui.display_years(years_set)
    tui.completed()

# This function takes a list named data as a parameter and
# tallies up the number of gold, silver and bronze medals.
def tally_medals(data):
    tui.started("Tallying medals")
    medal_tally_dict = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for lines in data:
        if lines[14] == "Gold":
            medal_tally_dict["Gold"] += 1
        elif lines[14] == "Silver":
            medal_tally_dict["Silver"] += 1
        elif lines[14] == "Bronze":
            medal_tally_dict["Bronze"] += 1
    tui.display_medal_tally(medal_tally_dict)
    tui.completed()


# This function takes a list named data as a parameter and
# tallies up the number of gold, silver and bronze medals for each team.
def tally_team_medals(data):
    tui.started("Tallying medals for each team.")
    team_medal_tally_dict = {}
    for lines in data:
        if lines[6] not in team_medal_tally_dict:
            team_medal_tally_dict[lines[6]] = {"Gold": 0, "Silver": 0, "Bronze": 0}
        if lines[14] == "Gold":
            team_medal_tally_dict[lines[6]]["Gold"] += 1
        elif lines[14] == "Silver":
            team_medal_tally_dict[lines[6]]["Silver"] += 1
        elif lines[14] == "Bronze":
            team_medal_tally_dict[lines[6]]["Bronze"] += 1

    for key, value in team_medal_tally_dict.items():
        print(f"{key} ")
        temp_dict = str(value)
        print(str(temp_dict).replace("{", "").replace("}", "").replace("'", "").replace(" ", "").replace(",", ", "))
        #lines below for printing through a loop
        #for key2, value2 in value.items():
        #    print(f"{key2}:{value2}  ",end="")

    #print(team_medal_tally_dict)
    tui.completed()



