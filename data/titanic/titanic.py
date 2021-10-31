# A program that will allow us to load the data set for processing.

# Define global variables
records = []
headings = []

# Import required modules
import csv


# Define a function to open the data file
def load_data(file_path):
    print(f"Loading Data... ", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            records.append(values)
    print(f"Done!")

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"\nSuccessfully loaded {num_records} records.")


if __name__ == "__main__":
    run()