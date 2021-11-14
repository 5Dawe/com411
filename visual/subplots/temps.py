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

    #We can also create the subplots such that they share
    #the x - axis, the y axis, or both:
    # fig, axs = plt.subplots(2, 2, sharex='all')  # all subplots share the x-axis
    # fig, axs = plt.subplots(2, 2, sharex='col')  # only subplots in the same column share the x-axis
    # fig, axs = plt.subplots(2, 2, sharey='row')  # only subplots in the same row share the y-axis

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()

if __name__ == "__main__":
    run()