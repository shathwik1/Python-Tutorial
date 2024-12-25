# name = input("Enter your full name: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("o")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = name.count("e")
# result = name.replace("e", "E")

# print(result)
# print(dir(help(str)))

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters.")
elif username.find(" ") != -1:
    print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username can contain only alphabets.")
else:
    print(f"Welcome @{username}.")
