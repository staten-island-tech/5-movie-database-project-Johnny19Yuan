import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = input("Search movies after the year: ")
