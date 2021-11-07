# olympics Test User Interface


# A function named started that takes 1 parameter named msg.
# The default value of the parameter is an empty string.
def started(msg=""):
    print(f"\n------------------------------------------")
    print(f"Operation started: {msg}...\n")


# A function named completed that takes no parameters.
def completed():
    print(f"\nOperation completed.")
    print(f"------------------------------------------")

# A function named error that takes 1 parameter named msg.
# The function should display the message "Error! {msg}"
# where {msg} is the value passed as a parameter.
def error(msg):
    print(f"Error! {msg}")


# A function named menu that takes no parameters.
# The function should display a menu
def menu():
    print(f"Please select one of the following options:")
    print(f"[years]    List unique years")
    print(f"[tally]      Tally up medals")
    print(f"[team]    Tally up medals for each team")
    print(f"[exit]       Exit the program")
    print(f"\nYour selection:")
    return input()




# The function should display the name of each medal and
# its count with "Gold" displayed first and "Bronze" displayed last.
def display_medal_tally(tally):
    for key, value in tally.items():
        print(f"|{key:<8} | {value:<8}|")

# The function should display the name of each team and the medals
# the team has one.
def display_team_medal_tally(team_tally):
    print(team_tally)

# The function should sort the years into descending order
# (largest first) and display each year on a new line
def display_years(years):
    for item in (sorted(years)):
        print(item)



