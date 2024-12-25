# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for x in reversed(range(1, 11, 2)):
#     print(x)

# for x in "abc":
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     print(x)

for x in range(1, 21):
    if x == 13:
        break
    print(x)
