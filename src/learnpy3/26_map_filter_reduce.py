# --------------- Map function ----------------

import math
def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

# Method 2: Use 'map' function

print(map(area, radii))

print(list(map(area, radii)))

# how 'map' function works:
# Data: a1, a2, ..., an
# Function: f
# map(f, data):
#   Returns iterator over
#   f(a1), f(a2), ..., f(an)


# Example for converting list of celsious to farenheit
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temps)))


# --------------- Filter function ----------------

# Example: Finda all data above the average.
import statistics # it contains mean function

data = [1.3, 2.7, 0.8, 4.2, 4.3, -0.3]

avg = statistics.mean(data)
print(avg)

favg = filter(lambda x: x > avg, data)

print(favg)
print(list(favg))

print(list(filter(lambda x: x < avg, data)))

# Remove missing data
# False values (None) => "", 0, 0.0, 0j, [], (), {}, False, None, instances which signal they are empty

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colobia", "", "Ecuador", "", "", "Venezuela"]

print(list(filter(None, countries)))


# --------------- Reduce function ----------------
# In Python 3+, reduce is not a builtin function - Moved to the 'functools' module
# Use functools.reduce() if you really need it; however, 99% of the time an explicit for loop is more readable.
# How it works:
# Data: [a1, a2, a3, ..., an]
# Function: f(x, y)
#
# reduce(f, data):
#   Step 1:    val1 = f(a1, a2)
#   Step 2:    val2 = f(val1, a3)
#   Step 3:    val3 = f(val2, a4)
#   ...
#   Step n-1: valn-1 = f(valn-2, an)
#   Return valn-1
#
# Alternatively:
#   Returns f(f(f(a1, a2), a3), a4), ..., an)

# Example: Multiply all numbers in a list

from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))

product = 1
for x in data:
    product = product * x

print(product)

