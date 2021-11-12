# A program to display some data related to temperatures observed during 1 week


# import graphical plotting module
import matplotlib.pyplot as plt


# function to read data
def read(f_path):
    file = open(f_path, mode='r')
    temp_list = []
    for lines in file:
        temp_list.append(int(lines))
    file.close
    return temp_list




# run the program to display the temp plot
def run():
    data = read("temps.txt")
    #plt.plot(data)
    plt.bar(data, data)
    plt.show()
    #fig, axs = plt.subplots(2, 2)
    #fig, axs = plt.subplots(2, 2, sharex='all')  # all subplots share the x-axis


if __name__ == "__main__":
    run()