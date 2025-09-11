# Difference between List and Tuple
# List example:
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Display lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

# Iterate over both sequences
for p in prime_numbers:
 print("# Prime: ", p)

for p in perfect_squares:
 print("# Sqares: ", p)

# What is the difference
# Lists:
# - add data
# - remove data
# - change data
#
# Tuples:
# - Cannot be changed
# - "Immutable"
# - Made quiclkly

print("List methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))

print("Lists have more methods available than tuples, so lists ocupie more memory than tuples")

import sys

print(dir(sys))

# print(help(sys.getsizeof))
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
print("# Size of List: ", sys.getsizeof(list_eg))
print("# Size of Tuple: ",sys.getsizeof(tuple_eg))

import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)


# Tuple tests
empty_tuple = ()
test1 = ("a")
test1_1 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test1_1)
print(test2)
print(test3)

# Alternative Construction of Tuples

test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3

print(test1)
print(type(test1))

print(test2)
print(type(test2))

print(test3)
print(type(test3))

# Tuples with 1 element - Tuple Assigment
# (age, country, know_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country =", country)
print("Knows Python?", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2

print("Age = ", age)
print("Country =", country)
print("Knows Python?", knows_python)

