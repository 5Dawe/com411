# A program to help Beep and Bop search the library.

def display_chars(f_path, ch_read):
    file = open(f_path)
    partial_data = file.read(ch_read)
    print(f"\nThe first character is:")
    print(f"{partial_data}")
    file.close


def display_line(f_path):
    file = open(f_path)
    line = file.readline().strip()
    print(f"\nThe first line is:")
    print(f"{line}")
    file.close

def display_text(f_path):
    with open(f_path) as file:
        print(f"\nThe full text is:")
        data = file.read()
        print(data)

def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()


