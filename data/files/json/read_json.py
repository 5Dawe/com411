# A program to display the content of a JSON file

# import json module
import json

def open_bots():
  with open("robocity.json") as file:
    data = json.load(file)
    #display the name of the city & population
    city = data["city"]
    population = data["population"]
    print(f"The name of the city is {city}")
    print(f"Population is {population}")
    #display the name of each bot
    bots = data["bots"]

    for bot in bots:
      bot_name = bot["name"]
      #you need to call stats first before calling strength
      bot_stats = bot["stats"]
      bot_strength = bot_stats["strength"]
      bot_speed = bot_stats["speed"]

      print(f"{bot_name} has a strength level of {bot_strength} and a speed level of {bot_speed}")
      #print(f"The name of the first bot is: {bot_name}{bot_strength}{bot_speed}")


def run():
  open_bots()


if __name__ == "__main__":
  run()