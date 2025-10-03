

# for i in range(5):
#     print("Živijo!")

# print(1/2)

# with open("x_files.txt") as xf:
#     the_truth = fx.read()

# print(the_truth)

#  ------- Exception Clauses ---------
#
#  try:
#    # Runs first
#    < code >
#  except:
#    # Runs if exception occurs in try bloc
#    < code >
#  else:
#    # Executes if try block *succeeds*
#    < code >
#  finally:
#    # This code *always" executes
#    < code >

# Objective:
# - Write function that reads binary file and returns data
# - Measure time required

import logging
import time

# Create logger
logging.basicConfig(filename="./logs/problems.log", level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'paht' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

data = read_file_timed("./data/test_non.png")