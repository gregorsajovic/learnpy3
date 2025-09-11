# Collect string / test length

#import numbers


test_string = input("Please enter a test string: ")

if len(test_string) < 6:
  print("Your string is to short.")
  print("Please enter a string with at least 6 characters.")

# Prompt user to enter number / test if even or odd

def test_number(num):
  number = int(num)
  if number & 1:
    print("The number you entered is odd number")
  else:
    print("The number you entered is even number")

inp_num = input("Please enter a number: ")

if inp_num.isnumeric():
#  test_number(int(inp_num))
  test_number(inp_num)
else:
  print("The text you enterend is not a nubmer")
  inp_num = input("Please try again and this time enter a numeric value: ")
  if inp_num.isnumeric():
    test_number(inp_num)
  else:
    print("Still not a number, exiting.")


# Checking triangle sides:
# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.

a =  int(input("The length of side a = "))
b =  int(input("The length of side b = "))
c =  int(input("The length of side c = "))

if a!=b and b!=c and a!=c:
 print("This is a scalene triangle.")
elif a==b and b==c:
 print("This is an equilateral triangle.")
else: 
 print("This is an isosceles triangle.")

