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
    #file.close
    #print(f"{sections}\n\n{books}")
    ret_search = {sections}
    print(f"{ret_search}")
    return ret_search


#define function to save
def save(f_path, to_store):
    print(f"Saving...")
    print(f"{f_path}   {to_store}")
    with open(f_path, "w") as file:
        file.write(to_store)
    print(f"Done!")


#define a function to run
def run():
    search_return = (search("books.txt"))
    print(f"{search_return}")
    save("section-books.txt", search_return)


if __name__ == "__main__":
    run()