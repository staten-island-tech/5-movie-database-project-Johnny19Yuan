import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies after the year: "))
years=[]
for index, item in enumerate(data):
    year =-1
    if 
print(data[year]["title"])