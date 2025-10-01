import json

json_file = open("../../data/movie_1.txt", "r", encoding="utf-8")

movie = json.load(json_file)

json_file.close()

print(movie)

value = """
    {"title": "Tron: Legacy",
     "composer": "Draft Punk",
     "release_year": 2010,
     "budget": 170000000,
     "actors": null,
     "won_oscar": false
    }"""

tron = json.loads(value)

print(tron)

print(json.dumps(movie))
print(json.dumps(movie, ensure_ascii=False))

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kamiński"

file2 = open("../../data/movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close()