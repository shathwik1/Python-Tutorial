import math

# Arithmetic Operations

# num_of_students = 10

# num_of_students = num_of_students + 1
# num_of_students += 1
# num_of_students = num_of_students - 1
# num_of_students -= 1
# num_of_students = num_of_students * 1
# num_of_students *= 1
# num_of_students = num_of_students / 1
# num_of_students /= 1
# num_of_students = num_of_students ** 2
# num_of_students **= 2

# remaining_num_of_students = num_of_students % 3

# print(remaining_num_of_students)
# print(num_of_students)


# Math functions


# result = round(2.9)
# result = abs(-2)
# result = pow(9, 3)
# result = max(9, 3, 1)
# result = min(9, 3, 1)

# result = math.pi
# result = math.e
# result = math.sqrt(9)
# result = math.ceil(4.1)
# result = math.floor(4.9)

# print(result)


# Exercise 1: Circumference of a circle
# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is {round(circumference, 2)}.")

# Exercise 2: Area of a circle
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The are of circle is {round(area, 2)}cm².")

# Exercise 3: Hypotenuse of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))

side_c = math.sqrt(pow(side_a, 2) + pow(side_b, 2))

print(f"Side c : {round(side_c, 2)}.")
