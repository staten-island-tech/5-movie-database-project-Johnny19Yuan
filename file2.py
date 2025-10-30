import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies after the year: "))
x = print(data[year]["title"])