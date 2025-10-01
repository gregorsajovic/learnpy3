# List: [1, 2, "a", "b", 3.14, True]

# List comprehensions:
#   [expr for val in collection]
#   [expr for val in collection if <test>]
#   [expr for val in collection if <test1> and <test2>]
#   [expr for val1 in collection1 and val2 in collection2]


# Example: List of squares

squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 101)]
print(remainders11)

movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump", "Inception", "Fight Club", "The Matrix", "The Lord of the Rings: The Fellowship of the Ring", "The Lord of the Rings: The Return of the King", "The Lord of the Rings: The Two Towers", "Interstellar", "Gladiator", "Saving Private Ryan", "The Green Mile", "Se7en", "The Silence of the Lambs", "The Usual Suspects", "Schindler's List", "Goodfellas", "Braveheart", "Titanic", "The Departed", "The Prestige", "Memento", "Avatar", "Avengers: Endgame", "The Lion King", "Back to the Future", "Jurassic Park"]

# gmovies = []
# for title in movies:
#     if title.startswith("G"):
#         gmovies.append(title)

gmovies = [title for title in movies if title.startswith("G")]

print(gmovies)

ymovies = [("The Shawshank Redemption", 1994), ("The Godfather", 1972), ("The Dark Knight", 2008), ("Pulp Fiction", 1994), ("Forrest Gump", 1994), ("Inception", 2010), ("Fight Club", 1999), ("The Matrix", 1999), ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("The Lord of the Rings: The Return of the King", 2003), ("The Lord of the Rings: The Two Towers", 2002), ("Interstellar", 2014), ("Gladiator", 2000), ("Saving Private Ryan", 1998), ("The Green Mile", 1999), ("Se7en", 1995), ("The Silence of the Lambs", 1991), ("The Usual Suspects", 1995), ("Schindler's List", 1993), ("Goodfellas", 1990), ("Braveheart", 1995), ("Titanic", 1997), ("The Departed", 2006), ("The Prestige", 2006), ("Memento", 2000), ("Avatar", 2009), ("Avengers: Endgame", 2019), ("The Lion King", 1994), ("Back to the Future", 1985), ("Jurassic Park", 1993)]


pre2k = [title + "-" + str(year) for (title, year) in ymovies if year < 2000]
print(pre2k)

nums = [1, 2, 3, 4, 5]
multip = [4 * number for number in nums]
print(multip)

# Cartesian Product
# If A an B are sets, then the Cartesian product is the set of pairs (a, b) where 'a' is in A and 'b' is in B.
#  A x B = {(a, b) | a ∈ A, b ∈ B}
# Example:
# A = {1, 3}
# B = {x, y}
# A x B = {(1, x), (1, y), (3, x), (3, y)}
# 

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]

print(cartesian_product)