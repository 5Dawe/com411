# A program to display the path Beep and Bop are taking through Robo City.



# import graphical plotting module
import matplotlib.pyplot as plt


# define a function
def coordinate():
    print(f"Please enter a value for x:")
    x = input()
    print(f"Please enter a value for y:")
    y = input()
    return (x, y)

# define a function
def path():
    print(f"Retrieving path...")
    x_values = []
    y_values = []
    for iterations in range(0,4,1):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return (x_values, y_values)


# run the program to display the plots
def run():
    values = path()
    print(f"{values}")
    x = values[0]
    y = values[1]
    plt.plot(x, y, 'ro--')
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()


if __name__ == "__main__":
    run()


