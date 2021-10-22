#A program to help Beep and Bop search the library.

# define a function to search
def search(f_name):
    print(f"\nSearching...")
    file = open(f_name)
    for lines in file:
        #This line was not required - python does this for you line = file.readline().strip()
        print(f"{lines}")
    file.close


#define a function to run
def run():
    search("library.txt")


if __name__ == "__main__":
    run()