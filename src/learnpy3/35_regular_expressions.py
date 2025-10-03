# Regular Expression - Regex - describes a search of string for a pattern

#  ^S.+a
#  S[a-t]*$
#  \w{9}

# Signs describing
#  ^ $          - Position
#  \w   [a-t]   - Set of characters
#  +  *  {9}    - Quantifiers


# Regex Position Patterns
#   regex         |    names
#   Fran (1,4)    |1    Francois         (contains "Fran")
#                 |2    Mike Whitney
#   ^Fran (1)     |3    Sagun Khatri     (starts with "Fran")
#                 |4    Nick Francesco
#                 |5    Pickles
#      i$ (3)     |6    K5ANR            


# Regex Character Sats
#   regex         |    names
#   \d (6)        |1    Francois         (digits)
#                 |2    Mike Whitney
#   \d\d  (0)     |3    Sagun Khatri     (two consecutive digits - no result)
#     \s (2,3,4)  |4    Nick Francesco   (whitespace)
#                 |5    Pickles
# \w (1,2,3,4,5,6)|6    K5ANR             (matches a-z, A-Z, 0-9, _) \w -> word
# ^\w\w\w\w\s  (2,4) - starts with 4 letters folowed by a whitespace  
# 


# Regex Quantifiers
#   regex         |    names
#  [aeiou]{2}     |1    Francois          (1) - searches for 2 consecutive vowels
#  ^\w{7}$        |2    Mike Whitney      (5) - searches for any names that are exactly 7 consecutive word characters
#  \w{7}          |3    Sagun Khatri      (1,2,4,5) - searches for any name that contains 7 consecutive word characters
#                 |4    Nick Francesco
#                 |5    Pickles
#                 |6    K5ANR

import re  # regular expressions 

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron  Cromberge',
         'Sohil']

# Find people with first and last name only
regex = r'^\w+\s+\w+$'

# for name in names:
#     result = re.search(regex, name)
#     if result:
#         print(name)

# for name in names:
#     result = re.search(regex, name)
#     if result:
#         print(result)

# Search for word char sequence starting with C
regex1 = r'C\w*'
# for name in names:
#     result = re.search(regex1, name)
#     if result:
#         print(name)
#         print(result.start())
#         print(result.end())
#         print(result.group())


names2 = ['Brian Daugette', 'Veronica Supersonica', 'Tony Gasparovic', 'Patrick Germann', 'm!sha']

# Test for first name and last name
# regex3 = r'^(?P<fn>\w+)\s+(?P<ln>\w+)$'
# for name in names2:
#     match = re.search(regex3, name)
#     if match:
#         print(name)
#         print(match.group('fn'))
#         print(match.group('ln'))


# Detect last name
regex4 = r'^[a-zA-Z!]+$'
for name in names2:
    if re.search(regex4, name):
        print(name)


# Scan for blocks or lower case letters
regex5 = r'[a-z]+'
for name in names2:
    matches = re.findall(regex5, name)
    if matches:
        print(matches)


# re.finditer(pattern, string, flags=0)
# Return an iterator yielding match objects over all non-overlapping matches for the RE pattern in string.
for name in names2:
    matches = re.finditer(regex5, name)
    for match in matches:
        print(match)



# re.match(pattern, string, flags=0) 
# If zero or more characters at the beginning of 'string' match the regular expression 'pattern', return a corresponding match object.
# Return  'None' if the string does not match the pattern.

values = ['https://www.socratica.com',
          'http://www.socratica.org', 
          'file://test.this.path',
          'com.socratica.www_https://']

# Test if string sarts with http or https
regex6 = r'https?'

for value in values:
    if re.match(regex6, value):
        print(value)


# re.fullmatch(pattern, string, flags=0)
# If the whole string matches the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern.

regex7 = r'https?://w{3}.\w+.(org|com)'
for value in values:
    if re.fullmatch(regex7, value):
        print(value)

# Want to #LearnMore ?
# https://docs.python.org/3/library/re.html

