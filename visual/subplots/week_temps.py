# A program to read temps from CSV and display

import csv

# import graphical plotting module
import matplotlib.pyplot as plt


def read_data():
    with open("temps.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header = next(csv_reader)
        temp_dict = {}
        temp_dict[(header[0])] = []
        temp_dict[(header[1])] = []
        for row in csv_reader:
            temp_dict[(header[0])].append(row[0])
            temp_dict[(header[1])].append(row[1])
    return temp_dict

# run the program to display the temp plot
def run():
    data = read_data()
    weeks = []
    for key in data.keys():
        weeks.append(key)

    fig, axs = plt.subplots(2, 1)
    ax_index = 0

    for week in weeks:
        axs[ax_index].plot(range(len(data[week])), data[week])
        ax_index += 1

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()