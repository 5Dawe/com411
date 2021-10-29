# A program to store data to a JSON file.

import json

def read(f_path):
  print(f"Reading...")
  with open("robocity.json") as file:
    data = json.load(file)
  print(f"Done!")
  return data

def save(s_path, save_d):
  print(f"Exporting...")
  with open(s_path, "w") as file:
    json.dump(save_d, file, indent = 4)
  print(f"Done!")


def run():
  json_data = read("robocity.josn")
  save("exported.json", json_data)


if __name__ == "__main__":
  run()

