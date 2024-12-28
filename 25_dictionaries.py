# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital exists.")
# else:
#     print("That capital doesn't exists.")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "New York"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# values = capitals.values()
# print(keys)
# for key in keys:
#     print(key)

# for value in values:
#     print(value)

for key, value in capitals.items():
    print(f"{key} : {value}.")
