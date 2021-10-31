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
    print("")
    #choose = int(input())
    choose = 2
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
    else:
        print(f"Sorry, option not recognised!")

if __name__ == "__main__":
    run()