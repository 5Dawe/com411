# A program to help us extract values from the CSV file

# import csv module
import csv

# define function to open csv and read 1st line as header and cycle through file for values
def extract(f_path):
    print(f"Extracting...")
    with open(f_path) as file:
        names = str("")
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            # have to convert value to sting before adding it to the variable
            names = names + "\n" + str(values[1])
        print(f"Done! The extracted names are as follows:")
        print(names)

# Define a run function to start program
def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
