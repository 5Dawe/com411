# A program to display the content of a CSV file.

# import csv module
import csv

# define function to open csv and read 1st line as header and cycle through file for values
def read(f_path):
    with open(f_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print(f"Values:")
        for values in csv_reader:
            print(f"{values}")


def run():
    read("bots.csv")


if __name__ == "__main__":
  run()