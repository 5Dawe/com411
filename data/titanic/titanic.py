# A program that will allow us to load the data set for processing.

# Define global variables
records = []
headings = []

# Import required modules
import csv


# Define a function to open the data file
def load_data(file_path):
    print(f"\nLoading Data... ", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            records.append(values)
    print(f"Done!")


# Present the user with a simple menu of options and ask for input
def display_menu():
    print("")
    print(f"Please select one of the following options:")
    print(f"[1] Display the names of all the passengers")
    print(f"[2] Display the number of passengers that survived")
    print(f"[3] Display the number of passengers by gender")
    print(f"[4] Display the number of passengers by age group")
    print(f"[5] Display the number of survivors by age group")
    print("")
    choose = int(input())
    #choose = 5
    return choose


# function for option 1: displaying passenger names
def display_passenger_names():
    print(f"\nThe names of the passengers are...")
    for values in records:
        passenger_name = values[3]
        print(f"{passenger_name}")


# function for option 2: number of survivors
def display_num_survivors():
    num_survived = 0
    for values in records:
        survival_status = int(values[1])
        if survival_status == 1:
            num_survived = num_survived + 1
    print(f"\n{num_survived} passengers survived.")


# function for option 3: number of passengers by gender
def display_passengers_by_gender():
    females = 0
    males = 0
    other = 0
    for values in records:
        gender = str.lower(values[4])
        if gender == "male":
            males = males + 1
        elif gender == "female":
            females = females + 1
        else:
            other = other + 1
    print(f"Males: {males}, Females: {females}.")


# function for option 4: passengers by age group
def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for values in records:
        if (values[5]) != "":
            age = float(values[5])
            if age < 18:
                children = children + 1
            elif age < 65:
                adults = adults + 1
            else:
                elderly = elderly + 1
    print(f"\nChildren: {children}, Adults: {adults}, Elderly: {elderly}.")


# function for option 5: number of survivors by age group
def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    children_s = 0
    adults_s = 0
    elderly_s = 0
    for values in records:
        if (values[5]) != "":
            age = float(values[5])
            if age < 18:
                children = children + 1
                if (values[1]) == "1":
                    children_s = children_s + 1
            elif age < 65:
                adults = adults + 1
                if (values[1]) == "1":
                    adults_s = adults_s + 1
            else:
                elderly = elderly + 1
                if (values[1]) == "1":
                    elderly_s = elderly_s + 1
    print(f"\nNumber of survivors.\nChildren: {children_s}/{children}, Adults: {adults_s}/{adults}, Elderly: {elderly_s}/{elderly}.")


# function to run the program and action user selection
def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"\nSuccessfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_by_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print(f"Sorry, option not recognised!")

if __name__ == "__main__":
    run()