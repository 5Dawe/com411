import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()

def animate(frame):
    global ax
    ax.cla()
    ax.set_xlim(0, 360)
    ax.set_ylim(-1, 1)
    x = range(0, 360)
    y = []
    #for value in x:
    y = [math.sin(math.radians(degrees) + (frame / 1000)) for degrees in x]
    ax.plot(x, y, 'ro:')

def run():
    global fig
    # your code here (use fig with animation function)
    simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 1)
    plt.show()

run()