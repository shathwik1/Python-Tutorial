# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# double = []

# for x in range(1, 11):
#     double.append(x * 2)

# print(double)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# squares = [x * x for x in range(1, 11)]
# print(doubles)
# print(triples)
# print(squares)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits_chars = [fruit[0] for fruit in fruits]

# print(fruits_chars)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num >= 0]
# print(positive_nums)

# even_nums = [even_num for even_num in numbers if even_num % 2 == 0]
# print(even_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade = [grade for grade in grades if grade >= 60]
print(passing_grade)
