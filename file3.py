import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies after the year: "))
year2 = int(input("Search movies before the year: "))
for index, item in enumerate(data):
        if (item["year"]) > year and (item["year"]) < year2:
            print(item["title"])