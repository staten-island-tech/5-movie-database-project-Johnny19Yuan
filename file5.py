import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
title = (input("Search for movie title: "))
lowert = title.lower()
for index, item in enumerate(data):
        if (item["title"]).lower() == lowert:
            print(item["title"])
#bro fix it it no work 💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀