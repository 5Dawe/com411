import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

def animate(frame):
    global ax
    #ax.cla()
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = range(0, frame)
    y = []
    for value in x:
        x_in_radians = math.radians(value)
        y_sin = math.sin(x_in_radians)
        y.append(y_sin)
    ax.plot(x, y, 'ro:')

def run():
    global fig
    # your code here (use fig with animation function)
    simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 1)
    plt.show()

run()