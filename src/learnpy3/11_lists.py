# Creating lists

example = list()
example = []

primes = [2,3,5,7,11,13]
primes.append(17)
primes.append(19)

print(primes)

print(primes[4])

print(str(primes[-1]) + " " + str(primes[-2]))


# Slicing

print(primes[2:5])

print(primes[0:6])

# Lists can contain: int, string, booleans, floats, complex numbers, other lists
# you can add multiple different types into same list and can also contain 
# duplicate values

example = [128, True, "Alpha", 1.8354, [54, False]]

rolls = [4, 7, 3, 7, 12, 4, 7]

print(example)
print(rolls)

# Combining lists - Concatenation
numbers = [1,2,3]
letters = ['a', 'b', 'c']
print(numbers + letters)
print(letters + numbers)

print(list(reversed(letters)))
print(list(reversed(numbers + letters)))



