import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies from the year: "))
for index, item in enumerate(data):
        if (item["year"]) == year:
            print(item["title"])