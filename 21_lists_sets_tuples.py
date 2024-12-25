# collection = single 'variable' used to store multiple values
# List = [] ordered and changeable, Duplicate OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# Lists
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(fruits[0:3])
# print(fruits[0::-1])

# print(len(fruits))
# print("banana" in fruits)
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("pineapple"))
# print(fruits.count("apple"))

# for fruit in fruits:
#     print(fruit)


# Sets
# fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()

# print(fruits)

# Tuple
fruits = ("apple", "orange", "banana", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

print(fruits.index("coconut"))
print(fruits.count("coconut"))
