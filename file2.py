import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies after the year: "))
for index, item in enumerate(data):
    for i in range(year):
        print (data[]["year"])