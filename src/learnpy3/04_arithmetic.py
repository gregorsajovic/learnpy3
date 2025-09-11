print("""In python are 4 tipes of arithmetic operation: 
... - Addition
... - Subtraction
... - Multiplication
... - Dividion""")

a = 8 		# int
b = 6.0 	# float
c = 12 + 0j	# complex number

# Rule: Widen numbers so they're the same type

# Addition 
print("int + float = float, float + complex = complex, int + complex = complex")
print(a + b)

# Subtraction 
print("float - int = float, int - float = float, float - complex = complex, int - complex = complex")
print(b - a)
print(a-b)

# Multiplication
print("int * int = int, int * float = float, int * complex = complex, float * complex = complex")
print(a * 7)

# Division
print("int/float = float, float/complex = complex, int/complex = complex, complex/int = complex")
print(a/b)
print(b/c)
print(c/a)

print("The percent (%) operator returns remainder of the long division:")
print(a % b)
print("At division with  quotient without remainder use double slash '//':")
print(a//b)

print("Dividing by zero returns error: 'ZeroDivisionError'")
print(a/0)
