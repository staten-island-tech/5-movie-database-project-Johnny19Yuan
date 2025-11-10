import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
movieyear=[]
x = 0
for index, item in enumerate(data):
    movieyear.append(data[x]["title"])
    movieyear.append(data[x]["year"])
    x = x + 1
print(movieyear)
year = int(input("Search for movies after the year: "))