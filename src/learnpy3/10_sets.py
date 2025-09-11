# Sets, adding and removeing

example = set()

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorioum")

print(example)
print(len(example))

example.remove(42)

print(example)
print(len(example))

example.discard(False)

print(example)
print(len(example))


example2 = set([28, False, 2.32432, "Helioulium"])

print(example2)
print(len(example2))


example2.clear()

print(example2)
print(len(example2))

# Set union
# Integers 1 - 10

odds = set([1,3,5,7,9])
evens = set([2, 4, 6, 8, 10])
primes = set([2,3,5,7])
composites = set ([4, 6, 8, 9, 10])

print(f"These are odd numbers between 1 and 10: {odds}")

print(f"These are even numbers between 1 and 10: {evens}")

print(odds.union(evens))

print(evens.union(odds))

print(f"This is intersection of odds and primes: {odds.intersection(primes)}")

print(f"This is intersection of primes and evens: {primes.intersection(evens)}")

print(f"This is intersection of evens and odds: {evens.intersection(odds)}")

print(f"This is the union of prime and composite numbers: {primes.union(composites)}")

# Checking for elements in sets:

print(f"Is number 2 in primes? {2 in primes}")

print(f"Is number 6 in odds? {6 in odds}")

print(f"Is number 9 not in evens? {9 not in primes}")

