# function = A block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthday {name}!")
#     print(f"You are {age+1} years old.")

# for i in range(1, 11):
#     happy_birthday("Bro")

# happy_birthday("Bro", 20)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Bro", 43.50, "01/04")
# display_invoice("Joe", 100.01, "09/12")

# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 4))
# print(subtract(10, 4))
# print(multiply(4, 9))
# print(divide(10, 5))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("bro", "code")
print(full_name)
