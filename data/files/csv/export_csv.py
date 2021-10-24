# A program to export user data as a CSV file.

# define function to export data to a csv
def export(f_path, num_bots):
    print(f"Exporting...")
    for count in range(0, num_bots):
        print(f"Please enter the bot id:")
        bot_id = str(input())
        print(f"Please enter the bot name:")
        bot_name = str(input())
        print(f"Please enter the bot paint:")
        bot_paint = str(input())
        user_data = bot_id + "," + bot_name + "," + bot_paint + "\n"
        print(f"{user_data}\n")
        with open(f_path, "a") as file:
            file.write(user_data)
    print(f"Done!")







#define a function to run
def run():
    export("exported_bots.csv", 2)

# run program if not called
if __name__ == "__main__":
    run()