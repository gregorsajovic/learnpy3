# Unit tests

from math import pi

def circle_area(r):
    return pi*(r**2)

# Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circles with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))


# Naming Convention #1 =>   /circles.py  ->  /test_circles.py
# Naming Convention #2 =>   /circles.py  ->  /circles_test.py
# Also you can put tests in separate folder



