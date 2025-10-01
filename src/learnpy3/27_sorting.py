# Sorting alphabetically - Alkaline earth metals

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)
print(earth_metals)

# Touples can not be sorted   earth_metals_t = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")

ymovies = [("The Shawshank Redemption", 1994), ("The Godfather", 1972), ("The Dark Knight", 2008), ("Pulp Fiction", 1994), ("Forrest Gump", 1994), ("Inception", 2010), ("Fight Club", 1999), ("The Matrix", 1999), ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("The Lord of the Rings: The Return of the King", 2003), ("The Lord of the Rings: The Two Towers", 2002), ("Interstellar", 2014), ("Gladiator", 2000), ("Saving Private Ryan", 1998), ("The Green Mile", 1999), ("Se7en", 1995), ("The Silence of the Lambs", 1991), ("The Usual Suspects", 1995), ("Schindler's List", 1993), ("Goodfellas", 1990), ("Braveheart", 1995), ("Titanic", 1997), ("The Departed", 2006), ("The Prestige", 2006), ("Memento", 2000), ("Avatar", 2009), ("Avengers: Endgame", 2019), ("The Lion King", 1994), ("Back to the Future", 1985), ("Jurassic Park", 1993)]

year = lambda x: x[1]

ymovies.sort(key=year, reverse=True)

print(ymovies)

title = lambda x: x[0]

ymovies.sort(key=title, reverse=False)

print(ymovies)


# list.sort() changes the list
# Q: Can you create a sorted copy?
# Q: How do you sort a tuple?
# A: Use sorted() function


sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)
print(earth_metals)

# Tuple
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)

print(sorted(data))
print(data)

print(sorted("Alphabetically"))
