# A program to read temps from CSV and display

# import csv module
import csv

# import graphical plotting module
import matplotlib.pyplot as plt


def read_data():
    with open("titanic.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header = next(csv_reader)
        temp_dict = {'survived':[], 'sex':[], 'age':[], 'fare':[]}
        for row in csv_reader:
            survived = row[1]
            sex = row[14]
            age = row[4]
            fare = row[8].strip()
            if (survived != "" and sex != "" and age != "" and fare != ""):
                temp_dict['survived'].append(survived)
                temp_dict['sex'].append(sex)
                temp_dict['age'].append(age)
                temp_dict['fare'].append(round(float(fare), 2))


    return temp_dict

# run the program to display the temp plot
def run():
    data = read_data()
    print(f"{data}")
    datasets = []
    for key in data.keys():
        datasets.append(key)

    fig, axs = plt.subplots(2, 2)
    ax_index = 0

    for dataset in datasets:
        axs[ax_index].plot(range(len(data[dataset])), data[dataset])
        ax_index =+ 1

    #for week in weeks:
    #    axs[ax_index].plot(range(len(data[week])), data[week])
    #    ax_index += 1

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()