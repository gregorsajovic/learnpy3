# Files divide into:
# Text Files: 
# - Plain Text
# - XML
# - JSON
# - Source Code 
# - ....
#
# Binary Files:
# - Compiled cod
# - App data
# - Media files
#   ~ images
#   ~ audio
#   ~ video
#   ~ ...

# to open file: help(open)

f = open("../../data/guido_bio.txt")
text = f.read()
f.close()

print(text)

# safer method for opening files
with open("../../data/guido_bio.txt") as fobj:
  bio = fobj.read()

print(bio)

# if file doesn't exist
try:
  with open("neki fajl.txt") as f:
    text = f.read()
except FileNotFoundError:
  text = None
print(text)


# Writing to the files. In this case if file don't exist will be created

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("../../data/oceans.txt", "w") as f:
  for ocean in oceans:
    f.write(ocean)
    f.write("\n") # writes each ocean in new line

# another way to write each ocean in new line:

with open("../../data/oceans2.txt", "w") as f:
  for ocean in oceans:
    print(ocean, file=f)

# write mode "w", rewrites all text in file, but if we don't want to loose old text we use
# append mode "a"

with open("../../data/oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are 5 oceans.", file=f)

