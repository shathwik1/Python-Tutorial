# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# for x in range(3):
#     for y in range(1, 11):
#         print(y, end=" ")
#     print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for row in range(rows):
    for col in range(columns):
        print(symbol, end=" ")
    print()
