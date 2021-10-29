# A program to help Beep and Bop find their way through the maze.

# define 2 functions

def directions():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn Left")
    directions.append("Turn Right")
    print(f"{directions}")

def run():
    directions()

if __name__ == "__main__":
    run()