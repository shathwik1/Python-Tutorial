# Python reading file (.txt, .json, .csv)
import json
import csv


# file_path = "output.txt"
file_path = "this.csv"

try:
    with open(file=file_path, mode="r") as file:
        # print(file.read())
        # content = json.load(file)
        # print(content["name"])
        content = csv.reader(file)
        for line in content:
            print(line[1], line[2])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
