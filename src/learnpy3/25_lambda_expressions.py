# Lambda Expressions - anonymus expresions

def f(x):
    return 3*x + 1

print(f(2))

# lambda is python keyword in next case for lambda expressions
print(lambda x: 3*x + 1)

g = lambda x: 3*x + 1

print(g(5))


full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   leonhard", "EULER"))


# How to write Lambda Expressions in general
#  lambda : "What is my purpose?"
#  lambda x: 3*x+1
#  lambda x, y: (x*y)**0.5 # Geometric Mean
#  lambda x, y, z: 3/(1/x + 1/y + 1/y)  # Harmonic Mean
#  ...
#  lambda x1, x2, ..., xn: <expression>

sifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Hainlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
print(sifi_authors)
# help(scifi_authors.sort)

sifi_authors .sort(key=lambda name: name.split(" ")[-1].lower())
print(sifi_authors)


# Quadratic Functions - for instance to calculate cannon ball projectory
# f(x) = a x**2 + b x + c

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

print(build_quadratic_function(3, 0, 1)(2)) # 3x^2+1 evaluated for x=2

