# A program to display information about the current working directory.

#Define Function
def cwd():
    import os
    path = os.getcwd()
    print(f"\nThe current working directory is {path}")
    print(f"\nThe directory contains the following files:")
    for file in os.listdir(path):
        print(file)

# Define function
def run():
    cwd()

run()
