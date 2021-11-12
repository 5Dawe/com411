# A program to display the path Beep and Bop are taking through Robo City

# import graphical plotting module
import matplotlib.pyplot as plt

# import random module
import random


# define a function
def data():
    paths = {}
    print(f"What type of line would you like? :, -- or -")
    line_type = input()
    print(f"What colour would you like? r, g or b")
    line_colour = input()
    print(f"What style of marker would you like? o, s or ^")
    marker_type = input()
    paths["line"] = line_type
    paths["colour"] = line_colour
    paths["marker"] = marker_type
    return paths


# define a function
def generate():
    print(f"How many lines would you like to display?")
    no_lines = int(input())
    for times in range(0, no_lines, 1):
        values = data()
        x_values = []
        for i in range(0,5):
            n = random.randint(1,30)
            x_values.append(n)
        y_values = []
        for i in range(0, 5):
            n = random.randint(1, 30)
            y_values.append(n)
        x = x_values
        y = y_values
        style = ""
        for value in values.values():
            style = style + (value)
        plt.plot(x, y, style)
        plt.show()


# run the program to display the plots
def run():
    print(f"Running...")
    generate()
    print(f"Done!")

if __name__ == "__main__":
    run()