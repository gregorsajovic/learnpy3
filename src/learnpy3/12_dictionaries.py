# Dictionaries

# FriendFace post
# ----------------------------------------
#  Key     |  Value
# user_id  = 209
# message  = "D5 E5 C5 C4 G4"
# language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)

post = {"user_id":209,  "message":"D5 E5 C5 C4 G4", "language":"English",  "datetime":"20230215T124231Z", "location":(44.590533, -104.715556)}

print(type(post))
print(post)

post2 = dict(message="SS Cotton", language="English")
print(post2)

post2["user_id"] = 208
post2["datetime"] = "19771116T090221Z"

print(post2)

# Accessing Data in dictionaries

print(post['message'])

# if you try to access data that doesn't exist you get KeyError
# print(post2['location'])

# solution:

if 'location' in post2:
  print(post2['location'])
else: 
  print("The post does not contain a location value.")

# or

try:
  print(post2['city'])
except KeyError:
  print("The post doesn't have a city.")

# Another way to access dictionari

print(post2.get('location', None))

# iterate trough the values in dictionari

for key in post.keys():
  value = post[key]
  print(key, "=", value)

# another way
for key, value in post.items():
  print(key, "=", value)



