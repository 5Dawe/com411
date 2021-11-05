# This module uses our other modules in order]
# to present the user with a functioning program.

import csv
#import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    data = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            data.append(values)
    tui.completed()
    return data


def run2():
    athlete_data = read_data("athlete_events.csv")


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run2()

