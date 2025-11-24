import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
title = (input("Search for movie title: "))
for index, item in enumerate(data):
        if title.lower() in (item["title"]).lower():
            print(item["title"])

 


#("bro fix it it it it it no work