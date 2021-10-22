# a program to help Beep and Bop search the books

#define function to search
def search(f_path):
    print(f"\nSearching...")
    sections = ""
    books = "Books:\n"
    file = open(f_path)
    for line in file:
        if line.startswith("Section"):
            sections = sections + "\n" + line
        else:
            books = books + "\n" + line
    file.close
    #print(f"{sections}\n\n{books}")
    ret_search = {sections}
    return ret_search


#define function to save
def save(f_path, to_store):
    print(f"{ret_search}")
    print(f"Done!")

#define a function to run
def run():
    search("books.txt")


if __name__ == "__main__":
    run()