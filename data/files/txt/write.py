# a program to help Beep and Bop search the books

#define function to search
def search(f_path):
    print(f"\nSearching...")
    sections = ""
    books = "Books:\n"
    file = open(f_path)
    for line in file:
        if line.startswith("Section"):
            print(f"sec")
            sections = sections + "\n" + line
        else:
            print(f"book")
            books = books + "\n" + line
    file.close
    print(f"{sections}")
    print(f"{books}")









#define function to save





#define a function to run
def run():
    search("books.txt")


if __name__ == "__main__":
    run()