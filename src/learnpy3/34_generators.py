# GENERATORS ->
# - Functions that act like iterators
# - "Generates" the elements in a loop
# - "On demand" iteration

# ITERATORS -> Loops over objects in memory


def f():
    return 1
    return 2
    return 3

print(f())


def g():
    yield 1
    yield 2
    yield 3

print(g())

for x in g():
    print(x)

import string

# Generate the lower case English letters
def letters():
    for c in string.ascii_lowercase:
        yield c
    
for letter in letters():
    print(letter)

# Function that uses yield instead of return is called Generator Function - "Generator"

import itertools

def prime_numbers():
    # Handle the first prime
    yield 2
    prime_cache = [2] # Cache of primes

    # Loop over positive, odd integers
    for n in itertools.count(3,2):
        is_prime = True

        # Check to see if any prime number divides n
        for p in prime_cache:
            if n % p == 0: # p divides n evenly
                is_prime = False
                break

        # Is it prime?
        if is_prime:
            prime_cache.append(n)
            yield n

count = 0

for p in prime_numbers():
    print(p)
    count += 1
    if p > 100:
        print(count)
        break

import sys

squares = (x**2 for x in itertools.count(1))

print(type(squares))

for x in squares:
    print(x)

    if x > 5000:
        squares.close()    


print(sys.getsizeof(squares))