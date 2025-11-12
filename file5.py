import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
title = (input("Search for movie title: "))
for index, item in enumerate(data):
        if (item["title"]) == title:
            print(item["title"])
#bro fix it it no work💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀67