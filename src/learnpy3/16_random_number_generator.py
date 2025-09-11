#WARNING: The pseudo-random generators of this module should not be used for security purposes. Use os.urandom() or SystemRandom if you require a cryptographically secure pseudo-random number generator.

import random
# print(dir(random))

# Display 10 random numbers from interval [0, 1]

#for i in range(10):
# print(random.random())

# Generate random numbers from interval [3, 7]

def my_random():
 # Random, scale, shift, return...
 return 4*random.random() + 3

for i in range(10):
 print(my_random())

# print(dir(random))
# print(help(random.uniform))


# The random() function can be used to build customiyed random nubmer generators.

for i in range(10):
 print(random.uniform(3, 7))

# random() and uniform() are both uniform distributions.
# Normal Ditributon (aka "Bell Curve") -> | Mean and _ Standard Deviaton

for i in range(20):
 print(random.normalvariate(3, 0.2))

# Random Integer - randint(min, max)

for i in range(20):
 print(random.randint(1,6))

# Random element from list
outcomes = ['rock', 'paper', 'scissors']

for i in range(20):
 print(random.choice(outcomes))

