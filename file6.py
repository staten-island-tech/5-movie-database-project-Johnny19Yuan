import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
genre = (input("Search for movie genre: "))

for movie in data:
    for item in movie["genres"]:
        if item == genre:
            print(movie["title"])