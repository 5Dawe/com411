# A program to display the path Beep and Bop are taking through Robo City.

# import graphical plotting module
import matplotlib.pyplot as plt


# define function to display graph plot from parameters
def display(x_values, y_values):
    x = x_values
    y = y_values
    plt.plot(x, y)
    plt.show()


# define function to create lists and store values
def run():
    x_values = []
    x_values.append(1)
    x_values.append(2)
    x_values.append(3)
    x_values.append(4)
    x_values.append(5)
    y_values = []
    y_values.append(1)
    y_values.append(4)
    y_values.append(9)
    y_values.append(16)
    y_values.append(25)
    display(x_values, y_values)




if __name__ == "__main__":
    run()


