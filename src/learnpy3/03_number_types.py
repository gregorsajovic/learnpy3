import sys # this imports library of system functions

print("""In python2 there are next types of numbers:
...			- int
...			- long
...			- float
...			- complex""")
print("""
...
... First int - INTEGER:""")

a = 28  #this is a perfect number
print(type(a))
print(a)

b = 2147483647
print(type(b))
print(b)

print("""
...
... Second long - LONG INTEGER:""")

c = 21474836492
print(c)
print(type(c))

# d = sys.maxint
# print(d)
# print(type(d))

# e = -sys.maxint
# print(e)
# print(type(e))

f = 5
print(f)
print(type(f))

print("""
...
... Third FLOATS:""")

g = 2.718281828
print(g)
print(type(g))

print("""
...
... Fourth COMPLEX NUMBERS:""")

z = 3 + 5.7j
print(z)
print(type(z))
print(z.real)
print(z.imag)

h = 34j
print(h)
print(type(h))
print(h.real)
print(h.imag)

