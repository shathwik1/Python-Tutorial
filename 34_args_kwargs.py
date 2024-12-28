# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# def add(*args):
#     print(type(args))
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum


# print(add(1, 2, 3))


# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name("Monkey", "D", "Luffy")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_address(street="123 Fake St.",
#               city="Detroit",
#               state="MI",
#               zip="54321")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    else:
        print(f"{kwargs.get("street")}")

    print(f"{kwargs.get("city")} {kwargs.get("state")}, {kwargs.get("zip")}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")
