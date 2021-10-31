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
    choose = int(input())
    return choose



def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"\nSuccessfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option {selected_option}")


if __name__ == "__main__":
    run()