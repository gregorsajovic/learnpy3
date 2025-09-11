# Operating with numbers
a = 3
b = 8

print(f"""We have two wariables: 
... a = 4 
... b = 5 
...
... and if we compare these valueslike in different ways we get:
... bool(a == b): {bool(a == b)}
... bool(a < b): {bool(a < b)}
... bool(a > b): {bool(a > b)}
... bool(a != b): {bool(a != b)}
""")


print(f'What type is True: {type(True)}')

print(f"What type is bool(28): {bool(28)}")

print(f"What type is bool(-2.718): {bool(-2.14)}")

print(f"What type is bool(0): {bool(0)}")

# Operating with strings

print(f"If we evaluate text: bool('Turning') we get result: {bool('Turning')}")

print(f"If we evaluate space: bool(' ') we get result: {bool(' ')}")

print(f"If we evaluate empty string: bool('') we get result: {bool('')}")

print(""" Boolean Conversions
... trivial  	-> False
... non-trivial -> True""")

# Conversion of boolean to other types

print(f"Converting True to string, you get 'True' with quotes -> example: str(True) you get: {str(True)}, same goes to False")

print(f"Converting True to integer, you get nuber of type int: 1 -> example: int(True) you get: {int(True)}")

print(f"Converting False to string, you get number of type int: 0 -> example: int(False) you get: {str(False)}")

print(f"If you add 5 + True, you get 6 -> example:  {5 + True}")

print(f"If you add 5 + False, you get 5 -> example:  {5 + False}")

print(f"If you multiply  5 * False, you get 0 -> example:  {5 * False}")




