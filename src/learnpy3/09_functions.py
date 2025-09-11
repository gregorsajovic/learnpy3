
import math

def ping():
  return "Ping!"

x = ping()

print(x)


def volumeSphere(r):
  """Returns the volume of a sphere with radius r."""
  v = (4.0/3.0) * math.pi * r**3
  return v

retvol = volumeSphere(int(input("Enter the radious of the sphere: ") or 0)) 

print(f"The volume of the sphere is: {retvol}")


# Function that computes the eria of triangle:

def triangle_area(b, h):
  """Returns the area of a triangle with base b and height h."""
  return 0.5 * b * h

b = int(input("Enter base length: ") or 1) 
h = int(input("Enter heigth of triangle: ") or 1)

y = triangle_area(b, h)

print(f"The area of triangle is: {y} sqare units")


# Function that converts american units into centimeters

def cm(feet = 0, inches = 0):
  """Conversts a length from feet and inches to centimeters."""
  inches_to_cm = inches * 2.54
  feet_to_cm = feet * 12 * 2.54
  return inches_to_cm + feet_to_cm

ft = int(input("Enter feet to transform to cm: ") or 0)
inc = int(input("Enter inches to transform to cm: ") or 0)

cm = cm(ft, inc)

print(f"The value of {ft} feet and value of {inc} inches is equal to {cm} centimeters")

# Types of Arguments in functions:
# - Keyword:	It has = sign
# - Required:	Does not have = sign
# Rules:
# - in function you can write both type of arguments at the same time, but
#   if you do, the keyword argument must come last.



