# A program that shows some animated squares - a small
# square, followed by a medium square, followed by a large square

# import graphical plotting module
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define global variable
squares = []
fig, ax = plt.subplots()


# Function to create and populate dictionaries
def init():
    global squares
    squares.append({"x": [3, 4, 4, 3, 3], "y": [3, 3, 4, 4, 3]})
    squares.append({"x": [2, 5, 5, 2, 2], "y": [2, 2, 5, 5, 2]})
    squares.append({"x": [1, 6, 6, 1, 1], "y": [1, 1, 6, 6, 1]})


# Function to animate
def animate(frame):
    global squares, ax
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)
    square_index = frame
    ax.plot(squares[square_index]['x'], squares[square_index]['y'])


# Function to run
def run():
    global fig
    squares_animation = animation.FuncAnimation(fig, animate, frames=3, interval=1000, init_func=init, repeat=True)
    plt.show()


run()
