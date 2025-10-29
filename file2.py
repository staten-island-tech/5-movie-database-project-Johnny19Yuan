import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies after the year: "))
x = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(x)