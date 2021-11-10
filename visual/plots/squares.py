# A program to display the path Beep and Bop are taking through Robo City.



# import graphical plotting module
import matplotlib.pyplot as plt



# The first function should be named small and should have no parameters.
def small():
    x = [3, 4, 4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, 'ro:')


#The second function should be named medium and should have no parameters.
def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, 'gs--')


#The third function should be named large and should have no parameters.
def large():
    x = [1, 6, 6, 1, 1]
    y = [1, 1, 6, 6, 1]
    plt.plot(x, y, 'pb-')

# run the program to display the plots
def run():
    small()
    medium()
    large()
    plt.show()


if __name__ == "__main__":
    run()



