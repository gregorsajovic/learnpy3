# Fimonacci Sequence
# 1, 1, 2, 3, 5, 8, 13, 21
# frist two terms are always 1,1, next is  2 = 1 + 1, 3 = 2 + 1, 5 = 3 + 2 , 8 = 5 + 3, ...

# Goal: Write function to return nᵗʰ term of Fibonacci Sequence - fuction should be:
# - Fast
# - Clearly written
# - Rock solid

# because this function call itself we call it: Recursive Function
def fibonacci_one(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  elif n > 2:
    return fibonacci_one(n-1) + fibonacci_one(n-2)

# this would take forever so we need to improve our fucntion
# for n in range(1, 101):
#  print(n, ":", fibonacci_one(n))

# by using Memoization
# Idea: Cache values
# 1. Implement explicitly

fibonacci_cache = {}

def fibonacci_mem(n):
 # If we have cached the value, then return it 
 if n in fibonacci_cache: 
  return fibonacci_cache[n]
 # Compute the Nth term
 if n == 1:
  value = 1
 elif n == 2:
  value = 1
 elif n > 2:
  value = fibonacci_mem(n-1) + fibonacci_mem(n-2)
 
 # Cache the value and return it
 fibonacci_cache[n] = value
 return value

for n in range(1, 1001):
 print(n, ":", fibonacci_mem(n))

# 2. Use builtin Python tool
# LRU Cache = Least Recently Used Cache
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
 # Check that the input is a positive integer
 if type(n) != int:
  raise TypeError("n must be a positive int")
 if n < 1:
  raise ValueError("n must be a positive int")

 # Compute the Nth term
 if n == 1:
  return 1
 elif n == 2:
  return 1
 elif n > 2:
  return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 51):
 print(n, ":", fibonacci(n))

# What if we pass next values to the function: 2.1, 
#fibonacci(2.1)
#fibonacci(-1)
#fibonacci("one")

for n in range(1, 51):
 print(fibonacci(n+1) / fibonacci(n))
