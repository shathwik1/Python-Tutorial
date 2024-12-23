# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()

name = "Shathwik Reddy"
age = 17
gpa = 3.7
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print(bool(0))  # --> Returns False and True for any other value

# print(int(name)) # --> Returns an error because alphabets can't be converted to integer

print(int(gpa))
print(float(age))
print(bool(name))

print(bool(""))  # --> Returns False as it is empty
