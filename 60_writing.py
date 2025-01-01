# Python writing files (.txt, .json, .csv)

import json
import csv
# txt_data = "I like pizza!"

# file_path = "output.txt"

# try:
#     with open(file=file_path, mode="x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path} was created")
# except FileExistsError:
#     print("That file already exists!")

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# try:
#     with open(file=file_path, mode="a") as file:
#         for employee in employees:
#             file.write("\n" + employee)
#         print(f"txt file '{file_path} was created")
# except FileExistsError:
#     print("That file already exists!")

# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

# file_path = "this.json"

# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "this.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
