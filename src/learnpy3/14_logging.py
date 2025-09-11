# Logging
# Purpose: Record progress and problems...
# Levels: Debug, Info, Warning, Error, Critical
# you can create additional levels

import logging
import math, cmath

# print(dir(logging))

# Create and configure logger
# basic level is 30 - WARNING 
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = ".//logs//Luberjack.log", 
		    level = logging.DEBUG, 
		    format = LOG_FORMAT,
		    filemode = 'w') # use this line if you want to rewrite the log file
logger = logging.getLogger()

# Test the logger
logger.info("Our second message.")

print(logger.level)

# -----------------------------
# | Level    |  Numeric Value |
# -----------------------------
# | NOTSET   |  0             |
# -----------------------------
# | DEBUG    |  10            |
# -----------------------------
# | INFO     |  20            |
# -----------------------------
# | WARNING  |  30            |
# -----------------------------
# | ERROR    |  40            |
# -----------------------------
# | CRITICAL |  50            |
# -----------------------------

# Let's create messages with all 5 levels
# Test messages
logger.debug("This is a harmles debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?!")
logger.critical("The entire internet is down!!!")

# Quadratic Formula
def quadratic_formula(a, b, c):
  """Return the sloutions to the equation ax^2 + bx + c = 0."""
  logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

  # Compute the discriminant
  logger.debug("# Compute the discriminant")
  disc = b**2 - 4*a*c

  # Compute the two roots
  logger.debug("# Compute the two roots")
  try:
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
  except ValueError:
    root1 = (-b + cmath.sqrt(disc)) / (2*a)
    root2 = (-b - cmath.sqrt(disc)) / (2*a)

  # Return the roots
  logger.debug("# Return the roots")
  return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)

roots = quadratic_formula(1, 0, 1)
print(roots)


