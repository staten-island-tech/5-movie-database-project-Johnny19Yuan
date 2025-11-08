import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
year = int(input("Search movies after the year: "))
years=[]
year =-1
x = 0
for index, item in enumerate(data):
    years.append(item["year"])
    if years[x] < year:
        years.pop
print(data[year]["title"])