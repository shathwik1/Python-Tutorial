# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules"))
# print(help("os"))

# import math
# print(math.e)
# print(math.pi)
# print(math.pow(2, 3))
# import math as m
# print(m.e)
# from math import e
# print(e)

import example

result = example.pi
result = example.square(3)
result = example.cube(4)
result = example.circumference(2)
result = example.area(6)

print(result)
